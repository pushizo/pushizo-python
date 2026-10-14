"""HeroSignal HTTP istemcisi: kimlik doğrulama, yeniden deneme, idempotency ve sayfalama."""

import hashlib
import hmac
import json
import mimetypes
import os
import time
import uuid
from email.utils import parsedate_to_datetime
from typing import Any, Callable, Dict, Iterator, List, Mapping, Optional, Tuple
from urllib.parse import quote

import httpx

from ._errors import HeroSignalError, NetworkError, error_class_for_status
from ._generated.resources import GeneratedResources
from ._types import FileInput, RequestOptions
from ._version import __version__

DEFAULT_BASE_URL = "https://api.herosignal.dev"
DEFAULT_TIMEOUT = 30.0
DEFAULT_MAX_RETRIES = 3
_BACKOFF_SECONDS = (0.3, 1.0, 3.0)


class HeroSignal(GeneratedResources):
    """HeroSignal sunucu SDK istemcisi.

    .. code-block:: python

        from herosignal import HeroSignal

        hs = HeroSignal(api_key=os.environ["HS_API_KEY"], app_id="app_…")
        hs.notifications.create(
            {"target": {"include_aliases": {"external_id": [user_id]}}, "contents": {"en": "Shipped"}},
            idempotency_key=f"order-{order_id}",
        )

    Kaynaklar (``notifications``, ``users``, ``segments``, ``templates``, ``campaigns`` …; tam liste
    ``herosignal._generated.resources.RESOURCE_NAMES``) ``api/openapi.yaml``'dan üretilir.
    """

    def __init__(
        self,
        api_key: str,
        *,
        app_id: Optional[str] = None,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        auto_idempotency_key: bool = True,
        user_agent: Optional[str] = None,
        http_client: Optional[httpx.Client] = None,
        sleep: Callable[[float], None] = time.sleep,
    ) -> None:
        """
        :param api_key: ``hs_live_…`` API anahtarı (Bearer).
        :param app_id: Çağrılarda ``app_id`` verilmezse kullanılacak varsayılan app.
        :param base_url: API adresi; yerel geliştirmede ``http://localhost:4000``.
        :param timeout: İstek zaman aşımı (saniye).
        :param max_retries: 429/5xx ve ağ hatalarında en fazla yeniden deneme.
        :param auto_idempotency_key: ``Idempotency-Key`` destekleyen çağrılarda anahtar verilmezse UUID üret.
        :param http_client: Özel ``httpx.Client`` (proxy, TLS, test transport'u). Verilirse kapatılması çağırana aittir.
        :param sleep: Yeniden deneme beklemesi (testlerde değiştirilebilir).
        """
        if not api_key:
            raise ValueError("HeroSignal: api_key gerekli.")
        self.api_key = api_key
        self.app_id = app_id
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries
        self.auto_idempotency_key = auto_idempotency_key
        self.user_agent = user_agent or f"herosignal-python/{__version__}"
        self._owns_http = http_client is None
        self._http = http_client if http_client is not None else httpx.Client()
        self._sleep = sleep
        self._init_resources()

    # -- yaşam döngüsü -------------------------------------------------------------------------

    def close(self) -> None:
        """İstemcinin kendi oluşturduğu bağlantı havuzunu kapatır."""
        if self._owns_http:
            self._http.close()

    def __enter__(self) -> "HeroSignal":
        return self

    def __exit__(self, *_exc: Any) -> None:
        self.close()

    # -- yardımcılar ---------------------------------------------------------------------------

    @staticmethod
    def identity_hash(sdk_secret: str, external_id: str) -> str:
        """SDK identity verification için ``identity_hash = HMAC-SHA256(sdk_secret, external_id)`` (hex)."""
        return hmac.new(sdk_secret.encode("utf-8"), external_id.encode("utf-8"), hashlib.sha256).hexdigest()

    def request(
        self,
        method: str,
        path: str,
        *,
        query: Optional[Mapping[str, Any]] = None,
        body: Any = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Any:
        """Düşük seviyeli istek (SDK'da henüz metodu olmayan uçlar veya ``format=csv`` gibi JSON dışı yanıtlar için).

        JSON yanıtlar ayrıştırılır, diğer içerik tipleri metin olarak döner.
        """
        return self._send(method, path, list(_query_items(query or {})), body, None, None, None, request_options)

    # -- üretilmiş kaynakların kullandığı iç API -----------------------------------------------

    def _resolve_app_id(self, app_id: Optional[str]) -> str:
        resolved = app_id or self.app_id
        if not resolved:
            raise ValueError("HeroSignal: app_id verilmedi (istemci seçeneği veya çağrı parametresi).")
        return resolved

    def _call(
        self,
        method: str,
        path: str,
        *,
        path_params: Mapping[str, str],
        query: Optional[Mapping[str, Any]] = None,
        body: Any = None,
        form: Optional[Mapping[str, Any]] = None,
        files: Optional[Mapping[str, Optional[FileInput]]] = None,
        app_id: Optional[str] = None,
        query_app_id: bool = False,
        body_app_id: bool = False,
        idempotent: bool = False,
        idempotency_key: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Any:
        url_path = path
        if "{appId}" in url_path:
            url_path = url_path.replace("{appId}", quote(self._resolve_app_id(app_id), safe=""))
        for name, value in path_params.items():
            if value is None or value == "":
                raise ValueError(f"HeroSignal: '{name}' yol parametresi boş olamaz.")
            url_path = url_path.replace("{" + name + "}", quote(str(value), safe=""))

        items: List[Tuple[str, str]] = []
        if query_app_id:
            items.append(("app_id", self._resolve_app_id(app_id)))
        items.extend(_query_items(query or {}))

        if body_app_id and isinstance(body, Mapping) and not body.get("app_id"):
            body = {**body, "app_id": self._resolve_app_id(app_id)}

        key = idempotency_key or (request_options or {}).get("idempotency_key")
        if not key and isinstance(body, Mapping) and isinstance(body.get("idempotency_key"), str):
            key = body["idempotency_key"]
        if not key and idempotent and self.auto_idempotency_key:
            key = str(uuid.uuid4())

        return self._send(method, url_path, items, body, form, files, key, request_options)

    def _paginate(self, fetch: Callable[[Optional[str]], Any], cursor: Optional[str]) -> Iterator[Any]:
        """``data`` / ``next_cursor`` / ``has_more`` zarfını sayfa sayfa dolaşır."""

        def generator() -> Iterator[Any]:
            next_cursor = cursor
            while True:
                page = fetch(next_cursor) or {}
                for item in page.get("data") or []:
                    yield item
                next_cursor = page.get("next_cursor")
                if not page.get("has_more") or not next_cursor:
                    return

        return generator()

    # -- HTTP ----------------------------------------------------------------------------------

    def _send(
        self,
        method: str,
        path: str,
        query: List[Tuple[str, str]],
        body: Any,
        form: Optional[Mapping[str, Any]],
        files: Optional[Mapping[str, Optional[FileInput]]],
        idempotency_key: Optional[str],
        request_options: Optional[RequestOptions],
    ) -> Any:
        opts: RequestOptions = request_options or {}
        headers: Dict[str, str] = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
            "User-Agent": self.user_agent,
        }
        content: Optional[bytes] = None
        data: Optional[Dict[str, str]] = None
        upload: Optional[Dict[str, Tuple[str, bytes, str]]] = None
        if files is not None:
            data = {k: _form_value(v) for k, v in (form or {}).items() if v is not None}
            upload = {k: _normalize_file(v) for k, v in files.items() if v is not None}
        elif body is not None:
            headers["Content-Type"] = "application/json"
            content = json.dumps(body, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
        if idempotency_key:
            headers["Idempotency-Key"] = idempotency_key
        headers.update(opts.get("headers") or {})

        url = f"{self.base_url}{path}"
        timeout = opts.get("timeout", self.timeout)
        max_retries = opts.get("max_retries", self.max_retries)
        # Gövdedeki idempotency_key, API tarafında Idempotency-Key başlığıyla eşdeğerdir.
        has_key = any(k.lower() == "idempotency-key" and v for k, v in headers.items()) or (
            isinstance(body, Mapping) and isinstance(body.get("idempotency_key"), str) and bool(body["idempotency_key"])
        )
        attempt = 0
        while True:
            response: Optional[httpx.Response] = None
            not_sent = False
            try:
                response = self._http.request(
                    method,
                    url,
                    params=query or None,
                    headers=headers,
                    content=content,
                    data=data,
                    files=upload,
                    timeout=timeout,
                )
            except httpx.TransportError as exc:
                error = NetworkError(0, "NETWORK", str(exc) or exc.__class__.__name__)
                not_sent = isinstance(exc, _NOT_SENT_ERRORS)
            else:
                if 200 <= response.status_code < 300:
                    return _parse_body(response)
                error = _error_from_response(response)
            if attempt >= max_retries or not _should_retry(method, error, has_key, not_sent):
                raise error
            self._sleep(_retry_delay(response, attempt))
            attempt += 1


#: Sunucuda tekrarlanması ek yan etki doğurmayan HTTP metotları; 5xx ve ağ hatalarında serbestçe yeniden denenir.
_IDEMPOTENT_METHODS = frozenset({"GET", "HEAD", "OPTIONS", "PUT", "DELETE"})

#: İstek sunucuya hiç ulaşmadan oluşan aktarım hataları: bağlantı reddi / DNS çözümlenemedi (``ConnectError``),
#: bağlantı kurma ve bağlantı havuzu zaman aşımı.
_NOT_SENT_ERRORS = (httpx.ConnectError, httpx.ConnectTimeout, httpx.PoolTimeout)


def _should_retry(method: str, error: HeroSignalError, has_idempotency_key: bool, not_sent: bool) -> bool:
    """Yeniden deneme politikası.

    - 429: her metotta yeniden denenir (istek işlenmeden reddedilmiştir; ``Retry-After``'a uyulur).
    - 5xx / ağ hatası: GET, HEAD, OPTIONS, PUT, DELETE her zaman; POST ve PATCH yalnızca ``Idempotency-Key``
      taşıyorsa (otomatik anahtar dahil) veya istek sunucuya hiç gönderilmeden başarısız olduysa (bağlantı reddi,
      DNS hatası, bağlantı zaman aşımı). Aksi hâlde sunucu isteği işlemiş olabilir; tekrar, çift kayıt üretebilir.
    """
    if error.status == 429:
        return True
    if not error.retryable:
        return False
    return method.upper() in _IDEMPOTENT_METHODS or has_idempotency_key or not_sent


def _query_items(query: Mapping[str, Any]) -> Iterator[Tuple[str, str]]:
    for key, value in query.items():
        if value is None:
            continue
        if isinstance(value, (list, tuple)):
            for v in value:
                if v is not None:
                    yield key, _scalar(v)
        else:
            yield key, _scalar(value)


def _scalar(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (str, int, float)):
        return str(value)
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def _form_value(value: Any) -> str:
    return _scalar(value)


def _normalize_file(value: FileInput) -> Tuple[str, bytes, str]:
    """Dosya girdisini (ad, bayt, içerik tipi) üçlüsüne çevirir; akış bir kez okunur ki yeniden denemeler aynı içeriği göndersin."""
    filename: Optional[str] = None
    content_type: Optional[str] = None
    raw: Any = value
    if isinstance(value, tuple):
        filename = value[0]
        raw = value[1]
        if len(value) > 2:
            content_type = value[2]  # type: ignore[misc]
    if not isinstance(raw, (bytes, bytearray)):
        if filename is None:
            name = getattr(raw, "name", None)
            if isinstance(name, str):
                filename = os.path.basename(name)
        raw = raw.read()
    if filename is None:
        filename = "upload"
    if content_type is None:
        content_type = mimetypes.guess_type(filename)[0] or "application/octet-stream"
    return filename, bytes(raw), content_type


def _parse_body(response: httpx.Response) -> Any:
    if not response.content:
        return None
    content_type = response.headers.get("content-type", "")
    if "json" in content_type or not content_type:
        return response.json()
    return response.text


def _error_from_response(response: httpx.Response) -> HeroSignalError:
    envelope: Dict[str, Any] = {}
    try:
        parsed = response.json()
        if isinstance(parsed, dict) and isinstance(parsed.get("error"), dict):
            envelope = parsed["error"]
    except ValueError:
        envelope = {}
    details = envelope.get("details")
    return error_class_for_status(response.status_code)(
        response.status_code,
        str(envelope.get("code") or f"HTTP_{response.status_code}"),
        str(envelope.get("message") or f"HTTP {response.status_code}"),
        envelope.get("request_id") or response.headers.get("x-request-id"),
        details if isinstance(details, dict) else None,
    )


def _retry_delay(response: Optional[httpx.Response], attempt: int) -> float:
    """``Retry-After`` (saniye veya HTTP tarihi) varsa ona uyar; yoksa 0.3 / 1 / 3 sn geri çekilme."""
    if response is not None:
        header = response.headers.get("retry-after")
        if header:
            header = header.strip()
            try:
                seconds = float(header)
                if seconds > 0:
                    return seconds
            except ValueError:
                try:
                    delta = parsedate_to_datetime(header).timestamp() - time.time()
                    if delta > 0:
                        return delta
                except (TypeError, ValueError):
                    pass
    return _BACKOFF_SECONDS[min(attempt, len(_BACKOFF_SECONDS) - 1)]
