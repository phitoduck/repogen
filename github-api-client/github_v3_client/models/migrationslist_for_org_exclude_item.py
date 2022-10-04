from enum import Enum


class MigrationslistForOrgExcludeItem(str, Enum):
    REPOSITORIES = "repositories"

    def __str__(self) -> str:
        return str(self.value)
