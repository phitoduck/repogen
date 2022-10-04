from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerStatisticsItemGheStatsMilestones")


@attr.s(auto_attribs=True)
class ServerStatisticsItemGheStatsMilestones:
    """
    Attributes:
        total_milestones (Union[Unset, int]):
        open_milestones (Union[Unset, int]):
        closed_milestones (Union[Unset, int]):
    """

    total_milestones: Union[Unset, int] = UNSET
    open_milestones: Union[Unset, int] = UNSET
    closed_milestones: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_milestones = self.total_milestones
        open_milestones = self.open_milestones
        closed_milestones = self.closed_milestones

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_milestones is not UNSET:
            field_dict["total_milestones"] = total_milestones
        if open_milestones is not UNSET:
            field_dict["open_milestones"] = open_milestones
        if closed_milestones is not UNSET:
            field_dict["closed_milestones"] = closed_milestones

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_milestones = d.pop("total_milestones", UNSET)

        open_milestones = d.pop("open_milestones", UNSET)

        closed_milestones = d.pop("closed_milestones", UNSET)

        server_statistics_item_ghe_stats_milestones = cls(
            total_milestones=total_milestones,
            open_milestones=open_milestones,
            closed_milestones=closed_milestones,
        )

        server_statistics_item_ghe_stats_milestones.additional_properties = d
        return server_statistics_item_ghe_stats_milestones

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
