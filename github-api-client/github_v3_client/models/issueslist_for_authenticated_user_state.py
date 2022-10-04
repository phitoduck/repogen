from enum import Enum


class IssueslistForAuthenticatedUserState(str, Enum):
    OPEN = "open"
    CLOSED = "closed"
    ALL = "all"

    def __str__(self) -> str:
        return str(self.value)
