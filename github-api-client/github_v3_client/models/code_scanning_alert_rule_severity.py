from enum import Enum


class CodeScanningAlertRuleSeverity(str, Enum):
    NONE = "none"
    NOTE = "note"
    WARNING = "warning"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)
