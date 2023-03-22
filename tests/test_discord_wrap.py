import pytest

from discordwrap import Auth, errors, post


def test_TokenNotSet():
    with pytest.raises(errors.TokenNotSet):
        post("")


def test_token():
    assert Auth.TOKEN == None
    Auth.TOKEN = "xxxxxxxxxxxx"
    assert Auth.TOKEN != None
