class TokenNotSet(Exception):
    pass


class InvlaidBody(Exception):
    def __init__(self, reason):
        super().__init__(reason)


class HTTPException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Forbidden(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class NotFound(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class DiscordServerError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
