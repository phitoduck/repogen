from enum import Enum


class OrgscreateInvitationJsonBodyRole(str, Enum):
    ADMIN = "admin"
    DIRECT_MEMBER = "direct_member"
    BILLING_MANAGER = "billing_manager"

    def __str__(self) -> str:
        return str(self.value)
