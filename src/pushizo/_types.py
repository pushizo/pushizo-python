"""Çağrı seçenekleri ve dosya yükleme tipleri."""

from typing import IO, Dict, Tuple, TypedDict, Union

#: Dosya içeriği: bayt dizisi veya ikili okunabilir akış (ör. ``open(path, "rb")``).
FileContent = Union[bytes, IO[bytes]]

#: Multipart dosya alanı: içerik, ``(dosya_adı, içerik)`` veya ``(dosya_adı, içerik, içerik_tipi)``.
FileInput = Union[FileContent, Tuple[str, FileContent], Tuple[str, FileContent, str]]


class RequestOptions(TypedDict, total=False):
    """Tek bir çağrı için istemci ayarlarını geçersiz kılar."""

    #: İstek zaman aşımı (saniye).
    timeout: float
    #: 429/5xx ve ağ hatalarında en fazla yeniden deneme sayısı.
    max_retries: int
    #: Ek HTTP başlıkları.
    headers: Dict[str, str]
    #: ``Idempotency-Key`` başlığı (her istekte elle verilebilir).
    idempotency_key: str
