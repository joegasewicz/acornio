import asyncio

from acornio.asgi import ASGIApp


class AcornIO:

    def __init__(
            self,
            application: ASGIApp,
            *,
            host: str = "localhost",
            port: int = 8000,
    ):
        self.application = application
        self.host = host
        self.port = port

    async def serve(self) -> None:
        server = await asyncio.start_server(
            self.handle_connection,
            self.host,
            self.port,
        )

        async  with server:
            await server.serve_forever()

    async def handle_connection(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
        raw_request = await reader.read(65536)


    async def parse_request(self, raw_request: bytes) -> tuple[str, str, list[tuple[bytes, bytes]]]:
        head = raw_request.split(b"\r\n\r\n", 1)[0]

    async def build_response(
        self,
        status: int,
        headers: list[tuple[bytes, bytes]],
        body: bytes,
    ) -> bytes:
        reason = {
            "200":
        }
