from enum import Enum


class PullsdismissReviewJsonBodyEvent(str, Enum):
    DISMISS = "DISMISS"

    def __str__(self) -> str:
        return str(self.value)
