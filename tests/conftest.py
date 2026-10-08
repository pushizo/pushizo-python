"""Ortak test yardımcıları: sahte HTTP transport'u ve kayıtlı istekler."""

import json
from typing import Any, Callable, List, Union

import httpx
import pytest

from herosignal import HeroSignal

Responder = Union[httpx.Response, Exception, Callable[[httpx.Request], httpx.Response]]


class FakeServer:
    """Sıradaki yanıtları dönen ve gelen istekleri kaydeden ``httpx.MockTransport`` sarmalayıcısı."""

    def __init__(self) -> None:
        self.requests: List[httpx.Request] = []
        self.responses: List[Responder] = []
        self.sleeps: List[float] = []

    def queue(self, *responses: Responder) -> None:
        self.responses.extend(responses)

    def handler(self, request: httpx.Request) -> httpx.Response:
        request.read()
        self.requests.append(request)
        if not self.responses:
            raise AssertionError(f"beklenmeyen istek: {request.method} {request.url}")
        nxt = self.responses.pop(0)
        if isinstance(nxt, Exception):
            raise nxt
        if isinstance(nxt, httpx.Response):
            return nxt
        return nxt(request)

    def client(self, **kwargs: Any) -> HeroSignal:
        opts = {"api_key": "hs_live_test", "app_id": "app_default", "base_url": "https://api.test"}
        opts.update(kwargs)
        return HeroSignal(
            http_client=httpx.Client(transport=httpx.MockTransport(self.handler)),
            sleep=self.sleeps.append,
            **opts,
        )


def json_response(status: int, body: Any, headers: Any = None) -> httpx.Response:
    return httpx.Response(
        status,
        content=json.dumps(body).encode("utf-8"),
        headers={"content-type": "application/json", **(headers or {})},
    )


@pytest.fixture
def server() -> FakeServer:
    return FakeServer()
