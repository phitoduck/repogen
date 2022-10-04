from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerStatisticsItemGithubConnect")


@attr.s(auto_attribs=True)
class ServerStatisticsItemGithubConnect:
    """
    Attributes:
        features_enabled (Union[Unset, List[str]]):
    """

    features_enabled: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        features_enabled: Union[Unset, List[str]] = UNSET
        if not isinstance(self.features_enabled, Unset):
            features_enabled = self.features_enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if features_enabled is not UNSET:
            field_dict["features_enabled"] = features_enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        features_enabled = cast(List[str], d.pop("features_enabled", UNSET))

        server_statistics_item_github_connect = cls(
            features_enabled=features_enabled,
        )

        server_statistics_item_github_connect.additional_properties = d
        return server_statistics_item_github_connect

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
