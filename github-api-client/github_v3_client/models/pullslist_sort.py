from enum import Enum


class PullslistSort(str, Enum):
    CREATED = "created"
    UPDATED = "updated"
    POPULARITY = "popularity"
    LONG_RUNNING = "long-running"

    def __str__(self) -> str:
        return str(self.value)
