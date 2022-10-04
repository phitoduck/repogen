from enum import Enum


class IssueslistFilter(str, Enum):
    ASSIGNED = "assigned"
    CREATED = "created"
    MENTIONED = "mentioned"
    SUBSCRIBED = "subscribed"
    REPOS = "repos"
    ALL = "all"

    def __str__(self) -> str:
        return str(self.value)
