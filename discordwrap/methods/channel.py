from typing import Union

from discordwrap.Errors import InvlaidBody
from discordwrap.core import get, post


def create_message(channel_id: Union[str, int], json: dict) -> dict:
    if json == None:
        raise InvlaidBody("JSON Body is None")
    if (
        json.get("content") == None
        and json.get("embeds") == None
        and json.get("sticker_ids") == None
        and json.get("components") == None
    ):
        raise InvlaidBody(
            "One of content, embeds, sticker_ids, or components must be set for a message"
        )
    res = post(
        f"/channels/{channel_id}/messages", json=json, bucket=f"channel:{channel_id}"
    )

    return res.json()


def get_channel(channel_id: Union[str, int]) -> dict:
    res = get(f"/channels/{channel_id}", bucket=f"channel:{channel_id}")
    return res.json()
