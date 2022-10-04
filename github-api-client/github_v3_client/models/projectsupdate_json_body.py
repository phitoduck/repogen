from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.projectsupdate_json_body_organization_permission import ProjectsupdateJsonBodyOrganizationPermission
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectsupdateJsonBody")


@attr.s(auto_attribs=True)
class ProjectsupdateJsonBody:
    """
    Attributes:
        name (Union[Unset, str]): Name of the project Example: Week One Sprint.
        body (Union[Unset, None, str]): Body of the project Example: This project represents the sprint of the first
            week in January.
        state (Union[Unset, str]): State of the project; either 'open' or 'closed' Example: open.
        organization_permission (Union[Unset, ProjectsupdateJsonBodyOrganizationPermission]): The baseline permission
            that all organization members have on this project
        private (Union[Unset, bool]): Whether or not this project can be seen by everyone.
    """

    name: Union[Unset, str] = UNSET
    body: Union[Unset, None, str] = UNSET
    state: Union[Unset, str] = UNSET
    organization_permission: Union[Unset, ProjectsupdateJsonBodyOrganizationPermission] = UNSET
    private: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        body = self.body
        state = self.state
        organization_permission: Union[Unset, str] = UNSET
        if not isinstance(self.organization_permission, Unset):
            organization_permission = self.organization_permission.value

        private = self.private

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if body is not UNSET:
            field_dict["body"] = body
        if state is not UNSET:
            field_dict["state"] = state
        if organization_permission is not UNSET:
            field_dict["organization_permission"] = organization_permission
        if private is not UNSET:
            field_dict["private"] = private

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        body = d.pop("body", UNSET)

        state = d.pop("state", UNSET)

        _organization_permission = d.pop("organization_permission", UNSET)
        organization_permission: Union[Unset, ProjectsupdateJsonBodyOrganizationPermission]
        if isinstance(_organization_permission, Unset):
            organization_permission = UNSET
        else:
            organization_permission = ProjectsupdateJsonBodyOrganizationPermission(_organization_permission)

        private = d.pop("private", UNSET)

        projectsupdate_json_body = cls(
            name=name,
            body=body,
            state=state,
            organization_permission=organization_permission,
            private=private,
        )

        projectsupdate_json_body.additional_properties = d
        return projectsupdate_json_body

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
