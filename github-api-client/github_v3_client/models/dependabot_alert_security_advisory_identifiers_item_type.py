from enum import Enum


class DependabotAlertSecurityAdvisoryIdentifiersItemType(str, Enum):
    CVE = "CVE"
    GHSA = "GHSA"

    def __str__(self) -> str:
        return str(self.value)
