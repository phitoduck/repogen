from enum import Enum


class IssueslistMilestonesSort(str, Enum):
    DUE_ON = "due_on"
    COMPLETENESS = "completeness"

    def __str__(self) -> str:
        return str(self.value)
