from enum import Enum


class ReposlistForksSort(str, Enum):
    NEWEST = "newest"
    OLDEST = "oldest"
    STARGAZERS = "stargazers"
    WATCHERS = "watchers"

    def __str__(self) -> str:
        return str(self.value)
