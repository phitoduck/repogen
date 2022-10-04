from enum import Enum


class PullssubmitReviewJsonBodyEvent(str, Enum):
    APPROVE = "APPROVE"
    REQUEST_CHANGES = "REQUEST_CHANGES"
    COMMENT = "COMMENT"

    def __str__(self) -> str:
        return str(self.value)
