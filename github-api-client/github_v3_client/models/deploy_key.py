from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeployKey")


@attr.s(auto_attribs=True)
class DeployKey:
    """An SSH key granting access to a single repository.

    Attributes:
        id (int):
        key (str):
        url (str):
        title (str):
        verified (bool):
        created_at (str):
        read_only (bool):
        added_by (Union[Unset, None, str]):
        last_used (Union[Unset, None, str]):
    """

    id: int
    key: str
    url: str
    title: str
    verified: bool
    created_at: str
    read_only: bool
    added_by: Union[Unset, None, str] = UNSET
    last_used: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        key = self.key
        url = self.url
        title = self.title
        verified = self.verified
        created_at = self.created_at
        read_only = self.read_only
        added_by = self.added_by
        last_used = self.last_used

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "key": key,
                "url": url,
                "title": title,
                "verified": verified,
                "created_at": created_at,
                "read_only": read_only,
            }
        )
        if added_by is not UNSET:
            field_dict["added_by"] = added_by
        if last_used is not UNSET:
            field_dict["last_used"] = last_used

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        key = d.pop("key")

        url = d.pop("url")

        title = d.pop("title")

        verified = d.pop("verified")

        created_at = d.pop("created_at")

        read_only = d.pop("read_only")

        added_by = d.pop("added_by", UNSET)

        last_used = d.pop("last_used", UNSET)

        deploy_key = cls(
            id=id,
            key=key,
            url=url,
            title=title,
            verified=verified,
            created_at=created_at,
            read_only=read_only,
            added_by=added_by,
            last_used=last_used,
        )

        deploy_key.additional_properties = d
        return deploy_key

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
