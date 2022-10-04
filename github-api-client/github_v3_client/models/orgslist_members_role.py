from enum import Enum


class OrgslistMembersRole(str, Enum):
    ALL = "all"
    ADMIN = "admin"
    MEMBER = "member"

    def __str__(self) -> str:
        return str(self.value)
