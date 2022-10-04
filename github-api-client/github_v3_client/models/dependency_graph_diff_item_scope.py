from enum import Enum


class DependencyGraphDiffItemScope(str, Enum):
    UNKNOWN = "unknown"
    RUNTIME = "runtime"
    DEVELOPMENT = "development"

    def __str__(self) -> str:
        return str(self.value)
