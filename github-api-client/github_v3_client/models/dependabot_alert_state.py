from enum import Enum


class DependabotAlertState(str, Enum):
    DISMISSED = "dismissed"
    FIXED = "fixed"
    OPEN = "open"

    def __str__(self) -> str:
        return str(self.value)
