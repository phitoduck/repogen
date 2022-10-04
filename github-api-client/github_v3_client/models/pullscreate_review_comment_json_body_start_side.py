from enum import Enum


class PullscreateReviewCommentJsonBodyStartSide(str, Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    SIDE = "side"

    def __str__(self) -> str:
        return str(self.value)
