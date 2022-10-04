from enum import Enum


class DependencyScope(str, Enum):
    RUNTIME = "runtime"
    DEVELOPMENT = "development"

    def __str__(self) -> str:
        return str(self.value)
