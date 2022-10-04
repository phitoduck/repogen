from enum import Enum


class EnterpriseAdmincreateSelfHostedRunnerGroupForEnterpriseJsonBodyVisibility(str, Enum):
    SELECTED = "selected"
    ALL = "all"

    def __str__(self) -> str:
        return str(self.value)
