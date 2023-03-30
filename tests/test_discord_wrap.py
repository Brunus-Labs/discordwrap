from unittest import mock

import pytest

from discordwrap import Auth, Errors, create_message

from .monkey import mock_request


def test_token(token):
    assert Auth.TOKEN != None


@mock.patch("requests.post", side_effect=mock_request)
def test_TokenNotSet(mock_request):
    with pytest.raises(Errors.TokenNotSet):
        message = "Hello world!"
        create_message(1065325022723440700, json={"content": message})


@mock.patch("requests.post", side_effect=mock_request)
def test_InvalidBody(mock_request, token):
    with pytest.raises(Errors.InvlaidBody):
        create_message(1065325022723440700, json=None)
    with pytest.raises(Errors.InvlaidBody):
        create_message(1065325022723440700, json={"key": "value"})


@mock.patch("requests.post", side_effect=mock_request)
def test_create_message(mock_request, token):
    message = "Hello world!"
    res = create_message(1065325022723440700, json={"content": message})
    assert res != None
    assert res["type"] == 0
    assert res["content"] == message
