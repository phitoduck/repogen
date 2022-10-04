from enum import Enum


class ReposcreateInOrgJsonBodyMergeCommitMessage(str, Enum):
    PR_BODY = "PR_BODY"
    PR_TITLE = "PR_TITLE"
    BLANK = "BLANK"

    def __str__(self) -> str:
        return str(self.value)
