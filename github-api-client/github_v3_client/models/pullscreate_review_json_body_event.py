from enum import Enum


class PullscreateReviewJsonBodyEvent(str, Enum):
    APPROVE = "APPROVE"
    REQUEST_CHANGES = "REQUEST_CHANGES"
    COMMENT = "COMMENT"

    def __str__(self) -> str:
        return str(self.value)
