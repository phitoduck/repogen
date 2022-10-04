from enum import Enum


class DependabotlistAlertsForRepoScope(str, Enum):
    DEVELOPMENT = "development"
    RUNTIME = "runtime"

    def __str__(self) -> str:
        return str(self.value)
