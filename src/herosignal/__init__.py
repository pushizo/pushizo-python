"""HeroSignal Python sunucu SDK'sı.

.. code-block:: python

    from herosignal import HeroSignal

    hs = HeroSignal(api_key="hs_live_…", app_id="app_…")
    hs.notifications.create({"target": {"include_aliases": {"external_id": ["u1"]}}, "contents": {"en": "Hi"}})
"""

from ._client import DEFAULT_BASE_URL, DEFAULT_MAX_RETRIES, DEFAULT_TIMEOUT, HeroSignal
from ._errors import HeroSignalError, WebhookSignatureError
from ._generated import API_VERSION
from ._types import FileContent, FileInput, RequestOptions
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
    "API_VERSION",
    "DEFAULT_BASE_URL",
    "DEFAULT_MAX_RETRIES",
    "DEFAULT_TIMEOUT",
    "FileContent",
    "FileInput",
    "HeroSignal",
    "HeroSignalError",
    "RequestOptions",
    "WEBHOOK_DEFAULT_TOLERANCE_SECONDS",
    "WEBHOOK_EVENT_ID_HEADER",
    "WEBHOOK_SIGNATURE_HEADER",
    "WebhookSignatureError",
    "WebhookVerifyResult",
    "__version__",
    "construct_webhook_events",
    "verify_webhook_signature",
]
