from enum import Enum


class IssueslockJsonBodyLockReason(str, Enum):
    OFF_TOPIC = "off-topic"
    TOO_HEATED = "too heated"
    RESOLVED = "resolved"
    SPAM = "spam"

    def __str__(self) -> str:
        return str(self.value)
