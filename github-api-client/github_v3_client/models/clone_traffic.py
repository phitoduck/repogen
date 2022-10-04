from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.traffic import Traffic

T = TypeVar("T", bound="CloneTraffic")


@attr.s(auto_attribs=True)
class CloneTraffic:
    """Clone Traffic

    Attributes:
        count (int):  Example: 173.
        uniques (int):  Example: 128.
        clones (List[Traffic]):
    """

    count: int
    uniques: int
    clones: List[Traffic]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count = self.count
        uniques = self.uniques
        clones = []
        for clones_item_data in self.clones:
            clones_item = clones_item_data.to_dict()

            clones.append(clones_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "uniques": uniques,
                "clones": clones,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        count = d.pop("count")

        uniques = d.pop("uniques")

        clones = []
        _clones = d.pop("clones")
        for clones_item_data in _clones:
            clones_item = Traffic.from_dict(clones_item_data)

            clones.append(clones_item)

        clone_traffic = cls(
            count=count,
            uniques=uniques,
            clones=clones,
        )

        clone_traffic.additional_properties = d
        return clone_traffic

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
