from enum import Enum


class GistscreateJsonBodyPublicType1(str, Enum):
    TRUE = "true"
    FALSE = "false"

    def __str__(self) -> str:
        return str(self.value)
