"""HeroSignal istisnaları."""

from typing import Any, Dict, Optional


class HeroSignalError(Exception):
    """API hata zarfından (``{"error": {"code", "message", "request_id", "details"}}``) türetilen istisna.

    Ağ hatalarında ``status`` 0 ve ``code`` ``"NETWORK"`` olur.
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
            f"HeroSignalError(status={self.status!r}, code={self.code!r}, "
            f"message={self.message!r}, request_id={self.request_id!r})"
        )


class WebhookSignatureError(Exception):
    """Webhook imzası geçersiz. ``reason``: ``missing_header``, ``malformed_header``,
    ``timestamp_out_of_tolerance``, ``signature_mismatch`` veya ``malformed_body``."""

    def __init__(self, reason: str) -> None:
        super().__init__(f"HeroSignal webhook imzası geçersiz: {reason}")
        self.reason = reason
