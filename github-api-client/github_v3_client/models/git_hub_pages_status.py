from enum import Enum


class GitHubPagesStatus(str, Enum):
    BUILT = "built"
    BUILDING = "building"
    ERRORED = "errored"

    def __str__(self) -> str:
        return str(self.value)
