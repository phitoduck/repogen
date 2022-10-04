from enum import Enum


class SecretScanningAlertResolution(str, Enum):
    FALSE_POSITIVE = "false_positive"
    WONT_FIX = "wont_fix"
    REVOKED = "revoked"
    USED_IN_TESTS = "used_in_tests"

    def __str__(self) -> str:
        return str(self.value)
