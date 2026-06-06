import asyncio

from acornio.asgi import ASGIApp
from acornio.logger import log


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
        log.info(f"Starting server on http://{self.host}:{self.port}")
        async  with server:
            await server.serve_forever()

    async def handle_connection(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
        """
        # parse HTTP bytes into method/path/headers/body
        # build ASGI scope
        # define receive()
        # define send()
        # await self.application(scope, receive, send)
        # write HTTP response back with writer.write(...)
        # close the connection

        it does not return the ASGI scope, it builds it and passes it to self.application(scope, receive, send)

        app response through send -
            {
                "type": "http.response.start",
                "status": 200,
                "headers": [(b"content-type", b"text/plain")],
            }
        """
        read_bytes = await reader.readuntil(b"\r\n\r\n")
        log.info(f"here -----------> {read_bytes}")