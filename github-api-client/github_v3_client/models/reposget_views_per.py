from enum import Enum


class ReposgetViewsPer(str, Enum):
    VALUE_0 = ""
    DAY = "day"
    WEEK = "week"

    def __str__(self) -> str:
        return str(self.value)
