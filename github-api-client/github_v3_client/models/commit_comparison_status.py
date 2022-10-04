from enum import Enum


class CommitComparisonStatus(str, Enum):
    DIVERGED = "diverged"
    AHEAD = "ahead"
    BEHIND = "behind"
    IDENTICAL = "identical"

    def __str__(self) -> str:
        return str(self.value)
