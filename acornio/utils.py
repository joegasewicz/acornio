from urllib.parse import urlsplit


def get_raw_path(*, path: str) -> bytes:
    """
    Returns excluding any query string, with percent-encoded
    sequences and UTF-8 byte sequences decoded into characters
    :param path:
    :return: HTTP request taget as bytes
    """
    parts = urlsplit(path)
    return parts.path.encode("ascii")
