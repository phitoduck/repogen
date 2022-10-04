from enum import Enum


class DependabotupdateAlertJsonBodyState(str, Enum):
    DISMISSED = "dismissed"
    OPEN = "open"

    def __str__(self) -> str:
        return str(self.value)
