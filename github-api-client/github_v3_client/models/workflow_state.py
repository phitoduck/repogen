from enum import Enum


class WorkflowState(str, Enum):
    ACTIVE = "active"
    DELETED = "deleted"
    DISABLED_FORK = "disabled_fork"
    DISABLED_INACTIVITY = "disabled_inactivity"
    DISABLED_MANUALLY = "disabled_manually"

    def __str__(self) -> str:
        return str(self.value)
