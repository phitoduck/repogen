from enum import Enum


class SearchreposSort(str, Enum):
    STARS = "stars"
    FORKS = "forks"
    HELP_WANTED_ISSUES = "help-wanted-issues"
    UPDATED = "updated"

    def __str__(self) -> str:
        return str(self.value)
