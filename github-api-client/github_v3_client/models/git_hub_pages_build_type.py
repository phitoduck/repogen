from enum import Enum


class GitHubPagesBuildType(str, Enum):
    LEGACY = "legacy"
    WORKFLOW = "workflow"

    def __str__(self) -> str:
        return str(self.value)
