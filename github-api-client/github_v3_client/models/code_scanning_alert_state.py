from enum import Enum


class CodeScanningAlertState(str, Enum):
    OPEN = "open"
    CLOSED = "closed"
    DISMISSED = "dismissed"
    FIXED = "fixed"

    def __str__(self) -> str:
        return str(self.value)
