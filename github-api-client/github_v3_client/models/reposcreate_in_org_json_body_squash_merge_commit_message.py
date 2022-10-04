from enum import Enum


class ReposcreateInOrgJsonBodySquashMergeCommitMessage(str, Enum):
    PR_BODY = "PR_BODY"
    COMMIT_MESSAGES = "COMMIT_MESSAGES"
    BLANK = "BLANK"

    def __str__(self) -> str:
        return str(self.value)
