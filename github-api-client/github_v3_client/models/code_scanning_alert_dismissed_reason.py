from enum import Enum


class CodeScanningAlertDismissedReason(str, Enum):
    FALSE_POSITIVE = "false positive"
    WONT_FIX = "won't fix"
    USED_IN_TESTS = "used in tests"

    def __str__(self) -> str:
        return str(self.value)
