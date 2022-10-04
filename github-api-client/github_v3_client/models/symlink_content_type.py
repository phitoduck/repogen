from enum import Enum


class SymlinkContentType(str, Enum):
    SYMLINK = "symlink"

    def __str__(self) -> str:
        return str(self.value)
