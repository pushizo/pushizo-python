"""HeroSignal istisnaları ve hata kodları."""

from typing import Any, Dict, Optional, Type


class ErrorCode:
    """API hata zarfındaki ``error.code`` değerleri (``HS_`` önekli katalog)."""

    VALIDATION_ERROR = "HS_VALIDATION_ERROR"
    BAD_REQUEST = "HS_BAD_REQUEST"
    UNAUTHENTICATED = "HS_UNAUTHENTICATED"
    FORBIDDEN = "HS_FORBIDDEN"
    TENANT_MISMATCH = "HS_TENANT_MISMATCH"
    NOT_FOUND = "HS_NOT_FOUND"
    CONFLICT = "HS_CONFLICT"
    IDEMPOTENCY_CONFLICT = "HS_IDEMPOTENCY_CONFLICT"
    IDEMPOTENCY_IN_PROGRESS = "HS_IDEMPOTENCY_IN_PROGRESS"
    NO_RECIPIENTS = "HS_NO_RECIPIENTS"
    CHANNEL_NOT_CONFIGURED = "HS_CHANNEL_NOT_CONFIGURED"
    CONTENT_INVALID = "HS_CONTENT_INVALID"
    SUBSCRIPTION_INVALID = "HS_SUBSCRIPTION_INVALID"
    UNPROCESSABLE = "HS_UNPROCESSABLE"
    RATE_LIMITED = "HS_RATE_LIMITED"
    QUOTA_EXCEEDED = "HS_QUOTA_EXCEEDED"
    INTERNAL = "HS_INTERNAL"
    NOT_IMPLEMENTED = "HS_NOT_IMPLEMENTED"
    PROVIDER_UNAVAILABLE = "HS_PROVIDER_UNAVAILABLE"
    SERVICE_UNAVAILABLE = "HS_SERVICE_UNAVAILABLE"
    #: İstemci tarafı: bağlantı kurulamadı / zaman aşımı (``status`` 0).
    NETWORK = "NETWORK"


class HeroSignalError(Exception):
    """API hata zarfından (``{"error": {"code", "message", "request_id", "details"}}``) türetilen istisna.

    Ağ hatalarında ``status`` 0 ve ``code`` ``"NETWORK"`` olur. HTTP durumuna göre alt sınıflar
    (:class:`NotFoundError`, :class:`RateLimitError` …) fırlatılır; hepsi bu sınıftan türer.
    """

    def __init__(
        self,
        status: int,
        code: str,
        message: str,
        request_id: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None,
    ) -> None:
        super().__init__(message)
        self.status = status
        self.code = code
        self.message = message
        self.request_id = request_id
        self.details = details

    @property
    def retryable(self) -> bool:
        """429, 5xx veya ağ hatası: yeniden denenebilir."""
        return self.status == 0 or self.status == 429 or self.status >= 500

    def __str__(self) -> str:
        suffix = f" (request_id={self.request_id})" if self.request_id else ""
        return f"[{self.status} {self.code}] {self.message}{suffix}"

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}(status={self.status!r}, code={self.code!r}, "
            f"message={self.message!r}, request_id={self.request_id!r})"
        )


class NetworkError(HeroSignalError):
    """Bağlantı kurulamadı veya zaman aşımı (``status`` 0)."""


class InvalidRequestError(HeroSignalError):
    """400 / 422: istek doğrulanamadı veya işlenemedi (``details`` alan hatalarını içerir)."""


class AuthenticationError(HeroSignalError):
    """401: API anahtarı eksik veya geçersiz."""


class PermissionDeniedError(HeroSignalError):
    """403: anahtarın kapsamı yetersiz, IP izin listesi dışı veya kaynak başka kiracıya ait."""


class NotFoundError(HeroSignalError):
    """404: kaynak bulunamadı."""


class ConflictError(HeroSignalError):
    """409: kaynak çakışması veya idempotency anahtarı çakışması."""


class RateLimitError(HeroSignalError):
    """429: hız sınırı veya plan kotası aşıldı."""


class ServerError(HeroSignalError):
    """5xx: sunucu veya sağlayıcı geçici olarak kullanılamıyor."""


def error_class_for_status(status: int) -> Type[HeroSignalError]:
    """HTTP durumuna karşılık gelen istisna sınıfı."""
    if status == 0:
        return NetworkError
    if status in (400, 422):
        return InvalidRequestError
    if status == 401:
        return AuthenticationError
    if status == 403:
        return PermissionDeniedError
    if status == 404:
        return NotFoundError
    if status == 409:
        return ConflictError
    if status == 429:
        return RateLimitError
    if status >= 500:
        return ServerError
    return HeroSignalError


class WebhookSignatureError(Exception):
    """Webhook imzası geçersiz. ``reason``: ``missing_header``, ``malformed_header``,
    ``timestamp_out_of_tolerance``, ``signature_mismatch`` veya ``malformed_body``."""

    def __init__(self, reason: str) -> None:
        super().__init__(f"HeroSignal webhook imzası geçersiz: {reason}")
        self.reason = reason
