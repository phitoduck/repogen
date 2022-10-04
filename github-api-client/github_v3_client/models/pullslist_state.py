from enum import Enum


class PullslistState(str, Enum):
    OPEN = "open"
    CLOSED = "closed"
    ALL = "all"

    def __str__(self) -> str:
        return str(self.value)
