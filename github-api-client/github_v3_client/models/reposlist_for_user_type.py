from enum import Enum


class ReposlistForUserType(str, Enum):
    ALL = "all"
    OWNER = "owner"
    MEMBER = "member"

    def __str__(self) -> str:
        return str(self.value)
