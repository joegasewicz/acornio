import asyncio
from http.client import parse_headers
from io import BytesIO

from acornio.asgi import ASGIApp
from acornio.logger import log, print_preamble
from acornio.exceptions import HTTPVersionUnsupportedError


DEFAULT_HTTP_VERSION = "1.1"


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
        print_preamble()
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
        raw_request = await reader.readuntil(b"\r\n\r\n")
        raw_method, host, raw_headers  = raw_request.split(b"\r\n", 2)


        parsed_headers = parse_headers(BytesIO(raw_headers))

        method, path, version = raw_method.decode().split()

        scope = self._build_scope(
            method=method,
            path=path,
            version=version,
        )

    def _build_scope(
        self,
        *,
        method: str,
        path: str,
        version: str,
    ) -> dict:
        """
        Ref: https://asgi.readthedocs.io/en/stable/specs/www.html#http-connection-scope
        :return:
        """
        try:
            valid_version = self._get_http_version(version="HTTP / 2.0")
        except HTTPVersionUnsupportedError as err:
            valid_version = DEFAULT_HTTP_VERSION
            log.error(f"Error for unsupported HTTP version. Defaulting to {DEFAULT_HTTP_VERSION}", exc_info=True)

        scope = {
            "type": "http",
            "asgi": {
                "version": "3.0",
                "spec_version": "2.0",
            },
            "http_version": valid_version,

        }
        log.debug(f"Scope:\n\t{scope}")
        return scope

    def _get_http_version(self, *, version: str) -> str | None:
        # E.g version = HTTP / 1.1
        version = version.split("/")[1]
        if version == "1.1" or version == "1.0":
            return version
        else:
            raise HTTPVersionUnsupportedError(
                "AcornIO currently only supports HTTP versions <= 1.1"
            )
