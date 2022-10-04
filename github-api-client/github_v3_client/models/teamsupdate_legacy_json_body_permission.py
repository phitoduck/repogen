from enum import Enum


class TeamsupdateLegacyJsonBodyPermission(str, Enum):
    PULL = "pull"
    PUSH = "push"
    ADMIN = "admin"

    def __str__(self) -> str:
        return str(self.value)
