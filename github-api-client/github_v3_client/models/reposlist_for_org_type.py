from enum import Enum


class ReposlistForOrgType(str, Enum):
    ALL = "all"
    PUBLIC = "public"
    PRIVATE = "private"
    FORKS = "forks"
    SOURCES = "sources"
    MEMBER = "member"
    INTERNAL = "internal"

    def __str__(self) -> str:
        return str(self.value)
