import pytest

from acornio.asgi import (
    Scope,
    Receive,
    Send,
    ASGIApp,
)


@pytest.fixture
def asgi_app() -> ASGIApp:
    async def app(scope: Scope, receive: Receive, send: Send) -> None:
        await send({
            "type": "http.response.start",
            "status": 200,
            "headers": [],
        })
        await send({
            "type": "http.response.body",
            "body": b"OK",
        })
    return app
