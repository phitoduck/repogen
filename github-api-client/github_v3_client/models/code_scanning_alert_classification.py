from enum import Enum


class CodeScanningAlertClassification(str, Enum):
    SOURCE = "source"
    GENERATED = "generated"
    TEST = "test"
    LIBRARY = "library"

    def __str__(self) -> str:
        return str(self.value)
