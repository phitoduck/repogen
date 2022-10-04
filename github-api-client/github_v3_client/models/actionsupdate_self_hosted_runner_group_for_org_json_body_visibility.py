from enum import Enum


class ActionsupdateSelfHostedRunnerGroupForOrgJsonBodyVisibility(str, Enum):
    SELECTED = "selected"
    ALL = "all"
    PRIVATE = "private"

    def __str__(self) -> str:
        return str(self.value)
