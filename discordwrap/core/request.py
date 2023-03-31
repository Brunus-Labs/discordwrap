import asyncio
import datetime
from types import TracebackType
from typing import Optional, Union

import requests

from discordwrap.Auth import Auth
from discordwrap.Errors import *


class Locks(object):
    # Singleton lock Object
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Locks, cls).__new__(cls)
            cls._locks = {}
            cls._loop = asyncio.new_event_loop()
            asyncio.set_event_loop(cls._loop)
            cls._global_over = asyncio.Event()
            cls._global_over.set()
        return cls.instance


class MaybeUnlock:
    # Shoutout to nextcord for this chunk
    def __init__(self, lock: asyncio.Lock) -> None:
        self.lock: asyncio.Lock = lock
        self._unlock: bool = True

    def __enter__(self):
        return self

    def defer(self) -> None:
        self._unlock = False

    def __exit__(
        self,
        exc_type,
        exc,
        traceback: Optional[TracebackType],
    ) -> None:
        if self._unlock:
            self.lock.release()


def syncwrap(func):
    def inner(*args, **kwargs):
        loop = Locks()._loop
        return loop.run_until_complete(func(*args, **kwargs))

    return inner


def handle_rate_limit(func):
    async def innter(*args, **kwargs):
        locks = Locks()
        _locks = locks._locks
        _global_over = locks._global_over

        if Auth.TOKEN == None:
            raise TokenNotSet

        bucket = kwargs.get("bucket", "_")
        lock = _locks.get(bucket)
        if lock is None:
            lock = asyncio.Lock()
            if bucket != "_":
                _locks[bucket] = lock

        if not _global_over.is_set():
            # wait until the global lock is complete
            await _global_over.wait()

        await lock.acquire()
        with MaybeUnlock(lock) as maybe_lock:
            for tries in range(5):
                try:
                    res = func(*args, **kwargs)

                    is_global = bool(res.headers.get("X-RateLimit-Global", False))
                    remaining = res.headers.get("X-Ratelimit-Remaining", "")
                    data = res.text
                    try:
                        if res.headers["content-type"] == "application/json":
                            data = res.json()
                    except KeyError:
                        # Thanks Cloudflare
                        pass
                    if remaining == "0" and res.status_code != 429:
                        # we've depleted our current bucket
                        utc = datetime.timezone.utc
                        now = datetime.datetime.now(utc)
                        reset = datetime.datetime.fromtimestamp(
                            float(res.headers["X-Ratelimit-Reset"]), utc
                        )
                        delta = (reset - now).total_seconds()
                        maybe_lock.defer()
                        locks._loop.call_later(delta, lock.release)

                    # the request was successful so just return the text/json
                    if 300 > res.status_code >= 200:
                        return res

                    # we are being rate limited
                    if res.status_code == 429:
                        if not res.headers.get("Via") or isinstance(data, str):
                            # Banned by Cloudflare more than likely.
                            raise HTTPException(res, data)

                        # sleep a bit
                        retry_after: float = data["retry_after"]

                        # check if it's a global rate limit
                        if is_global:
                            _global_over.clear()

                        await asyncio.sleep(retry_after)

                        # release the global lock now that the
                        # global rate limit has passed
                        if is_global:
                            _global_over.set()

                        continue

                    # we've received a 500, 502, or 504, unconditional retry
                    if res.status_code in {500, 502, 504}:
                        await asyncio.sleep(1 + tries * 2)
                        continue

                    # the usual error cases
                    if res.status_code == 403:
                        raise Forbidden(res, data, res.url)
                    elif res.status_code == 404:
                        raise NotFound(res, data, res.url)
                    elif res.status_code >= 500:
                        raise DiscordServerError(res, data, res.url)
                    else:
                        raise HTTPException(res, data, res.url)
                # This is handling exceptions from the request
                except OSError as e:
                    # Connection reset by peer
                    if tries < 4 and e.errno in (54, 10054):
                        await asyncio.sleep(1 + tries * 2)
                        continue
                    raise

    return innter


@syncwrap
@handle_rate_limit
def post(endpoint, json=None, bucket="_", **kwargs):
    base_url = f"https://discord.com/api/v10{endpoint}"
    headers = {
        "Authorization": f"Bot {Auth.TOKEN}",
        "Content-Type": "application/json",
    }
    res = requests.post(base_url, headers=headers, json=json, **kwargs)
    return res


@syncwrap
@handle_rate_limit
def get(endpoint, bucket="_", **kwargs):
    base_url = f"https://discord.com/api/v10{endpoint}"
    headers = {
        "Authorization": f"Bot {Auth.TOKEN}",
        "Content-Type": "application/json",
    }
    res = requests.get(base_url, headers=headers, **kwargs)
    return res
