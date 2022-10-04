from enum import Enum


class SearchcodeSort(str, Enum):
    INDEXED = "indexed"

    def __str__(self) -> str:
        return str(self.value)
