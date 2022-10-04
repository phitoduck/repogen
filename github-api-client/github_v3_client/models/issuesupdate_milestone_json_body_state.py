from enum import Enum


class IssuesupdateMilestoneJsonBodyState(str, Enum):
    OPEN = "open"
    CLOSED = "closed"

    def __str__(self) -> str:
        return str(self.value)
