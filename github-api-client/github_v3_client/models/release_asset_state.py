from enum import Enum


class ReleaseAssetState(str, Enum):
    UPLOADED = "uploaded"
    OPEN = "open"

    def __str__(self) -> str:
        return str(self.value)
