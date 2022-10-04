from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerStatisticsItemGheStatsGists")


@attr.s(auto_attribs=True)
class ServerStatisticsItemGheStatsGists:
    """
    Attributes:
        total_gists (Union[Unset, int]):
        private_gists (Union[Unset, int]):
        public_gists (Union[Unset, int]):
    """

    total_gists: Union[Unset, int] = UNSET
    private_gists: Union[Unset, int] = UNSET
    public_gists: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_gists = self.total_gists
        private_gists = self.private_gists
        public_gists = self.public_gists

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_gists is not UNSET:
            field_dict["total_gists"] = total_gists
        if private_gists is not UNSET:
            field_dict["private_gists"] = private_gists
        if public_gists is not UNSET:
            field_dict["public_gists"] = public_gists

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_gists = d.pop("total_gists", UNSET)

        private_gists = d.pop("private_gists", UNSET)

        public_gists = d.pop("public_gists", UNSET)

        server_statistics_item_ghe_stats_gists = cls(
            total_gists=total_gists,
            private_gists=private_gists,
            public_gists=public_gists,
        )

        server_statistics_item_ghe_stats_gists.additional_properties = d
        return server_statistics_item_ghe_stats_gists

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
