from enum import Enum


class PullsmergeJsonBodyMergeMethod(str, Enum):
    MERGE = "merge"
    SQUASH = "squash"
    REBASE = "rebase"

    def __str__(self) -> str:
        return str(self.value)
