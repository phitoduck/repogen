from enum import Enum


class TeamscreateJsonBodyPrivacy(str, Enum):
    SECRET = "secret"
    CLOSED = "closed"

    def __str__(self) -> str:
        return str(self.value)
