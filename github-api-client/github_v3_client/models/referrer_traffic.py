from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ReferrerTraffic")


@attr.s(auto_attribs=True)
class ReferrerTraffic:
    """Referrer Traffic

    Attributes:
        referrer (str):  Example: Google.
        count (int):  Example: 4.
        uniques (int):  Example: 3.
    """

    referrer: str
    count: int
    uniques: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        referrer = self.referrer
        count = self.count
        uniques = self.uniques

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "referrer": referrer,
                "count": count,
                "uniques": uniques,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        referrer = d.pop("referrer")

        count = d.pop("count")

        uniques = d.pop("uniques")

        referrer_traffic = cls(
            referrer=referrer,
            count=count,
            uniques=uniques,
        )

        referrer_traffic.additional_properties = d
        return referrer_traffic

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
