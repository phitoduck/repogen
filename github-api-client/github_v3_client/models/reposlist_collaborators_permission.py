from enum import Enum


class ReposlistCollaboratorsPermission(str, Enum):
    PULL = "pull"
    TRIAGE = "triage"
    PUSH = "push"
    MAINTAIN = "maintain"
    ADMIN = "admin"

    def __str__(self) -> str:
        return str(self.value)
