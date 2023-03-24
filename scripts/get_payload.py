import json
import os
import sys

import dotenv

import discordwrap

dotenv.load_dotenv()

if __name__ == "__main__":
    TOKEN = os.getenv("DISC_TOKEN")
    if TOKEN == None:
        print("Token not found, please set your discord token")
        sys.exit()

    discordwrap.Auth.TOKEN = TOKEN
    path = input("Request url: ")
    method = input("Method: ")
    res = discordwrap.post(path)
    print(res[1])
    with open(f"./tests/responses/{method}.json", "w") as file:
        file.write(json.dumps(res[0], indent=2))
