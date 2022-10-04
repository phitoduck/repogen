from enum import Enum


class PullslistReviewCommentsSort(str, Enum):
    CREATED = "created"
    UPDATED = "updated"

    def __str__(self) -> str:
        return str(self.value)
