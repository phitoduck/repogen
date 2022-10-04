from enum import Enum


class ReposlistCollaboratorsAffiliation(str, Enum):
    OUTSIDE = "outside"
    DIRECT = "direct"
    ALL = "all"

    def __str__(self) -> str:
        return str(self.value)
