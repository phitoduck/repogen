from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.pullsmerge_json_body_merge_method import PullsmergeJsonBodyMergeMethod
from ..types import UNSET, Unset

T = TypeVar("T", bound="PullsmergeJsonBody")


@attr.s(auto_attribs=True)
class PullsmergeJsonBody:
    """
    Attributes:
        commit_title (Union[Unset, str]): Title for the automatic commit message.
        commit_message (Union[Unset, str]): Extra detail to append to automatic commit message.
        sha (Union[Unset, str]): SHA that pull request head must match to allow merge.
        merge_method (Union[Unset, PullsmergeJsonBodyMergeMethod]): Merge method to use. Possible values are `merge`,
            `squash` or `rebase`. Default is `merge`.
    """

    commit_title: Union[Unset, str] = UNSET
    commit_message: Union[Unset, str] = UNSET
    sha: Union[Unset, str] = UNSET
    merge_method: Union[Unset, PullsmergeJsonBodyMergeMethod] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        commit_title = self.commit_title
        commit_message = self.commit_message
        sha = self.sha
        merge_method: Union[Unset, str] = UNSET
        if not isinstance(self.merge_method, Unset):
            merge_method = self.merge_method.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if commit_title is not UNSET:
            field_dict["commit_title"] = commit_title
        if commit_message is not UNSET:
            field_dict["commit_message"] = commit_message
        if sha is not UNSET:
            field_dict["sha"] = sha
        if merge_method is not UNSET:
            field_dict["merge_method"] = merge_method

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        commit_title = d.pop("commit_title", UNSET)

        commit_message = d.pop("commit_message", UNSET)

        sha = d.pop("sha", UNSET)

        _merge_method = d.pop("merge_method", UNSET)
        merge_method: Union[Unset, PullsmergeJsonBodyMergeMethod]
        if isinstance(_merge_method, Unset):
            merge_method = UNSET
        else:
            merge_method = PullsmergeJsonBodyMergeMethod(_merge_method)

        pullsmerge_json_body = cls(
            commit_title=commit_title,
            commit_message=commit_message,
            sha=sha,
            merge_method=merge_method,
        )

        pullsmerge_json_body.additional_properties = d
        return pullsmerge_json_body

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
