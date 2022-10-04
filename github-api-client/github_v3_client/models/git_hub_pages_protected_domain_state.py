from enum import Enum


class GitHubPagesProtectedDomainState(str, Enum):
    PENDING = "pending"
    VERIFIED = "verified"
    UNVERIFIED = "unverified"

    def __str__(self) -> str:
        return str(self.value)
