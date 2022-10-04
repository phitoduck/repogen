from enum import Enum


class IssuesupdateJsonBodyStateReason(str, Enum):
    COMPLETED = "completed"
    NOT_PLANNED = "not_planned"
    REOPENED = "reopened"

    def __str__(self) -> str:
        return str(self.value)
