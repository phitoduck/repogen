from enum import Enum


class PackagesgetAllPackageVersionsForPackageOwnedByAuthenticatedUserState(str, Enum):
    ACTIVE = "active"
    DELETED = "deleted"

    def __str__(self) -> str:
        return str(self.value)
