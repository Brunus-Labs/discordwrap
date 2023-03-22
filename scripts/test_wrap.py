import json
import os

import dotenv

import discordwrap as dw

dotenv.load_dotenv()

if __name__ == "__main__":
    dw.Auth.TOKEN = os.getenv("DISC_TOKEN")
    message = "Hello world, from discordwrap!"
    res = dw.send_message(1065325022723440700, message)
    print(json.dumps(res, indent=4))
