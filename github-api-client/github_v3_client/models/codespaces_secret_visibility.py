from enum import Enum


class CodespacesSecretVisibility(str, Enum):
    ALL = "all"
    PRIVATE = "private"
    SELECTED = "selected"

    def __str__(self) -> str:
        return str(self.value)
