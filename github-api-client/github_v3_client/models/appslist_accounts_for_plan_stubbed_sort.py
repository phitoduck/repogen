from enum import Enum


class AppslistAccountsForPlanStubbedSort(str, Enum):
    CREATED = "created"
    UPDATED = "updated"

    def __str__(self) -> str:
        return str(self.value)
