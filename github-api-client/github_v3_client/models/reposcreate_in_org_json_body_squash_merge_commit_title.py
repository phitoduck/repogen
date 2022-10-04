from enum import Enum


class ReposcreateInOrgJsonBodySquashMergeCommitTitle(str, Enum):
    PR_TITLE = "PR_TITLE"
    COMMIT_OR_PR_TITLE = "COMMIT_OR_PR_TITLE"

    def __str__(self) -> str:
        return str(self.value)
