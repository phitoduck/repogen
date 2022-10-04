from enum import Enum


class TeamslistMembersLegacyRole(str, Enum):
    MEMBER = "member"
    MAINTAINER = "maintainer"
    ALL = "all"

    def __str__(self) -> str:
        return str(self.value)
