from enum import Enum


class CodeScanningSarifsStatusProcessingStatus(str, Enum):
    PENDING = "pending"
    COMPLETE = "complete"
    FAILED = "failed"

    def __str__(self) -> str:
        return str(self.value)
