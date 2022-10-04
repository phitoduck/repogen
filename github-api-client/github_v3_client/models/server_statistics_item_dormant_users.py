from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerStatisticsItemDormantUsers")


@attr.s(auto_attribs=True)
class ServerStatisticsItemDormantUsers:
    """
    Attributes:
        total_dormant_users (Union[Unset, int]):
        dormancy_threshold (Union[Unset, str]):
    """

    total_dormant_users: Union[Unset, int] = UNSET
    dormancy_threshold: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_dormant_users = self.total_dormant_users
        dormancy_threshold = self.dormancy_threshold

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_dormant_users is not UNSET:
            field_dict["total_dormant_users"] = total_dormant_users
        if dormancy_threshold is not UNSET:
            field_dict["dormancy_threshold"] = dormancy_threshold

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_dormant_users = d.pop("total_dormant_users", UNSET)

        dormancy_threshold = d.pop("dormancy_threshold", UNSET)

        server_statistics_item_dormant_users = cls(
            total_dormant_users=total_dormant_users,
            dormancy_threshold=dormancy_threshold,
        )

        server_statistics_item_dormant_users.additional_properties = d
        return server_statistics_item_dormant_users

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
