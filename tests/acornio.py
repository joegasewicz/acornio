from acornio.acornio import AcornIO


class TestAcornIO:

    def test_acornio_instance(self, asgi_app):

        acorn = AcornIO(asgi_app)
        assert isinstance(acorn, AcornIO)
