from enum import Enum


class SelfHostedRunnerLabelType(str, Enum):
    READ_ONLY = "read-only"
    CUSTOM = "custom"

    def __str__(self) -> str:
        return str(self.value)
