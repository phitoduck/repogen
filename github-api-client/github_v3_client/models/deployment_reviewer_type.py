from enum import Enum


class DeploymentReviewerType(str, Enum):
    USER = "User"
    TEAM = "Team"

    def __str__(self) -> str:
        return str(self.value)
