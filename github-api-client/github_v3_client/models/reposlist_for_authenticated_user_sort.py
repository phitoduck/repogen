from enum import Enum


class ReposlistForAuthenticatedUserSort(str, Enum):
    CREATED = "created"
    UPDATED = "updated"
    PUSHED = "pushed"
    FULL_NAME = "full_name"

    def __str__(self) -> str:
        return str(self.value)
