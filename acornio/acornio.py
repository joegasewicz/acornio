from acornio.asgi import ASGIApp


class AcornIO:

    def __init__(
            self,
            application: ASGIApp,
            *,
            host: str = "localhost",
            port: int = 8888,
    ):
        self.application = application
        self.host = host
        self.port = port
