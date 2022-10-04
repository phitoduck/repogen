from enum import Enum


class EnterpriseAdminupdateSelfHostedRunnerGroupForEnterpriseJsonBodyVisibility(str, Enum):
    SELECTED = "selected"
    ALL = "all"

    def __str__(self) -> str:
        return str(self.value)
