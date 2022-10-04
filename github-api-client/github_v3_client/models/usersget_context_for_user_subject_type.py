from enum import Enum


class UsersgetContextForUserSubjectType(str, Enum):
    ORGANIZATION = "organization"
    REPOSITORY = "repository"
    ISSUE = "issue"
    PULL_REQUEST = "pull_request"

    def __str__(self) -> str:
        return str(self.value)
