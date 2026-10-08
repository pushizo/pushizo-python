"""Webhook imza doğrulaması: sdk/testdata/webhook-signature-vectors.json ortak vektörleri (Node/PHP ile aynı)."""

import hashlib
import hmac
import json
from pathlib import Path

import pytest

from herosignal import (
    WEBHOOK_SIGNATURE_HEADER,
    WebhookSignatureError,
    construct_webhook_events,
    verify_webhook_signature,
)

VECTORS_PATH = Path(__file__).resolve().parents[2] / "testdata" / "webhook-signature-vectors.json"
VECTORS = json.loads(VECTORS_PATH.read_text(encoding="utf-8"))["cases"]


@pytest.mark.parametrize("case", VECTORS, ids=[c["name"] for c in VECTORS])
def test_vector(case):
    result = verify_webhook_signature(
        case["payload"],
        case["header"],
        case["secrets"],
        tolerance_seconds=case["toleranceSeconds"],
        now=case["now"],
    )
    expected = case["expected"]
    assert result.ok is expected["ok"]
    if expected["ok"]:
        assert result.timestamp == expected["timestamp"]
    else:
        assert result.reason == expected["reason"]


EVENT_CASES = [c for c in VECTORS if "events" in c]


@pytest.mark.parametrize("case", EVENT_CASES, ids=[c["name"] for c in EVENT_CASES])
def test_construct_events(case):
    # Ham baytlarla da aynı sonuç alınmalı (çerçeveler gövdeyi bytes verir).
    for payload in (case["payload"], case["payload"].encode("utf-8")):
        events = construct_webhook_events(
            payload,
            case["header"],
            case["secrets"],
            tolerance_seconds=case["toleranceSeconds"],
            now=case["now"],
        )
        assert len(events) == case["events"]
        assert all(isinstance(e, dict) and "type" in e for e in events)


def test_construct_events_raises_with_reason():
    case = next(c for c in VECTORS if c["expected"].get("reason") == "signature_mismatch")
    with pytest.raises(WebhookSignatureError) as info:
        construct_webhook_events(case["payload"], case["header"], case["secrets"], now=case["now"])
    assert info.value.reason == "signature_mismatch"


def test_header_list_uses_first_value():
    case = VECTORS[0]
    result = verify_webhook_signature(case["payload"], [case["header"]], case["secrets"][0], now=case["now"])
    assert result.ok


def test_malformed_body_after_valid_signature():
    body = "not json"
    sig = hmac.new(b"s", b"1800000000." + body.encode(), hashlib.sha256).hexdigest()
    with pytest.raises(WebhookSignatureError) as info:
        construct_webhook_events(body, f"t=1800000000,v1={sig}", "s", now=1800000000)
    assert info.value.reason == "malformed_body"


def test_header_constant():
    assert WEBHOOK_SIGNATURE_HEADER == "HeroSignal-Signature"
