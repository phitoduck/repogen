from enum import Enum


class GitcreateTreeJsonBodyTreeItemMode(str, Enum):
    VALUE_0 = "100644"
    VALUE_1 = "100755"
    VALUE_2 = "040000"
    VALUE_3 = "160000"
    VALUE_4 = "120000"

    def __str__(self) -> str:
        return str(self.value)
