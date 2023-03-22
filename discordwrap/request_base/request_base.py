import requests

from discordwrap.auth import Auth
from discordwrap.errors import TokenNotSet


def post(endpoint):
    if Auth.TOKEN == None:
        raise TokenNotSet
    base_url = f"https://discord.com/api/v9{endpoint}"
    headers = {"Authorization": "Bot " + Auth.TOKEN, "Content-Type": "application/json"}
    res = requests.post(base_url, headers=headers)
    return res.json(), res.status_code
