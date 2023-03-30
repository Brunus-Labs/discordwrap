# DiscordWrap
A simple, intuitve wrapper around the underbelly of the discord API.
This library is meant to be used with the discord docs. Responses from methods in the library will return
JSON just as discords api details.

## Example
```py
from discordwrap import Auth, channel
Auth.TOKEN = 'your token'

# your channel
channel = 111111111111111
channel.create_message(channel, json={
    'content': 'Hello world!'
})
```
