from enum import Enum


class UserssetPrimaryEmailVisibilityForAuthenticatedUserJsonBodyVisibility(str, Enum):
    PUBLIC = "public"
    PRIVATE = "private"

    def __str__(self) -> str:
        return str(self.value)
