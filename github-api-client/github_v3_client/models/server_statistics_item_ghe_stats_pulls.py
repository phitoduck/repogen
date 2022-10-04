from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerStatisticsItemGheStatsPulls")


@attr.s(auto_attribs=True)
class ServerStatisticsItemGheStatsPulls:
    """
    Attributes:
        total_pulls (Union[Unset, int]):
        merged_pulls (Union[Unset, int]):
        mergeable_pulls (Union[Unset, int]):
        unmergeable_pulls (Union[Unset, int]):
    """

    total_pulls: Union[Unset, int] = UNSET
    merged_pulls: Union[Unset, int] = UNSET
    mergeable_pulls: Union[Unset, int] = UNSET
    unmergeable_pulls: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_pulls = self.total_pulls
        merged_pulls = self.merged_pulls
        mergeable_pulls = self.mergeable_pulls
        unmergeable_pulls = self.unmergeable_pulls

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_pulls is not UNSET:
            field_dict["total_pulls"] = total_pulls
        if merged_pulls is not UNSET:
            field_dict["merged_pulls"] = merged_pulls
        if mergeable_pulls is not UNSET:
            field_dict["mergeable_pulls"] = mergeable_pulls
        if unmergeable_pulls is not UNSET:
            field_dict["unmergeable_pulls"] = unmergeable_pulls

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_pulls = d.pop("total_pulls", UNSET)

        merged_pulls = d.pop("merged_pulls", UNSET)

        mergeable_pulls = d.pop("mergeable_pulls", UNSET)

        unmergeable_pulls = d.pop("unmergeable_pulls", UNSET)

        server_statistics_item_ghe_stats_pulls = cls(
            total_pulls=total_pulls,
            merged_pulls=merged_pulls,
            mergeable_pulls=mergeable_pulls,
            unmergeable_pulls=unmergeable_pulls,
        )

        server_statistics_item_ghe_stats_pulls.additional_properties = d
        return server_statistics_item_ghe_stats_pulls

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
