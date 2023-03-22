from discordwrap.auth import Auth
from discordwrap.errors import TokenNotSet


def post(endpoint):
    if Auth.TOKEN == None:
        raise TokenNotSet
    baseurl = f"https://discord.com/api/v9{endpoint}"
    headers = {"Authorization": "Bot " + Auth.TOKEN, "Content-Type": "application/json"}
    return
