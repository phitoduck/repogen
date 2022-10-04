from enum import Enum


class ActionslistJobsForWorkflowRunFilter(str, Enum):
    LATEST = "latest"
    ALL = "all"

    def __str__(self) -> str:
        return str(self.value)
