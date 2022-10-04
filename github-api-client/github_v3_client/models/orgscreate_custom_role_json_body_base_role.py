from enum import Enum


class OrgscreateCustomRoleJsonBodyBaseRole(str, Enum):
    READ = "read"
    TRIAGE = "triage"
    WRITE = "write"
    MAINTAIN = "maintain"

    def __str__(self) -> str:
        return str(self.value)
