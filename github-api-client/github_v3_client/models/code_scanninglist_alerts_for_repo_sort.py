from enum import Enum


class CodeScanninglistAlertsForRepoSort(str, Enum):
    CREATED = "created"
    UPDATED = "updated"

    def __str__(self) -> str:
        return str(self.value)
