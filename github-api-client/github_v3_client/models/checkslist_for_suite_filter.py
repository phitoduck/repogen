from enum import Enum


class CheckslistForSuiteFilter(str, Enum):
    LATEST = "latest"
    ALL = "all"

    def __str__(self) -> str:
        return str(self.value)
