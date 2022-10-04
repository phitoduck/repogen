from enum import Enum


class ReposcreateDeploymentStatusJsonBodyEnvironment(str, Enum):
    PRODUCTION = "production"
    STAGING = "staging"
    QA = "qa"

    def __str__(self) -> str:
        return str(self.value)
