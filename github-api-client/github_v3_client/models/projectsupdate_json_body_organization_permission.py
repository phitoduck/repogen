from enum import Enum


class ProjectsupdateJsonBodyOrganizationPermission(str, Enum):
    READ = "read"
    WRITE = "write"
    ADMIN = "admin"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
