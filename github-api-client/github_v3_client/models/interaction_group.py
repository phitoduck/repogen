from enum import Enum


class InteractionGroup(str, Enum):
    EXISTING_USERS = "existing_users"
    CONTRIBUTORS_ONLY = "contributors_only"
    COLLABORATORS_ONLY = "collaborators_only"

    def __str__(self) -> str:
        return str(self.value)
