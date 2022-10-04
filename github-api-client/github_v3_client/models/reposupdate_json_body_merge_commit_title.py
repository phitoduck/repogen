from enum import Enum


class ReposupdateJsonBodyMergeCommitTitle(str, Enum):
    PR_TITLE = "PR_TITLE"
    MERGE_MESSAGE = "MERGE_MESSAGE"

    def __str__(self) -> str:
        return str(self.value)
