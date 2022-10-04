from enum import Enum


class DependabotlistAlertsForRepoSort(str, Enum):
    CREATED = "created"
    UPDATED = "updated"

    def __str__(self) -> str:
        return str(self.value)
