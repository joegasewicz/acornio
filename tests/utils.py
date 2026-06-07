from acornio.utils import get_raw_path


def test_get_raw_path():
    mock_path = "/articles/You%20%26%20Me/1/2/3?cookies=true"
    result = get_raw_path(mock_path)
    expected = b"/articles/You%20%26%20Me/1/2/3"
    assert result == expected

