from unittest import mock

import pytest

from discordwrap import Auth, errors, send_message

from .monkey import mock_request


def test_TokenNotSet():
    with pytest.raises(errors.TokenNotSet):
        message = "Hello world, from discordwrap!"
        send_message(1065325022723440700, message)


def test_token():
    assert Auth.TOKEN == None
    Auth.TOKEN = "xxxxxxxxxxxx"
    assert Auth.TOKEN != None


@mock.patch("requests.post", side_effect=mock_request)
def test_create_message(mock_request):
    message = "Hello world, from discordwrap!"
    res = send_message(1065325022723440700, message)
    assert res != None
    assert res["type"] == 0
    assert res["content"] == message
