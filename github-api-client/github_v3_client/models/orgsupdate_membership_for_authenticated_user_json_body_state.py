from enum import Enum


class OrgsupdateMembershipForAuthenticatedUserJsonBodyState(str, Enum):
    ACTIVE = "active"

    def __str__(self) -> str:
        return str(self.value)
