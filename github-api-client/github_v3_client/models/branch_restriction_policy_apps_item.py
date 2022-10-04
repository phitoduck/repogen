from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.branch_restriction_policy_apps_item_owner import BranchRestrictionPolicyAppsItemOwner
from ..models.branch_restriction_policy_apps_item_permissions import BranchRestrictionPolicyAppsItemPermissions
from ..types import UNSET, Unset

T = TypeVar("T", bound="BranchRestrictionPolicyAppsItem")


@attr.s(auto_attribs=True)
class BranchRestrictionPolicyAppsItem:
    """
    Attributes:
        id (Union[Unset, int]):
        slug (Union[Unset, str]):
        node_id (Union[Unset, str]):
        owner (Union[Unset, BranchRestrictionPolicyAppsItemOwner]):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        external_url (Union[Unset, str]):
        html_url (Union[Unset, str]):
        created_at (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        permissions (Union[Unset, BranchRestrictionPolicyAppsItemPermissions]):
        events (Union[Unset, List[str]]):
    """

    id: Union[Unset, int] = UNSET
    slug: Union[Unset, str] = UNSET
    node_id: Union[Unset, str] = UNSET
    owner: Union[Unset, BranchRestrictionPolicyAppsItemOwner] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    external_url: Union[Unset, str] = UNSET
    html_url: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    permissions: Union[Unset, BranchRestrictionPolicyAppsItemPermissions] = UNSET
    events: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        slug = self.slug
        node_id = self.node_id
        owner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        name = self.name
        description = self.description
        external_url = self.external_url
        html_url = self.html_url
        created_at = self.created_at
        updated_at = self.updated_at
        permissions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        events: Union[Unset, List[str]] = UNSET
        if not isinstance(self.events, Unset):
            events = self.events

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if slug is not UNSET:
            field_dict["slug"] = slug
        if node_id is not UNSET:
            field_dict["node_id"] = node_id
        if owner is not UNSET:
            field_dict["owner"] = owner
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if external_url is not UNSET:
            field_dict["external_url"] = external_url
        if html_url is not UNSET:
            field_dict["html_url"] = html_url
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        slug = d.pop("slug", UNSET)

        node_id = d.pop("node_id", UNSET)

        _owner = d.pop("owner", UNSET)
        owner: Union[Unset, BranchRestrictionPolicyAppsItemOwner]
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = BranchRestrictionPolicyAppsItemOwner.from_dict(_owner)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        external_url = d.pop("external_url", UNSET)

        html_url = d.pop("html_url", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _permissions = d.pop("permissions", UNSET)
        permissions: Union[Unset, BranchRestrictionPolicyAppsItemPermissions]
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = BranchRestrictionPolicyAppsItemPermissions.from_dict(_permissions)

        events = cast(List[str], d.pop("events", UNSET))

        branch_restriction_policy_apps_item = cls(
            id=id,
            slug=slug,
            node_id=node_id,
            owner=owner,
            name=name,
            description=description,
            external_url=external_url,
            html_url=html_url,
            created_at=created_at,
            updated_at=updated_at,
            permissions=permissions,
            events=events,
        )

        branch_restriction_policy_apps_item.additional_properties = d
        return branch_restriction_policy_apps_item

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
