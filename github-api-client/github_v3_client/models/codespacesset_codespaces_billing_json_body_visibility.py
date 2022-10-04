from enum import Enum


class CodespacessetCodespacesBillingJsonBodyVisibility(str, Enum):
    DISABLED = "disabled"
    SELECTED_MEMBERS = "selected_members"
    ALL_MEMBERS = "all_members"
    ALL_MEMBERS_AND_OUTSIDE_COLLABORATORS = "all_members_and_outside_collaborators"

    def __str__(self) -> str:
        return str(self.value)
