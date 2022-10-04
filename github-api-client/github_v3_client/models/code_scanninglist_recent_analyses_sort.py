from enum import Enum


class CodeScanninglistRecentAnalysesSort(str, Enum):
    CREATED = "created"

    def __str__(self) -> str:
        return str(self.value)
