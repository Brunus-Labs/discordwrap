import json
import os

import dotenv

import discordwrap

dotenv.load_dotenv()

if __name__ == "__main__":
    discordwrap.Auth.TOKEN = os.getenv("DISC_TOKEN")
    res = discordwrap.post("/channels/1065325022723440700/messages")
    print(res[1])
    with open("payload.json", "w") as file:
        file.write(json.dumps(res[0], indent=4))
