import os

import dotenv

from discordwrap import Auth, channel

dotenv.load_dotenv()


def test_live():
    Auth.TOKEN = os.getenv("DISC_TOKEN")
    for i in range(10):
        channel.create_message(1065325022723440700, json={"content": f"Message {i}"})


if __name__ == "__main__":
    test_live()
