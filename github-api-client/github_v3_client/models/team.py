from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..models.team_permissions import TeamPermissions
from ..models.team_simple import TeamSimple
from ..types import UNSET, Unset

T = TypeVar("T", bound="Team")


@attr.s(auto_attribs=True)
class Team:
    """Groups of organization members that gives permissions on specified repositories.

    Attributes:
        id (int):
        node_id (str):
        name (str):
        slug (str):
        permission (str):
        url (str):
        html_url (str):  Example: https://github.com/orgs/rails/teams/core.
        members_url (str):
        repositories_url (str):
        description (Optional[str]):
        privacy (Union[Unset, str]):
        permissions (Union[Unset, TeamPermissions]):
        parent (Optional[TeamSimple]): Groups of organization members that gives permissions on specified repositories.
    """

    id: int
    node_id: str
    name: str
    slug: str
    permission: str
    url: str
    html_url: str
    members_url: str
    repositories_url: str
    description: Optional[str]
    parent: Optional[TeamSimple]
    privacy: Union[Unset, str] = UNSET
    permissions: Union[Unset, TeamPermissions] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        node_id = self.node_id
        name = self.name
        slug = self.slug
        permission = self.permission
        url = self.url
        html_url = self.html_url
        members_url = self.members_url
        repositories_url = self.repositories_url
        description = self.description
        privacy = self.privacy
        permissions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        parent = self.parent.to_dict() if self.parent else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "node_id": node_id,
                "name": name,
                "slug": slug,
                "permission": permission,
                "url": url,
                "html_url": html_url,
                "members_url": members_url,
                "repositories_url": repositories_url,
                "description": description,
                "parent": parent,
            }
        )
        if privacy is not UNSET:
            field_dict["privacy"] = privacy
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        node_id = d.pop("node_id")

        name = d.pop("name")

        slug = d.pop("slug")

        permission = d.pop("permission")

        url = d.pop("url")

        html_url = d.pop("html_url")

        members_url = d.pop("members_url")

        repositories_url = d.pop("repositories_url")

        description = d.pop("description")

        privacy = d.pop("privacy", UNSET)

        _permissions = d.pop("permissions", UNSET)
        permissions: Union[Unset, TeamPermissions]
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = TeamPermissions.from_dict(_permissions)

        _parent = d.pop("parent")
        parent: Optional[TeamSimple]
        if _parent is None:
            parent = None
        else:
            parent = TeamSimple.from_dict(_parent)

        team = cls(
            id=id,
            node_id=node_id,
            name=name,
            slug=slug,
            permission=permission,
            url=url,
            html_url=html_url,
            members_url=members_url,
            repositories_url=repositories_url,
            description=description,
            privacy=privacy,
            permissions=permissions,
            parent=parent,
        )

        team.additional_properties = d
        return team

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
