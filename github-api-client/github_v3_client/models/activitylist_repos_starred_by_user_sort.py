from enum import Enum


class ActivitylistReposStarredByUserSort(str, Enum):
    CREATED = "created"
    UPDATED = "updated"

    def __str__(self) -> str:
        return str(self.value)
