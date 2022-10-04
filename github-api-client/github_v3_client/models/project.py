import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.project_organization_permission import ProjectOrganizationPermission
from ..models.simple_user import SimpleUser
from ..types import UNSET, Unset

T = TypeVar("T", bound="Project")


@attr.s(auto_attribs=True)
class Project:
    """Projects are a way to organize columns and cards of work.

    Attributes:
        owner_url (str):  Example: https://api.github.com/repos/api-playground/projects-test.
        url (str):  Example: https://api.github.com/projects/1002604.
        html_url (str):  Example: https://github.com/api-playground/projects-test/projects/12.
        columns_url (str):  Example: https://api.github.com/projects/1002604/columns.
        id (int):  Example: 1002604.
        node_id (str):  Example: MDc6UHJvamVjdDEwMDI2MDQ=.
        name (str): Name of the project Example: Week One Sprint.
        number (int):  Example: 1.
        state (str): State of the project; either 'open' or 'closed' Example: open.
        created_at (datetime.datetime):  Example: 2011-04-10T20:09:31Z.
        updated_at (datetime.datetime):  Example: 2014-03-03T18:58:10Z.
        body (Optional[str]): Body of the project Example: This project represents the sprint of the first week in
            January.
        creator (Optional[SimpleUser]): Simple User
        organization_permission (Union[Unset, ProjectOrganizationPermission]): The baseline permission that all
            organization members have on this project. Only present if owner is an organization.
        private (Union[Unset, bool]): Whether or not this project can be seen by everyone. Only present if owner is an
            organization.
    """

    owner_url: str
    url: str
    html_url: str
    columns_url: str
    id: int
    node_id: str
    name: str
    number: int
    state: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    body: Optional[str]
    creator: Optional[SimpleUser]
    organization_permission: Union[Unset, ProjectOrganizationPermission] = UNSET
    private: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        owner_url = self.owner_url
        url = self.url
        html_url = self.html_url
        columns_url = self.columns_url
        id = self.id
        node_id = self.node_id
        name = self.name
        number = self.number
        state = self.state
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        body = self.body
        creator = self.creator.to_dict() if self.creator else None

        organization_permission: Union[Unset, str] = UNSET
        if not isinstance(self.organization_permission, Unset):
            organization_permission = self.organization_permission.value

        private = self.private

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "owner_url": owner_url,
                "url": url,
                "html_url": html_url,
                "columns_url": columns_url,
                "id": id,
                "node_id": node_id,
                "name": name,
                "number": number,
                "state": state,
                "created_at": created_at,
                "updated_at": updated_at,
                "body": body,
                "creator": creator,
            }
        )
        if organization_permission is not UNSET:
            field_dict["organization_permission"] = organization_permission
        if private is not UNSET:
            field_dict["private"] = private

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        owner_url = d.pop("owner_url")

        url = d.pop("url")

        html_url = d.pop("html_url")

        columns_url = d.pop("columns_url")

        id = d.pop("id")

        node_id = d.pop("node_id")

        name = d.pop("name")

        number = d.pop("number")

        state = d.pop("state")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        body = d.pop("body")

        _creator = d.pop("creator")
        creator: Optional[SimpleUser]
        if _creator is None:
            creator = None
        else:
            creator = SimpleUser.from_dict(_creator)

        _organization_permission = d.pop("organization_permission", UNSET)
        organization_permission: Union[Unset, ProjectOrganizationPermission]
        if isinstance(_organization_permission, Unset):
            organization_permission = UNSET
        else:
            organization_permission = ProjectOrganizationPermission(_organization_permission)

        private = d.pop("private", UNSET)

        project = cls(
            owner_url=owner_url,
            url=url,
            html_url=html_url,
            columns_url=columns_url,
            id=id,
            node_id=node_id,
            name=name,
            number=number,
            state=state,
            created_at=created_at,
            updated_at=updated_at,
            body=body,
            creator=creator,
            organization_permission=organization_permission,
            private=private,
        )

        project.additional_properties = d
        return project

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
