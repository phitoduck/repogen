from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerStatisticsItemGheStatsComments")


@attr.s(auto_attribs=True)
class ServerStatisticsItemGheStatsComments:
    """
    Attributes:
        total_commit_comments (Union[Unset, int]):
        total_gist_comments (Union[Unset, int]):
        total_issue_comments (Union[Unset, int]):
        total_pull_request_comments (Union[Unset, int]):
    """

    total_commit_comments: Union[Unset, int] = UNSET
    total_gist_comments: Union[Unset, int] = UNSET
    total_issue_comments: Union[Unset, int] = UNSET
    total_pull_request_comments: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_commit_comments = self.total_commit_comments
        total_gist_comments = self.total_gist_comments
        total_issue_comments = self.total_issue_comments
        total_pull_request_comments = self.total_pull_request_comments

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_commit_comments is not UNSET:
            field_dict["total_commit_comments"] = total_commit_comments
        if total_gist_comments is not UNSET:
            field_dict["total_gist_comments"] = total_gist_comments
        if total_issue_comments is not UNSET:
            field_dict["total_issue_comments"] = total_issue_comments
        if total_pull_request_comments is not UNSET:
            field_dict["total_pull_request_comments"] = total_pull_request_comments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_commit_comments = d.pop("total_commit_comments", UNSET)

        total_gist_comments = d.pop("total_gist_comments", UNSET)

        total_issue_comments = d.pop("total_issue_comments", UNSET)

        total_pull_request_comments = d.pop("total_pull_request_comments", UNSET)

        server_statistics_item_ghe_stats_comments = cls(
            total_commit_comments=total_commit_comments,
            total_gist_comments=total_gist_comments,
            total_issue_comments=total_issue_comments,
            total_pull_request_comments=total_pull_request_comments,
        )

        server_statistics_item_ghe_stats_comments.additional_properties = d
        return server_statistics_item_ghe_stats_comments

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
