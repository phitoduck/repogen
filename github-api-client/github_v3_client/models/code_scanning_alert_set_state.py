from enum import Enum


class CodeScanningAlertSetState(str, Enum):
    OPEN = "open"
    DISMISSED = "dismissed"

    def __str__(self) -> str:
        return str(self.value)
