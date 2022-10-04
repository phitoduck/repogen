from enum import Enum


class MigrationsstartForAuthenticatedUserJsonBodyExcludeItem(str, Enum):
    REPOSITORIES = "repositories"

    def __str__(self) -> str:
        return str(self.value)
