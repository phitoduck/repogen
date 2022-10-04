from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerStatisticsItemGheStatsHooks")


@attr.s(auto_attribs=True)
class ServerStatisticsItemGheStatsHooks:
    """
    Attributes:
        total_hooks (Union[Unset, int]):
        active_hooks (Union[Unset, int]):
        inactive_hooks (Union[Unset, int]):
    """

    total_hooks: Union[Unset, int] = UNSET
    active_hooks: Union[Unset, int] = UNSET
    inactive_hooks: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_hooks = self.total_hooks
        active_hooks = self.active_hooks
        inactive_hooks = self.inactive_hooks

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_hooks is not UNSET:
            field_dict["total_hooks"] = total_hooks
        if active_hooks is not UNSET:
            field_dict["active_hooks"] = active_hooks
        if inactive_hooks is not UNSET:
            field_dict["inactive_hooks"] = inactive_hooks

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_hooks = d.pop("total_hooks", UNSET)

        active_hooks = d.pop("active_hooks", UNSET)

        inactive_hooks = d.pop("inactive_hooks", UNSET)

        server_statistics_item_ghe_stats_hooks = cls(
            total_hooks=total_hooks,
            active_hooks=active_hooks,
            inactive_hooks=inactive_hooks,
        )

        server_statistics_item_ghe_stats_hooks.additional_properties = d
        return server_statistics_item_ghe_stats_hooks

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
