from enum import Enum


class GitcreateTreeJsonBodyTreeItemType(str, Enum):
    BLOB = "blob"
    TREE = "tree"
    COMMIT = "commit"

    def __str__(self) -> str:
        return str(self.value)
