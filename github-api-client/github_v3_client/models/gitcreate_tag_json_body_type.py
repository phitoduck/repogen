from enum import Enum


class GitcreateTagJsonBodyType(str, Enum):
    COMMIT = "commit"
    TREE = "tree"
    BLOB = "blob"

    def __str__(self) -> str:
        return str(self.value)
