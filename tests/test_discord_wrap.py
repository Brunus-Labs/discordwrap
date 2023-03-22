from discordwrap import auth

auth.TOKEN = "xxxxxxxxxxxx"


def test_token():
    assert auth.TOKEN != None
