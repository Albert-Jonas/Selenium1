from Joke import len_joke
from unittest import mock


@mock.patch("Joke.get_joke", return_value="almafa")
def test_len_joke(mock_get_joke):
    assert len_joke() == 6


