from enum import Enum


class ActionsWorkflowAccessToRepositoryAccessLevel(str, Enum):
    NONE = "none"
    ORGANIZATION = "organization"
    ENTERPRISE = "enterprise"

    def __str__(self) -> str:
        return str(self.value)
