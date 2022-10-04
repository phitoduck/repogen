from enum import Enum


class CodespaceMachinePrebuildAvailability(str, Enum):
    NONE = "none"
    READY = "ready"
    IN_PROGRESS = "in_progress"

    def __str__(self) -> str:
        return str(self.value)
