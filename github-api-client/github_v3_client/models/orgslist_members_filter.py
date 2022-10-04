from enum import Enum


class OrgslistMembersFilter(str, Enum):
    VALUE_0 = "2fa_disabled"
    ALL = "all"

    def __str__(self) -> str:
        return str(self.value)
