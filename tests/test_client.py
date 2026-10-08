"""İstemci davranışı: kimlik doğrulama, app kapsamı, idempotency, yeniden deneme, hata eşleme, sayfalama."""

import hashlib
import hmac
import json
import uuid

import httpx
import pytest

from herosignal import HeroSignal, HeroSignalError

from .conftest import json_response

NOTIFICATION = {"target": {"include_aliases": {"external_id": ["u1"]}}, "contents": {"en": "Hi"}}


def body_of(request: httpx.Request):
    return json.loads(request.content.decode("utf-8"))


def test_requires_api_key():
    with pytest.raises(ValueError):
        HeroSignal("")


def test_headers_and_body_app_id(server):
    server.queue(json_response(202, {"id": "msg_1"}))
    hs = server.client()
    result = hs.notifications.create(NOTIFICATION)
    assert result == {"id": "msg_1"}
    req = server.requests[0]
    assert req.method == "POST"
    assert str(req.url) == "https://api.test/v1/notifications"
    assert req.headers["authorization"] == "Bearer hs_live_test"
    assert req.headers["accept"] == "application/json"
    assert req.headers["content-type"] == "application/json"
    assert req.headers["user-agent"].startswith("herosignal-python/")
    assert body_of(req)["app_id"] == "app_default"
    # Çağıranın sözlüğü değiştirilmez.
    assert "app_id" not in NOTIFICATION


def test_app_id_override_and_path_escaping(server):
    server.queue(json_response(200, {"id": "seg_1"}))
    hs = server.client()
    hs.segments.get("seg/1", app_id="app_other")
    assert server.requests[0].url.raw_path == b"/v1/apps/app_other/segments/seg%2F1"


def test_query_app_id_and_params(server):
    server.queue(json_response(200, {"data": [], "next_cursor": None, "has_more": False}))
    hs = server.client()
    hs.notifications.list(limit=10, status="completed")
    params = server.requests[0].url.params
    assert params["app_id"] == "app_default"
    assert params["limit"] == "10"
    assert params["status"] == "completed"
    assert "cursor" not in params


def test_missing_app_id():
    hs = HeroSignal("k", http_client=httpx.Client(transport=httpx.MockTransport(lambda r: httpx.Response(200))))
    with pytest.raises(ValueError):
        hs.segments.list()


def test_auto_idempotency_key_reused_across_retries(server):
    server.queue(
        json_response(503, {"error": {"code": "UNAVAILABLE", "message": "x"}}),
        json_response(202, {"id": "m"}),
    )
    hs = server.client()
    hs.notifications.create(NOTIFICATION)
    keys = [r.headers.get("idempotency-key") for r in server.requests]
    assert len(keys) == 2 and keys[0] == keys[1]
    uuid.UUID(keys[0])


def test_explicit_and_body_idempotency_key(server):
    server.queue(json_response(202, {"id": "m"}), json_response(202, {"id": "m"}))
    hs = server.client()
    hs.notifications.create(NOTIFICATION, idempotency_key="order-1")
    hs.notifications.create({**NOTIFICATION, "idempotency_key": "order-2"})
    assert server.requests[0].headers["idempotency-key"] == "order-1"
    assert server.requests[1].headers["idempotency-key"] == "order-2"


def test_auto_idempotency_disabled_and_non_idempotent_ops(server):
    server.queue(json_response(202, {"id": "m"}), json_response(200, {"id": "s"}))
    hs = server.client(auto_idempotency_key=False)
    hs.notifications.create(NOTIFICATION)
    hs.suppressions.create({"channel": "email", "value": "a@b.c"})
    assert all("idempotency-key" not in r.headers for r in server.requests)


def test_retry_backoff_and_retry_after(server):
    server.queue(
        json_response(500, {}),
        json_response(429, {}, {"retry-after": "2"}),
        json_response(502, {}),
        json_response(200, {"ok": True}),
    )
    hs = server.client()
    assert hs.apps.list() == {"ok": True}
    assert server.sleeps == [0.3, 2.0, 3.0]


def test_retry_after_past_http_date_falls_back(server):
    server.queue(json_response(429, {}, {"retry-after": "Wed, 21 Oct 2015 07:28:00 GMT"}), json_response(200, {}))
    hs = server.client()
    hs.apps.list()
    assert server.sleeps == [0.3]


def test_retries_exhausted(server):
    server.queue(*[json_response(503, {"error": {"code": "UNAVAILABLE", "message": "down"}}) for _ in range(3)])
    hs = server.client(max_retries=2)
    with pytest.raises(HeroSignalError) as info:
        hs.apps.list()
    assert info.value.status == 503 and info.value.code == "UNAVAILABLE"
    assert len(server.requests) == 3
    assert server.sleeps == [0.3, 1.0]


def test_client_error_not_retried_and_mapped(server):
    server.queue(
        json_response(
            422,
            {"error": {"code": "VALIDATION_FAILED", "message": "bad", "request_id": "req_1", "details": {"field": "x"}}},
        )
    )
    hs = server.client()
    with pytest.raises(HeroSignalError) as info:
        hs.apps.list()
    err = info.value
    assert (err.status, err.code, err.message, err.request_id, err.details) == (
        422,
        "VALIDATION_FAILED",
        "bad",
        "req_1",
        {"field": "x"},
    )
    assert not err.retryable
    assert len(server.requests) == 1
    assert "req_1" in str(err)


def test_error_without_envelope_uses_header_request_id(server):
    server.queue(httpx.Response(404, content=b"not found", headers={"x-request-id": "req_h"}))
    hs = server.client()
    with pytest.raises(HeroSignalError) as info:
        hs.apps.get()
    assert (info.value.code, info.value.request_id) == ("HTTP_404", "req_h")


def test_network_error_retried(server):
    server.queue(httpx.ConnectError("boom"), httpx.ReadTimeout("slow"), json_response(200, {"ok": 1}))
    hs = server.client()
    assert hs.apps.list() == {"ok": 1}
    assert server.sleeps == [0.3, 1.0]


def test_network_error_exhausted(server):
    server.queue(httpx.ConnectError("boom"))
    hs = server.client(max_retries=0)
    with pytest.raises(HeroSignalError) as info:
        hs.apps.list()
    assert info.value.status == 0 and info.value.code == "NETWORK" and info.value.retryable


def test_request_options_override(server):
    server.queue(json_response(500, {}))
    hs = server.client()
    with pytest.raises(HeroSignalError):
        hs.apps.list(request_options={"max_retries": 0, "headers": {"X-Trace": "t1"}})
    assert server.requests[0].headers["x-trace"] == "t1"
    assert len(server.requests) == 1


def test_pagination(server):
    server.queue(
        json_response(200, {"data": [{"id": "s1"}, {"id": "s2"}], "next_cursor": "c2", "has_more": True}),
        json_response(200, {"data": [{"id": "s3"}], "next_cursor": None, "has_more": False}),
    )
    hs = server.client()
    ids = [s["id"] for s in hs.segments.list_all(limit=2)]
    assert ids == ["s1", "s2", "s3"]
    assert "cursor" not in server.requests[0].url.params
    assert server.requests[1].url.params["cursor"] == "c2"
    assert server.requests[1].url.params["limit"] == "2"


def test_query_encoding(server):
    server.queue(json_response(200, {}))
    hs = server.client()
    hs.request("GET", "/v1/custom", query={"a": True, "b": [1, 2], "c": None, "d": {"x": 1}})
    url = server.requests[0].url
    assert url.params.get_list("b") == ["1", "2"]
    assert url.params["a"] == "true"
    assert url.params["d"] == '{"x":1}'
    assert "c" not in url.params


def test_non_json_response_returned_as_text(server):
    server.queue(httpx.Response(200, content=b"a,b\n1,2\n", headers={"content-type": "text/csv"}))
    hs = server.client()
    assert hs.request("GET", "/v1/apps/app_default/analytics/messages", query={"format": "csv"}) == "a,b\n1,2\n"


def test_empty_response_is_none(server):
    server.queue(httpx.Response(204))
    hs = server.client()
    assert hs.request("DELETE", "/v1/x") is None


def test_multipart_upload(server):
    server.queue(json_response(201, {"id": "imp_1"}))
    hs = server.client()
    hs.imports.create("csv_users", ("users.csv", b"external_id\nu1\n"))
    req = server.requests[0]
    assert req.url.path == "/v1/apps/app_default/imports"
    assert req.headers["content-type"].startswith("multipart/form-data")
    raw = req.content.decode("utf-8")
    assert 'name="type"' in raw and "csv_users" in raw
    assert 'filename="users.csv"' in raw and "external_id" in raw


def test_identity_hash():
    expected = hmac.new(b"secret", b"user-1", hashlib.sha256).hexdigest()
    assert HeroSignal.identity_hash("secret", "user-1") == expected


def test_resources_present(server):
    hs = server.client()
    for name in ("notifications", "users", "subscriptions", "segments", "templates", "campaigns", "webhooks"):
        assert hasattr(hs, name)


def test_context_manager_closes_owned_client():
    with HeroSignal("k") as hs:
        assert hs._owns_http
    assert hs._http.is_closed
