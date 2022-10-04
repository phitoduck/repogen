from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerStatisticsItemGheStatsIssues")


@attr.s(auto_attribs=True)
class ServerStatisticsItemGheStatsIssues:
    """
    Attributes:
        total_issues (Union[Unset, int]):
        open_issues (Union[Unset, int]):
        closed_issues (Union[Unset, int]):
    """

    total_issues: Union[Unset, int] = UNSET
    open_issues: Union[Unset, int] = UNSET
    closed_issues: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_issues = self.total_issues
        open_issues = self.open_issues
        closed_issues = self.closed_issues

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_issues is not UNSET:
            field_dict["total_issues"] = total_issues
        if open_issues is not UNSET:
            field_dict["open_issues"] = open_issues
        if closed_issues is not UNSET:
            field_dict["closed_issues"] = closed_issues

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_issues = d.pop("total_issues", UNSET)

        open_issues = d.pop("open_issues", UNSET)

        closed_issues = d.pop("closed_issues", UNSET)

        server_statistics_item_ghe_stats_issues = cls(
            total_issues=total_issues,
            open_issues=open_issues,
            closed_issues=closed_issues,
        )

        server_statistics_item_ghe_stats_issues.additional_properties = d
        return server_statistics_item_ghe_stats_issues

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
