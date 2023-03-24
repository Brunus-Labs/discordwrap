import requests

from discordwrap.Errors import TokenNotSet
from discordwrap.auth import Auth


def post(endpoint, json=None):
    if Auth.TOKEN == None:
        raise TokenNotSet
    base_url = f"https://discord.com/api/v10{endpoint}"
    headers = {"Authorization": "Bot " + Auth.TOKEN, "Content-Type": "application/json"}
    res = requests.post(base_url, headers=headers, json=json)
    return res.json()
