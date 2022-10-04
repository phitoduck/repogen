import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RepositoryActionsCachesActionsCachesItem")


@attr.s(auto_attribs=True)
class RepositoryActionsCachesActionsCachesItem:
    """
    Attributes:
        id (Union[Unset, int]):  Example: 2.
        ref (Union[Unset, str]):  Example: refs/heads/main.
        key (Union[Unset, str]):  Example: Linux-node-958aff96db2d75d67787d1e634ae70b659de937b.
        version (Union[Unset, str]):  Example: 73885106f58cc52a7df9ec4d4a5622a5614813162cb516c759a30af6bf56e6f0.
        last_accessed_at (Union[Unset, datetime.datetime]):  Example: 2019-01-24T22:45:36.000Z.
        created_at (Union[Unset, datetime.datetime]):  Example: 2019-01-24T22:45:36.000Z.
        size_in_bytes (Union[Unset, int]):  Example: 1024.
    """

    id: Union[Unset, int] = UNSET
    ref: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    last_accessed_at: Union[Unset, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    size_in_bytes: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        ref = self.ref
        key = self.key
        version = self.version
        last_accessed_at: Union[Unset, str] = UNSET
        if not isinstance(self.last_accessed_at, Unset):
            last_accessed_at = self.last_accessed_at.isoformat()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        size_in_bytes = self.size_in_bytes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if ref is not UNSET:
            field_dict["ref"] = ref
        if key is not UNSET:
            field_dict["key"] = key
        if version is not UNSET:
            field_dict["version"] = version
        if last_accessed_at is not UNSET:
            field_dict["last_accessed_at"] = last_accessed_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if size_in_bytes is not UNSET:
            field_dict["size_in_bytes"] = size_in_bytes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        ref = d.pop("ref", UNSET)

        key = d.pop("key", UNSET)

        version = d.pop("version", UNSET)

        _last_accessed_at = d.pop("last_accessed_at", UNSET)
        last_accessed_at: Union[Unset, datetime.datetime]
        if isinstance(_last_accessed_at, Unset):
            last_accessed_at = UNSET
        else:
            last_accessed_at = isoparse(_last_accessed_at)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        size_in_bytes = d.pop("size_in_bytes", UNSET)

        repository_actions_caches_actions_caches_item = cls(
            id=id,
            ref=ref,
            key=key,
            version=version,
            last_accessed_at=last_accessed_at,
            created_at=created_at,
            size_in_bytes=size_in_bytes,
        )

        repository_actions_caches_actions_caches_item.additional_properties = d
        return repository_actions_caches_actions_caches_item

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
