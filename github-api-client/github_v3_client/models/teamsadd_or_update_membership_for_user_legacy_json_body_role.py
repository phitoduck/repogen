from enum import Enum


class TeamsaddOrUpdateMembershipForUserLegacyJsonBodyRole(str, Enum):
    MEMBER = "member"
    MAINTAINER = "maintainer"

    def __str__(self) -> str:
        return str(self.value)
