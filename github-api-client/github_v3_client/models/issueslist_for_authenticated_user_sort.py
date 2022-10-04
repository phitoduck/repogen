from enum import Enum


class IssueslistForAuthenticatedUserSort(str, Enum):
    CREATED = "created"
    UPDATED = "updated"
    COMMENTS = "comments"

    def __str__(self) -> str:
        return str(self.value)
