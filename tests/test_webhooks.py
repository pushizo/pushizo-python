"""Ortak webhook imza vektörleri (sdk/testdata/webhook-signature-vectors.json)."""

import json
from pathlib import Path

import pytest

from herosignal import WebhookSignatureError, construct_webhook_events, verify_webhook_signature

VECTORS = json.loads(
    (Path(__file__).resolve().parents[2] / "testdata" / "webhook-signature-vectors.json").read_text(encoding="utf-8")
)


@pytest.mark.parametrize("case", VECTORS["cases"], ids=[c["name"] for c in VECTORS["cases"]])
def test_vector(case):
    secret = case["secrets"][0] if len(case["secrets"]) == 1 else case["secrets"]
    result = verify_webhook_signature(
        case["payload"], case["header"], secret, tolerance_seconds=case["toleranceSeconds"], now=case["now"]
    )
    expected = case["expected"]
    assert result.ok is expected["ok"]
    if expected["ok"]:
        assert result.timestamp == expected["timestamp"]
    else:
        assert result.reason == expected["reason"]
    # Aynı vektör bayt girdisiyle de aynı sonucu vermeli.
    as_bytes = verify_webhook_signature(
        case["payload"].encode("utf-8"), case["header"], case["secrets"], tolerance_seconds=case["toleranceSeconds"], now=case["now"]
    )
    assert as_bytes.ok is expected["ok"]
    if "events" in case:
        events = construct_webhook_events(
            case["payload"], case["header"], case["secrets"], tolerance_seconds=case["toleranceSeconds"], now=case["now"]
        )
        assert len(events) == case["events"]
    elif not expected["ok"]:
        with pytest.raises(WebhookSignatureError) as info:
            construct_webhook_events(
                case["payload"], case["header"], case["secrets"], tolerance_seconds=case["toleranceSeconds"], now=case["now"]
            )
        assert info.value.reason == expected["reason"]


def test_header_list_uses_first_value():
    case = VECTORS["cases"][0]
    result = verify_webhook_signature(case["payload"], [case["header"]], case["secrets"], now=case["now"])
    assert result.ok
