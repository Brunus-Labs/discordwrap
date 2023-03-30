import json
import os
import sys

import dotenv

import discordwrap

dotenv.load_dotenv()


def surround(color: str, *args) -> str:
    msg = ""
    for arg in args:
        msg += str(arg)
    return color + msg + "\033[0m"


if __name__ == "__main__":
    TOKEN = os.getenv("DISC_TOKEN")
    if TOKEN == None:
        print("Token not found, please set your discord token")
        sys.exit()

    discordwrap.Auth.TOKEN = TOKEN
    path = input(
        "Request Url: " + surround("\033[90m", "https://discord.com/api/v10")
    ).lower()
    request_type = input(
        "Request Method " + surround("\033[90m", "(POST)") + ": "
    ).upper()
    method = input("Method Name: ")
    if method == "POST":
        input(
            "Make sure that the body json is in "
            + surround("\u001b[34m", "body.json")
            + "\n"
        )

    while len(path) == 0:
        print("Requires request path")
        path = input(
            "Request url: " + surround("\033[90m", "https://discord.com/api/v10")
        )
    while len(method) == 0:
        print("Requires method name")
        method = input("Method: ")

    res = {}

    if request_type == "POST":
        res = discordwrap.core.post(path)
    if request_type == "GET":
        res = discordwrap.core.get(path)

    print(res)
    with open(f"./tests/responses/{method}.json", "w") as file:
        file.write(json.dumps(res, indent=2))
