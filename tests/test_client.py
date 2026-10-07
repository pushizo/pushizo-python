"""HTTP katmanı: kimlik doğrulama, app kapsamı, idempotency, yeniden deneme, hatalar ve sayfalama."""

import json
import re

import httpx
import pytest

from herosignal import (
    AuthenticationError,
    ErrorCode,
    HeroSignal,
    HeroSignalError,
    InvalidRequestError,
    NetworkError,
    NotFoundError,
    RateLimitError,
    ServerError,
)


class Recorder:
    """Sıralı yanıtlar döndüren ``httpx.MockTransport`` işleyicisi."""

    def __init__(self, responses):
        self.responses = list(responses)
        self.requests = []

    def __call__(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        item = self.responses.pop(0)
        if isinstance(item, Exception):
            raise item
        return item


def make(responses, **kwargs):
    rec = Recorder(responses)
    sleeps = []
    client = HeroSignal(
        "hs_live_test",
        app_id="app_1",
        base_url="https://api.test/",
        http_client=httpx.Client(transport=httpx.MockTransport(rec)),
        sleep=sleeps.append,
        **kwargs,
    )
    return client, rec, sleeps


def json_response(status, body, headers=None):
    return httpx.Response(status, json=body, headers=headers)


def test_create_notification_sends_auth_app_and_idempotency():
    hs, rec, _ = make([json_response(202, {"id": "msg_1", "status": "queued"})])
    res = hs.notifications.create({"target": {"include_aliases": {"external_id": ["u1"]}}, "contents": {"tr": "Merhaba"}})
    assert res["id"] == "msg_1"
    req = rec.requests[0]
    assert req.method == "POST"
    assert str(req.url) == "https://api.test/v1/notifications"
    assert req.headers["authorization"] == "Bearer hs_live_test"
    assert req.headers["user-agent"].startswith("herosignal-python/")
    body = json.loads(req.content)
    assert body["app_id"] == "app_1"
    assert body["contents"]["tr"] == "Merhaba"
    assert re.fullmatch(r"[0-9a-f-]{36}", req.headers["idempotency-key"])


def test_explicit_and_body_idempotency_key():
    hs, rec, _ = make([json_response(202, {"id": "m"}), json_response(202, {"id": "m"})])
    hs.notifications.create({"contents": {"en": "x"}}, idempotency_key="order-1")
    hs.notifications.create({"contents": {"en": "x"}, "idempotency_key": "order-2"}, app_id="app_2")
    assert rec.requests[0].headers["idempotency-key"] == "order-1"
    assert rec.requests[1].headers["idempotency-key"] == "order-2"
    assert json.loads(rec.requests[1].content)["app_id"] == "app_2"


def test_auto_idempotency_can_be_disabled_and_not_sent_for_other_posts():
    hs, rec, _ = make([json_response(202, {"id": "m"}), json_response(200, {"accepted": 1})], auto_idempotency_key=False)
    hs.notifications.create({"contents": {"en": "x"}})
    hs.events.send({"events": [{"external_id": "u1", "name": "purchase"}]})
    assert "idempotency-key" not in rec.requests[0].headers
    assert "idempotency-key" not in rec.requests[1].headers


def test_query_and_path_encoding():
    hs, rec, _ = make([json_response(200, {"data": []}), json_response(200, {"id": "usr_1"})])
    hs.notifications.list(limit=10, status="completed")
    assert str(rec.requests[0].url) == "https://api.test/v1/notifications?app_id=app_1&limit=10&status=completed"
    hs.users.get_by_alias("crm id", "a/b", app_id="app 2")
    assert rec.requests[1].url.raw_path == b"/v1/apps/app%202/users/by/crm%20id/a%2Fb"


def test_missing_app_id_raises():
    hs = HeroSignal("k", http_client=httpx.Client(transport=httpx.MockTransport(lambda r: httpx.Response(200))))
    with pytest.raises(ValueError):
        hs.apps.get()


def test_retry_after_and_backoff_then_success():
    hs, rec, sleeps = make(
        [
            json_response(429, {"error": {"code": "HS_RATE_LIMITED", "message": "yavaş"}}, {"retry-after": "2"}),
            json_response(503, {"error": {"code": "HS_SERVICE_UNAVAILABLE", "message": "x"}}),
            httpx.ConnectError("bağlantı yok"),
            json_response(200, {"id": "msg_1"}),
        ]
    )
    res = hs.notifications.create({"contents": {"en": "x"}})
    assert res["id"] == "msg_1"
    assert sleeps == [2.0, 1.0, 3.0]
    keys = {r.headers["idempotency-key"] for r in rec.requests}
    assert len(keys) == 1, "yeniden denemelerde aynı idempotency anahtarı"


def test_typed_errors_and_no_retry_on_4xx():
    hs, rec, sleeps = make(
        [
            json_response(
                404,
                {"error": {"code": "HS_NOT_FOUND", "message": "yok", "request_id": "req_1", "details": {"id": "x"}}},
            ),
            json_response(400, {"error": {"code": "HS_VALIDATION_ERROR", "message": "kötü"}}),
            json_response(401, {"error": {"code": "HS_UNAUTHENTICATED", "message": "anahtar"}}),
        ]
    )
    with pytest.raises(NotFoundError) as info:
        hs.notifications.get("msg_x")
    err = info.value
    assert isinstance(err, HeroSignalError)
    assert (err.status, err.code, err.request_id, err.details) == (404, ErrorCode.NOT_FOUND, "req_1", {"id": "x"})
    assert not err.retryable
    with pytest.raises(InvalidRequestError):
        hs.segments.get("seg_1")
    with pytest.raises(AuthenticationError):
        hs.apps.list()
    assert sleeps == []
    assert len(rec.requests) == 3


def test_retries_exhausted():
    hs, rec, sleeps = make([json_response(500, {})] * 4)
    with pytest.raises(ServerError) as info:
        hs.apps.list()
    assert info.value.code == "HTTP_500"
    assert len(rec.requests) == 4
    assert sleeps == [0.3, 1.0, 3.0]

    hs, rec, sleeps = make([json_response(429, {"error": {"code": "HS_RATE_LIMITED", "message": "x"}})], max_retries=0)
    with pytest.raises(RateLimitError):
        hs.apps.list()

    hs, rec, sleeps = make([httpx.ConnectError("x")] * 2, max_retries=1)
    with pytest.raises(NetworkError) as net:
        hs.apps.list()
    assert net.value.status == 0 and net.value.code == "NETWORK"


def test_pagination_iterates_all_pages():
    hs, rec, _ = make(
        [
            json_response(200, {"data": [{"id": "s1"}, {"id": "s2"}], "next_cursor": "c2", "has_more": True}),
            json_response(200, {"data": [{"id": "s3"}], "next_cursor": None, "has_more": False}),
        ]
    )
    ids = [s["id"] for s in hs.segments.list_all(limit=2)]
    assert ids == ["s1", "s2", "s3"]
    assert "cursor" not in rec.requests[0].url.params
    assert rec.requests[1].url.params["cursor"] == "c2"
    assert rec.requests[1].url.params["limit"] == "2"


def test_multipart_import():
    hs, rec, _ = make([json_response(202, {"id": "imp_1"})])
    hs.imports.create("csv_users", ("users.csv", b"external_id\nu1\n", "text/csv"))
    req = rec.requests[0]
    assert req.headers["content-type"].startswith("multipart/form-data; boundary=")
    raw = req.read()
    assert b'name="type"' in raw and b"csv_users" in raw
    assert b'filename="users.csv"' in raw and b"external_id\nu1\n" in raw


def test_identity_hash_matches_node():
    # Node: createHmac('sha256', 'secret').update('user-1').digest('hex')
    assert HeroSignal.identity_hash("secret", "user-1") == "1d16fd7e96e8a9681f283b8a251822ffdc71e2a5bda0c5267a044874fa21b82b"


def test_every_operation_has_a_method():
    from herosignal._generated.resources import RESOURCE_NAMES

    hs = HeroSignal("k", app_id="a")
    for name in RESOURCE_NAMES:
        assert getattr(hs, name) is not None
