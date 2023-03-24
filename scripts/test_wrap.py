import asyncio
import json
import os

import dotenv

import discordwrap as dw

dotenv.load_dotenv()


def test_live():
    dw.Auth.TOKEN = os.getenv("DISC_TOKEN")
    for i in range(10):
        dw.create_message(1065325022723440700, json={"content": f"Message {i}"})


if __name__ == "__main__":
    test_live()
