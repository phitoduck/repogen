from enum import Enum


class TeamsaddOrUpdateMembershipForUserInOrgJsonBodyRole(str, Enum):
    MEMBER = "member"
    MAINTAINER = "maintainer"

    def __str__(self) -> str:
        return str(self.value)
