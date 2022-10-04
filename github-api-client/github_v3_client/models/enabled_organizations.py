from enum import Enum


class EnabledOrganizations(str, Enum):
    ALL = "all"
    NONE = "none"
    SELECTED = "selected"

    def __str__(self) -> str:
        return str(self.value)
