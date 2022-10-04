from enum import Enum


class PackagesgetAllPackageVersionsForPackageOwnedByOrgState(str, Enum):
    ACTIVE = "active"
    DELETED = "deleted"

    def __str__(self) -> str:
        return str(self.value)
