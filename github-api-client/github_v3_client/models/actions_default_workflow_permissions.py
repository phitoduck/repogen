from enum import Enum


class ActionsDefaultWorkflowPermissions(str, Enum):
    READ = "read"
    WRITE = "write"

    def __str__(self) -> str:
        return str(self.value)
