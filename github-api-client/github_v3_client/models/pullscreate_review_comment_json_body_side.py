from enum import Enum


class PullscreateReviewCommentJsonBodySide(str, Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"

    def __str__(self) -> str:
        return str(self.value)
