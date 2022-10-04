from enum import Enum


class SearchusersSort(str, Enum):
    FOLLOWERS = "followers"
    REPOSITORIES = "repositories"
    JOINED = "joined"

    def __str__(self) -> str:
        return str(self.value)
