from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="ParticipationStats")


@attr.s(auto_attribs=True)
class ParticipationStats:
    """
    Attributes:
        all_ (List[int]):
        owner (List[int]):
    """

    all_: List[int]
    owner: List[int]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        all_ = self.all_

        owner = self.owner

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "all": all_,
                "owner": owner,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        all_ = cast(List[int], d.pop("all"))

        owner = cast(List[int], d.pop("owner"))

        participation_stats = cls(
            all_=all_,
            owner=owner,
        )

        participation_stats.additional_properties = d
        return participation_stats

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
