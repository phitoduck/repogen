from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.teamscreate_json_body_permission import TeamscreateJsonBodyPermission
from ..models.teamscreate_json_body_privacy import TeamscreateJsonBodyPrivacy
from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamscreateJsonBody")


@attr.s(auto_attribs=True)
class TeamscreateJsonBody:
    """
    Attributes:
        name (str): The name of the team.
        description (Union[Unset, str]): The description of the team.
        maintainers (Union[Unset, List[str]]): List GitHub IDs for organization members who will become team
            maintainers.
        repo_names (Union[Unset, List[str]]): The full name (e.g., "organization-name/repository-name") of repositories
            to add the team to.
        privacy (Union[Unset, TeamscreateJsonBodyPrivacy]): The level of privacy this team should have. The options are:
            **For a non-nested team:**
            \* `secret` - only visible to organization owners and members of this team.
            \* `closed` - visible to all members of this organization.
            Default: `secret`
            **For a parent or child team:**
            \* `closed` - visible to all members of this organization.
            Default for child team: `closed`
        permission (Union[Unset, TeamscreateJsonBodyPermission]): **Deprecated**. The permission that new repositories
            will be added to the team with when none is specified. Default: TeamscreateJsonBodyPermission.PULL.
        parent_team_id (Union[Unset, int]): The ID of a team to set as the parent team.
    """

    name: str
    description: Union[Unset, str] = UNSET
    maintainers: Union[Unset, List[str]] = UNSET
    repo_names: Union[Unset, List[str]] = UNSET
    privacy: Union[Unset, TeamscreateJsonBodyPrivacy] = UNSET
    permission: Union[Unset, TeamscreateJsonBodyPermission] = TeamscreateJsonBodyPermission.PULL
    parent_team_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        description = self.description
        maintainers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.maintainers, Unset):
            maintainers = self.maintainers

        repo_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.repo_names, Unset):
            repo_names = self.repo_names

        privacy: Union[Unset, str] = UNSET
        if not isinstance(self.privacy, Unset):
            privacy = self.privacy.value

        permission: Union[Unset, str] = UNSET
        if not isinstance(self.permission, Unset):
            permission = self.permission.value

        parent_team_id = self.parent_team_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if maintainers is not UNSET:
            field_dict["maintainers"] = maintainers
        if repo_names is not UNSET:
            field_dict["repo_names"] = repo_names
        if privacy is not UNSET:
            field_dict["privacy"] = privacy
        if permission is not UNSET:
            field_dict["permission"] = permission
        if parent_team_id is not UNSET:
            field_dict["parent_team_id"] = parent_team_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        description = d.pop("description", UNSET)

        maintainers = cast(List[str], d.pop("maintainers", UNSET))

        repo_names = cast(List[str], d.pop("repo_names", UNSET))

        _privacy = d.pop("privacy", UNSET)
        privacy: Union[Unset, TeamscreateJsonBodyPrivacy]
        if isinstance(_privacy, Unset):
            privacy = UNSET
        else:
            privacy = TeamscreateJsonBodyPrivacy(_privacy)

        _permission = d.pop("permission", UNSET)
        permission: Union[Unset, TeamscreateJsonBodyPermission]
        if isinstance(_permission, Unset):
            permission = UNSET
        else:
            permission = TeamscreateJsonBodyPermission(_permission)

        parent_team_id = d.pop("parent_team_id", UNSET)

        teamscreate_json_body = cls(
            name=name,
            description=description,
            maintainers=maintainers,
            repo_names=repo_names,
            privacy=privacy,
            permission=permission,
            parent_team_id=parent_team_id,
        )

        teamscreate_json_body.additional_properties = d
        return teamscreate_json_body

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
