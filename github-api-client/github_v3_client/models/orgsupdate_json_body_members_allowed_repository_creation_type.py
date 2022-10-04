from enum import Enum


class OrgsupdateJsonBodyMembersAllowedRepositoryCreationType(str, Enum):
    ALL = "all"
    PRIVATE = "private"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
