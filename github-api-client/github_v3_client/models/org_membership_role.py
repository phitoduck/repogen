from enum import Enum


class OrgMembershipRole(str, Enum):
    ADMIN = "admin"
    MEMBER = "member"
    BILLING_MANAGER = "billing_manager"

    def __str__(self) -> str:
        return str(self.value)
