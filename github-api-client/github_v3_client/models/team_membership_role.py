from enum import Enum


class TeamMembershipRole(str, Enum):
    MEMBER = "member"
    MAINTAINER = "maintainer"

    def __str__(self) -> str:
        return str(self.value)
