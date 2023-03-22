from discordwrap.request_base import post


def send_message(channel_id, message):
    return post(f"/channels/{channel_id}/messages", json={"content": message})
