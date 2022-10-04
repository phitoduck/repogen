from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TagProtection")


@attr.s(auto_attribs=True)
class TagProtection:
    """Tag protection

    Attributes:
        pattern (str):  Example: v1.*.
        id (Union[Unset, int]):  Example: 2.
        created_at (Union[Unset, str]):  Example: 2011-01-26T19:01:12Z.
        updated_at (Union[Unset, str]):  Example: 2011-01-26T19:01:12Z.
        enabled (Union[Unset, bool]):  Example: True.
    """

    pattern: str
    id: Union[Unset, int] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pattern = self.pattern
        id = self.id
        created_at = self.created_at
        updated_at = self.updated_at
        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pattern": pattern,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        pattern = d.pop("pattern")

        id = d.pop("id", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        enabled = d.pop("enabled", UNSET)

        tag_protection = cls(
            pattern=pattern,
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            enabled=enabled,
        )

        tag_protection.additional_properties = d
        return tag_protection

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
