from enum import Enum


class SearchcommitsSort(str, Enum):
    AUTHOR_DATE = "author-date"
    COMMITTER_DATE = "committer-date"

    def __str__(self) -> str:
        return str(self.value)
