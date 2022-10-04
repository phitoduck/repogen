from enum import Enum


class ReposupdateJsonBodyVisibility(str, Enum):
    PUBLIC = "public"
    PRIVATE = "private"
    INTERNAL = "internal"

    def __str__(self) -> str:
        return str(self.value)
