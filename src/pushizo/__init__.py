"""Pushizo Python sunucu SDK'sı.

.. code-block:: python

    from pushizo import Pushizo

    hs = Pushizo(api_key=os.environ["HS_API_KEY"], app_id="app_…")
    hs.notifications.create({"target": {"include_aliases": {"external_id": ["u1"]}}, "contents": {"en": "Shipped"}})
"""

from ._client import DEFAULT_BASE_URL, Pushizo
from ._errors import (
    AuthenticationError,
    ConflictError,
    ErrorCode,
    PushizoError,
    InvalidRequestError,
    NetworkError,
    NotFoundError,
    PermissionDeniedError,
    RateLimitError,
    ServerError,
    WebhookSignatureError,
)
from ._generated import API_VERSION
from ._identity import identity_token
from ._types import FileInput, RequestOptions
from ._version import __version__
from ._webhooks import (
    WEBHOOK_DEFAULT_TOLERANCE_SECONDS,
    WEBHOOK_EVENT_ID_HEADER,
    WEBHOOK_SIGNATURE_HEADER,
    WebhookVerifyResult,
    construct_webhook_events,
    verify_webhook_signature,
)

__all__ = [
    "identity_token",
    "API_VERSION",
    "DEFAULT_BASE_URL",
    "WEBHOOK_DEFAULT_TOLERANCE_SECONDS",
    "WEBHOOK_EVENT_ID_HEADER",
    "WEBHOOK_SIGNATURE_HEADER",
    "AuthenticationError",
    "ConflictError",
    "ErrorCode",
    "FileInput",
    "Pushizo",
    "PushizoError",
    "InvalidRequestError",
    "NetworkError",
    "NotFoundError",
    "PermissionDeniedError",
    "RateLimitError",
    "RequestOptions",
    "ServerError",
    "WebhookSignatureError",
    "WebhookVerifyResult",
    "__version__",
    "construct_webhook_events",
    "verify_webhook_signature",
]
