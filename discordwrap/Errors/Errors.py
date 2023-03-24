class TokenNotSet(Exception):
    pass


class InvlaidBody(Exception):
    def __init__(self, reason):
        super().__init__(reason)
