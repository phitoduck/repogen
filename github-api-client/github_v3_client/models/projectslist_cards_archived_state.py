from enum import Enum


class ProjectslistCardsArchivedState(str, Enum):
    ALL = "all"
    ARCHIVED = "archived"
    NOT_ARCHIVED = "not_archived"

    def __str__(self) -> str:
        return str(self.value)
