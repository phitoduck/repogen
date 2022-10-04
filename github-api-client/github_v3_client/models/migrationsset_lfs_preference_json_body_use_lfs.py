from enum import Enum


class MigrationssetLfsPreferenceJsonBodyUseLfs(str, Enum):
    OPT_IN = "opt_in"
    OPT_OUT = "opt_out"

    def __str__(self) -> str:
        return str(self.value)
