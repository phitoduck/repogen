from enum import Enum


class ProjectOrganizationPermission(str, Enum):
    READ = "read"
    WRITE = "write"
    ADMIN = "admin"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
