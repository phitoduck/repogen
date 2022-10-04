from enum import Enum


class TeamsaddOrUpdateRepoPermissionsLegacyJsonBodyPermission(str, Enum):
    PULL = "pull"
    PUSH = "push"
    ADMIN = "admin"

    def __str__(self) -> str:
        return str(self.value)
