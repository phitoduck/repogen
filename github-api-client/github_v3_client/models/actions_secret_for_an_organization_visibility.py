from enum import Enum


class ActionsSecretForAnOrganizationVisibility(str, Enum):
    ALL = "all"
    PRIVATE = "private"
    SELECTED = "selected"

    def __str__(self) -> str:
        return str(self.value)
