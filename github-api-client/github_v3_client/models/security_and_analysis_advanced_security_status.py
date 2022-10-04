from enum import Enum


class SecurityAndAnalysisAdvancedSecurityStatus(str, Enum):
    ENABLED = "enabled"
    DISABLED = "disabled"

    def __str__(self) -> str:
        return str(self.value)
