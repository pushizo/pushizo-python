"""Giden webhook imza doğrulaması (alıcı tarafı).

Başlık: ``HeroSignal-Signature: t=<unix>,v1=<hex>``; ``v1 = HMAC-SHA256(secret, f"{t}.{ham_gövde}")``.
Secret rotasyonunda başlıkta iki ``v1`` bulunabilir; herhangi biri eşleşirse imza geçerlidir.
"""

import hashlib
import hmac
import json
import re
import time
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Sequence, Union

from ._errors import WebhookSignatureError

#: İmza başlığı adı (çerçeveler küçük harfe çevirebilir: ``herosignal-signature``).
WEBHOOK_SIGNATURE_HEADER = "HeroSignal-Signature"
#: Olay kimliği başlığı; tekrar gönderimleri ayıklamak için kullanın.
WEBHOOK_EVENT_ID_HEADER = "HeroSignal-Event-Id"
#: Varsayılan zaman damgası toleransı (sn); daha eski ``t`` tekrar (replay) sayılır.
WEBHOOK_DEFAULT_TOLERANCE_SECONDS = 300

_TIMESTAMP = re.compile(r"[0-9]+")
_SIGNATURE = re.compile(r"[0-9a-f]{64}")


@dataclass(frozen=True)
class WebhookVerifyResult:
    """Doğrulama sonucu. ``ok`` doğruysa ``timestamp``, değilse ``reason`` doludur."""

    ok: bool
    timestamp: Optional[int] = None
    reason: Optional[str] = None


def _to_bytes(payload: Union[str, bytes, bytearray]) -> bytes:
    if isinstance(payload, (bytes, bytearray)):
        return bytes(payload)
    return payload.encode("utf-8")


def verify_webhook_signature(
    payload: Union[str, bytes, bytearray],
    header: Union[str, Sequence[str], None],
    secret: Union[str, Sequence[str]],
    *,
    tolerance_seconds: int = WEBHOOK_DEFAULT_TOLERANCE_SECONDS,
    now: Optional[float] = None,
) -> WebhookVerifyResult:
    """HeroSignal webhook imzasını doğrular.

    ``payload`` HAM istek gövdesi olmalıdır (JSON'u ayrıştırıp yeniden serileştirmeyin).
    ``secret`` rotasyon sırasında eski ve yeni secret'ı içeren bir liste olabilir.
    ``now`` test için Unix zamanıdır (saniye). Karşılaştırma sabit zamanlıdır.
    """
    raw = header[0] if isinstance(header, (list, tuple)) and header else header
    if not raw or not isinstance(raw, str):
        return WebhookVerifyResult(ok=False, reason="missing_header")
    timestamp: Optional[int] = None
    signatures: List[str] = []
    for part in raw.split(","):
        idx = part.find("=")
        if idx <= 0:
            continue
        key = part[:idx].strip()
        value = part[idx + 1 :].strip()
        if key == "t" and _TIMESTAMP.fullmatch(value):
            timestamp = int(value)
        elif key == "v1" and _SIGNATURE.fullmatch(value):
            signatures.append(value)
    if timestamp is None or not signatures:
        return WebhookVerifyResult(ok=False, reason="malformed_header")
    current = int(time.time() if now is None else now)
    if abs(current - timestamp) > tolerance_seconds:
        return WebhookVerifyResult(ok=False, reason="timestamp_out_of_tolerance")
    body = _to_bytes(payload)
    secrets = [secret] if isinstance(secret, str) else list(secret)
    for s in secrets:
        expected = hmac.new(s.encode("utf-8"), f"{timestamp}.".encode("ascii") + body, hashlib.sha256).hexdigest()
        if any(hmac.compare_digest(expected, sig) for sig in signatures):
            return WebhookVerifyResult(ok=True, timestamp=timestamp)
    return WebhookVerifyResult(ok=False, reason="signature_mismatch")


def construct_webhook_events(
    payload: Union[str, bytes, bytearray],
    header: Union[str, Sequence[str], None],
    secret: Union[str, Sequence[str]],
    *,
    tolerance_seconds: int = WEBHOOK_DEFAULT_TOLERANCE_SECONDS,
    now: Optional[float] = None,
) -> List[Dict[str, Any]]:
    """İmzayı doğrular ve gövdeyi olay listesine çevirir (tekil gövde veya ``{"events": [...]}`` batch).

    Geçersiz imzada :class:`WebhookSignatureError` fırlatır.
    """
    result = verify_webhook_signature(payload, header, secret, tolerance_seconds=tolerance_seconds, now=now)
    if not result.ok:
        raise WebhookSignatureError(result.reason or "signature_mismatch")
    try:
        body = json.loads(_to_bytes(payload).decode("utf-8"))
    except ValueError as exc:
        raise WebhookSignatureError("malformed_body") from exc
    if not isinstance(body, dict):
        raise WebhookSignatureError("malformed_body")
    events = body.get("events")
    if isinstance(events, list):
        return events
    return [body]
