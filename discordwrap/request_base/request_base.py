import requests

from discordwrap.auth import Auth
from discordwrap.errors import TokenNotSet


def post(endpoint):
    if Auth.TOKEN == None:
        raise TokenNotSet
    base_url = f"https://discord.com/api/v10{endpoint}"
    headers = {"Authorization": "Bot " + Auth.TOKEN, "Content-Type": "application/json"}
    res = requests.post(base_url, headers=headers, json={"content": "Hello world!"})
    return res.json(), res.status_code
