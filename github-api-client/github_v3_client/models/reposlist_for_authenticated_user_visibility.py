from enum import Enum


class ReposlistForAuthenticatedUserVisibility(str, Enum):
    ALL = "all"
    PUBLIC = "public"
    PRIVATE = "private"

    def __str__(self) -> str:
        return str(self.value)
