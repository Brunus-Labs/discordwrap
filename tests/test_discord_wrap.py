from discordwrap import __version__, hello


def test_hello():
    assert hello() == "world!"
