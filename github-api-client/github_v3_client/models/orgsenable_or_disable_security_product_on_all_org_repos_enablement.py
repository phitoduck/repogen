from enum import Enum


class OrgsenableOrDisableSecurityProductOnAllOrgReposEnablement(str, Enum):
    ENABLE_ALL = "enable_all"
    DISABLE_ALL = "disable_all"

    def __str__(self) -> str:
        return str(self.value)
