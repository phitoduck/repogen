from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerStatisticsItemGheStatsUsers")


@attr.s(auto_attribs=True)
class ServerStatisticsItemGheStatsUsers:
    """
    Attributes:
        total_users (Union[Unset, int]):
        admin_users (Union[Unset, int]):
        suspended_users (Union[Unset, int]):
    """

    total_users: Union[Unset, int] = UNSET
    admin_users: Union[Unset, int] = UNSET
    suspended_users: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_users = self.total_users
        admin_users = self.admin_users
        suspended_users = self.suspended_users

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_users is not UNSET:
            field_dict["total_users"] = total_users
        if admin_users is not UNSET:
            field_dict["admin_users"] = admin_users
        if suspended_users is not UNSET:
            field_dict["suspended_users"] = suspended_users

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_users = d.pop("total_users", UNSET)

        admin_users = d.pop("admin_users", UNSET)

        suspended_users = d.pop("suspended_users", UNSET)

        server_statistics_item_ghe_stats_users = cls(
            total_users=total_users,
            admin_users=admin_users,
            suspended_users=suspended_users,
        )

        server_statistics_item_ghe_stats_users.additional_properties = d
        return server_statistics_item_ghe_stats_users

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
