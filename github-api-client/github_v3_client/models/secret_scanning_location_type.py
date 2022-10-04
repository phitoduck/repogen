from enum import Enum


class SecretScanningLocationType(str, Enum):
    COMMIT = "commit"

    def __str__(self) -> str:
        return str(self.value)
