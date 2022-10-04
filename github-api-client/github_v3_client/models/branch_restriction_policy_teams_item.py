from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="BranchRestrictionPolicyTeamsItem")


@attr.s(auto_attribs=True)
class BranchRestrictionPolicyTeamsItem:
    """
    Attributes:
        id (Union[Unset, int]):
        node_id (Union[Unset, str]):
        url (Union[Unset, str]):
        html_url (Union[Unset, str]):
        name (Union[Unset, str]):
        slug (Union[Unset, str]):
        description (Union[Unset, None, str]):
        privacy (Union[Unset, str]):
        permission (Union[Unset, str]):
        members_url (Union[Unset, str]):
        repositories_url (Union[Unset, str]):
        parent (Union[Unset, None, str]):
    """

    id: Union[Unset, int] = UNSET
    node_id: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    html_url: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    slug: Union[Unset, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    privacy: Union[Unset, str] = UNSET
    permission: Union[Unset, str] = UNSET
    members_url: Union[Unset, str] = UNSET
    repositories_url: Union[Unset, str] = UNSET
    parent: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        node_id = self.node_id
        url = self.url
        html_url = self.html_url
        name = self.name
        slug = self.slug
        description = self.description
        privacy = self.privacy
        permission = self.permission
        members_url = self.members_url
        repositories_url = self.repositories_url
        parent = self.parent

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if node_id is not UNSET:
            field_dict["node_id"] = node_id
        if url is not UNSET:
            field_dict["url"] = url
        if html_url is not UNSET:
            field_dict["html_url"] = html_url
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if description is not UNSET:
            field_dict["description"] = description
        if privacy is not UNSET:
            field_dict["privacy"] = privacy
        if permission is not UNSET:
            field_dict["permission"] = permission
        if members_url is not UNSET:
            field_dict["members_url"] = members_url
        if repositories_url is not UNSET:
            field_dict["repositories_url"] = repositories_url
        if parent is not UNSET:
            field_dict["parent"] = parent

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        node_id = d.pop("node_id", UNSET)

        url = d.pop("url", UNSET)

        html_url = d.pop("html_url", UNSET)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        description = d.pop("description", UNSET)

        privacy = d.pop("privacy", UNSET)

        permission = d.pop("permission", UNSET)

        members_url = d.pop("members_url", UNSET)

        repositories_url = d.pop("repositories_url", UNSET)

        parent = d.pop("parent", UNSET)

        branch_restriction_policy_teams_item = cls(
            id=id,
            node_id=node_id,
            url=url,
            html_url=html_url,
            name=name,
            slug=slug,
            description=description,
            privacy=privacy,
            permission=permission,
            members_url=members_url,
            repositories_url=repositories_url,
            parent=parent,
        )

        branch_restriction_policy_teams_item.additional_properties = d
        return branch_restriction_policy_teams_item

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
