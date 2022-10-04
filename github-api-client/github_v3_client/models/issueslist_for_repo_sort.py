from enum import Enum


class IssueslistForRepoSort(str, Enum):
    CREATED = "created"
    UPDATED = "updated"
    COMMENTS = "comments"

    def __str__(self) -> str:
        return str(self.value)
