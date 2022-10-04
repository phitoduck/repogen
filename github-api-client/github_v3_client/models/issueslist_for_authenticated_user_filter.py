from enum import Enum


class IssueslistForAuthenticatedUserFilter(str, Enum):
    ASSIGNED = "assigned"
    CREATED = "created"
    MENTIONED = "mentioned"
    SUBSCRIBED = "subscribed"
    REPOS = "repos"
    ALL = "all"

    def __str__(self) -> str:
        return str(self.value)
