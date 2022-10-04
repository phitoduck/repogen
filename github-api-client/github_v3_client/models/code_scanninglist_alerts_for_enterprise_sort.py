from enum import Enum


class CodeScanninglistAlertsForEnterpriseSort(str, Enum):
    CREATED = "created"
    UPDATED = "updated"

    def __str__(self) -> str:
        return str(self.value)
