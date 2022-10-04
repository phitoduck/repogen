from enum import Enum


class SecretScanninglistAlertsForOrgState(str, Enum):
    OPEN = "open"
    RESOLVED = "resolved"

    def __str__(self) -> str:
        return str(self.value)
