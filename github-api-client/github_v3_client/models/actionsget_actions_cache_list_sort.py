from enum import Enum


class ActionsgetActionsCacheListSort(str, Enum):
    CREATED_AT = "created_at"
    LAST_ACCESSED_AT = "last_accessed_at"
    SIZE_IN_BYTES = "size_in_bytes"

    def __str__(self) -> str:
        return str(self.value)
