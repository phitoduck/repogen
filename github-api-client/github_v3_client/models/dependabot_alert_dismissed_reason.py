from enum import Enum


class DependabotAlertDismissedReason(str, Enum):
    FIX_STARTED = "fix_started"
    INACCURATE = "inaccurate"
    NO_BANDWIDTH = "no_bandwidth"
    NOT_USED = "not_used"
    TOLERABLE_RISK = "tolerable_risk"

    def __str__(self) -> str:
        return str(self.value)
