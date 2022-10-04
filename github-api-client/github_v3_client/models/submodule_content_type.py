from enum import Enum


class SubmoduleContentType(str, Enum):
    SUBMODULE = "submodule"

    def __str__(self) -> str:
        return str(self.value)
