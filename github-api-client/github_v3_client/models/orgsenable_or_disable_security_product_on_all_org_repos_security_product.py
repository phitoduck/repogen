from enum import Enum


class OrgsenableOrDisableSecurityProductOnAllOrgReposSecurityProduct(str, Enum):
    DEPENDENCY_GRAPH = "dependency_graph"
    DEPENDABOT_ALERTS = "dependabot_alerts"
    DEPENDABOT_SECURITY_UPDATES = "dependabot_security_updates"
    ADVANCED_SECURITY = "advanced_security"
    SECRET_SCANNING = "secret_scanning"
    SECRET_SCANNING_PUSH_PROTECTION = "secret_scanning_push_protection"

    def __str__(self) -> str:
        return str(self.value)
