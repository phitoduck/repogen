from enum import Enum


class AllowedActions(str, Enum):
    ALL = "all"
    LOCAL_ONLY = "local_only"
    SELECTED = "selected"

    def __str__(self) -> str:
        return str(self.value)
