from unittest import mock

import pytest

from discordwrap import Auth, errors, post

from .monkey import mock_request


def test_TokenNotSet():
    with pytest.raises(errors.TokenNotSet):
        post("")


def test_token():
    assert Auth.TOKEN == None
    Auth.TOKEN = "xxxxxxxxxxxx"
    assert Auth.TOKEN != None


@mock.patch("requests.post", side_effect=mock_request)
def test_create_message(mock_request):
    assert post("/404") == (None, 404)
