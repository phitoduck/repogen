from enum import Enum


class PullslistReviewCommentsForRepoSort(str, Enum):
    CREATED = "created"
    UPDATED = "updated"
    CREATED_AT = "created_at"

    def __str__(self) -> str:
        return str(self.value)
