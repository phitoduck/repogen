from enum import Enum


class TeamsupdateLegacyJsonBodyPrivacy(str, Enum):
    SECRET = "secret"
    CLOSED = "closed"

    def __str__(self) -> str:
        return str(self.value)
