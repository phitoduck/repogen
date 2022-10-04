from enum import Enum


class TeamscreateJsonBodyPermission(str, Enum):
    PULL = "pull"
    PUSH = "push"

    def __str__(self) -> str:
        return str(self.value)
