from enum import Enum


class OrgssetMembershipForUserJsonBodyRole(str, Enum):
    ADMIN = "admin"
    MEMBER = "member"

    def __str__(self) -> str:
        return str(self.value)
