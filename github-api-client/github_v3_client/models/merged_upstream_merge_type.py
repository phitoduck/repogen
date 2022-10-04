from enum import Enum


class MergedUpstreamMergeType(str, Enum):
    MERGE = "merge"
    FAST_FORWARD = "fast-forward"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
