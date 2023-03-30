import os

from dotenv import load_dotenv
import pytest

from discordwrap import Auth


@pytest.fixture(scope="function")
def token():
    load_dotenv()
    Auth.TOKEN = os.getenv("DISC_TOKEN")
    yield
    Auth.TOKEN = None
