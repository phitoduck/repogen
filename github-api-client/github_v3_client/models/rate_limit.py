from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="RateLimit")


@attr.s(auto_attribs=True)
class RateLimit:
    """
    Attributes:
        limit (int):
        remaining (int):
        reset (int):
        used (int):
    """

    limit: int
    remaining: int
    reset: int
    used: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        limit = self.limit
        remaining = self.remaining
        reset = self.reset
        used = self.used

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "limit": limit,
                "remaining": remaining,
                "reset": reset,
                "used": used,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        limit = d.pop("limit")

        remaining = d.pop("remaining")

        reset = d.pop("reset")

        used = d.pop("used")

        rate_limit = cls(
            limit=limit,
            remaining=remaining,
            reset=reset,
            used=used,
        )

        rate_limit.additional_properties = d
        return rate_limit

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
