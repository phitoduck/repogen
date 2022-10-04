from enum import Enum


class ReposcreateForAuthenticatedUserJsonBodyMergeCommitTitle(str, Enum):
    PR_TITLE = "PR_TITLE"
    MERGE_MESSAGE = "MERGE_MESSAGE"

    def __str__(self) -> str:
        return str(self.value)
