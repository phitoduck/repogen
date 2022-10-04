from enum import Enum


class ReposlistForAuthenticatedUserType(str, Enum):
    ALL = "all"
    OWNER = "owner"
    PUBLIC = "public"
    PRIVATE = "private"
    MEMBER = "member"

    def __str__(self) -> str:
        return str(self.value)
