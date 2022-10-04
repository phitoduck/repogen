from enum import Enum


class ReposgetClonesPer(str, Enum):
    VALUE_0 = ""
    DAY = "day"
    WEEK = "week"

    def __str__(self) -> str:
        return str(self.value)
