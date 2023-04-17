# DiscordWrap
A simple, intuitive wrapper around the underbelly of the discord API.
This library is meant to be used with the discord docs. Responses from methods in the library will return
JSON just as discords api details.

# Installation
```sh
pip install discordwrap
```

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

## Docs

Find offical docs [here](https://discordwrap.brunuslabs.com)!

## Motivation
Using any API can be daunting. Using a library with poor documentation can be even worse. 
The goal of this library is to not need any documentation, other than discords.
This is why users are encouraged to use raw json for bodies, and responses of requests.

So what does this library do? The most daunting part. The rate limiting, and overall python
function creation, and async handling. Requests under the hood are asynchronous, however to the end
user of the library, they are not. This lets consumers freely use our library without needing to
worry about buckets, rate limits, or any other messy details, and focus on building their product.

Rate limiting blocks only when needed, and makes sure to only keep one thread alive. There is no class instantiation needed once the
Auth token is set.

This library does NOT (yet) implement the discord gateway, as there are plenty of other libraries that are much better for bot building.
This library is targeted at developers that are not building an interactive bot, but need the ability to use the discord api in another project.

## Use cases

- Ping a discord server when a script is done running
- Get information about a discord channel for integration with another service
- More to come!

