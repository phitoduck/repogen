from enum import Enum


class TeamsaddOrUpdateProjectPermissionsLegacyJsonBodyPermission(str, Enum):
    READ = "read"
    WRITE = "write"
    ADMIN = "admin"

    def __str__(self) -> str:
        return str(self.value)
