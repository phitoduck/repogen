from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.teamsupdate_in_org_json_body_permission import TeamsupdateInOrgJsonBodyPermission
from ..models.teamsupdate_in_org_json_body_privacy import TeamsupdateInOrgJsonBodyPrivacy
from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamsupdateInOrgJsonBody")


@attr.s(auto_attribs=True)
class TeamsupdateInOrgJsonBody:
    """
    Attributes:
        name (Union[Unset, str]): The name of the team.
        description (Union[Unset, str]): The description of the team.
        privacy (Union[Unset, TeamsupdateInOrgJsonBodyPrivacy]): The level of privacy this team should have. Editing
            teams without specifying this parameter leaves `privacy` intact. When a team is nested, the `privacy` for parent
            teams cannot be `secret`. The options are:
            **For a non-nested team:**
            \* `secret` - only visible to organization owners and members of this team.
            \* `closed` - visible to all members of this organization.
            **For a parent or child team:**
            \* `closed` - visible to all members of this organization.
        permission (Union[Unset, TeamsupdateInOrgJsonBodyPermission]): **Deprecated**. The permission that new
            repositories will be added to the team with when none is specified. Default:
            TeamsupdateInOrgJsonBodyPermission.PULL.
        parent_team_id (Union[Unset, None, int]): The ID of a team to set as the parent team.
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    privacy: Union[Unset, TeamsupdateInOrgJsonBodyPrivacy] = UNSET
    permission: Union[Unset, TeamsupdateInOrgJsonBodyPermission] = TeamsupdateInOrgJsonBodyPermission.PULL
    parent_team_id: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        description = self.description
        privacy: Union[Unset, str] = UNSET
        if not isinstance(self.privacy, Unset):
            privacy = self.privacy.value

        permission: Union[Unset, str] = UNSET
        if not isinstance(self.permission, Unset):
            permission = self.permission.value

        parent_team_id = self.parent_team_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
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
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _privacy = d.pop("privacy", UNSET)
        privacy: Union[Unset, TeamsupdateInOrgJsonBodyPrivacy]
        if isinstance(_privacy, Unset):
            privacy = UNSET
        else:
            privacy = TeamsupdateInOrgJsonBodyPrivacy(_privacy)

        _permission = d.pop("permission", UNSET)
        permission: Union[Unset, TeamsupdateInOrgJsonBodyPermission]
        if isinstance(_permission, Unset):
            permission = UNSET
        else:
            permission = TeamsupdateInOrgJsonBodyPermission(_permission)

        parent_team_id = d.pop("parent_team_id", UNSET)

        teamsupdate_in_org_json_body = cls(
            name=name,
            description=description,
            privacy=privacy,
            permission=permission,
            parent_team_id=parent_team_id,
        )

        teamsupdate_in_org_json_body.additional_properties = d
        return teamsupdate_in_org_json_body

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
