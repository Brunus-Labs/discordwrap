from discordwrap import __version__, hello


def test_version():
    assert __version__ == "0.2.0"


def test_hello():
    assert hello() == "world"
