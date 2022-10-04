from enum import Enum


class ReposupdateInvitationJsonBodyPermissions(str, Enum):
    READ = "read"
    WRITE = "write"
    MAINTAIN = "maintain"
    TRIAGE = "triage"
    ADMIN = "admin"

    def __str__(self) -> str:
        return str(self.value)
