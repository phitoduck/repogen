from enum import Enum


class ActionscreateSelfHostedRunnerGroupForOrgJsonBodyVisibility(str, Enum):
    SELECTED = "selected"
    ALL = "all"
    PRIVATE = "private"

    def __str__(self) -> str:
        return str(self.value)
