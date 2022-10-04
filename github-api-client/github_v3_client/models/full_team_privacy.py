from enum import Enum


class FullTeamPrivacy(str, Enum):
    CLOSED = "closed"
    SECRET = "secret"

    def __str__(self) -> str:
        return str(self.value)
