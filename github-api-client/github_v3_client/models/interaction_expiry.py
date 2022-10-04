from enum import Enum


class InteractionExpiry(str, Enum):
    ONE_DAY = "one_day"
    THREE_DAYS = "three_days"
    ONE_WEEK = "one_week"
    ONE_MONTH = "one_month"
    SIX_MONTHS = "six_months"

    def __str__(self) -> str:
        return str(self.value)
