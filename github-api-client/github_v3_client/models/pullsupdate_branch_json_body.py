from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PullsupdateBranchJsonBody")


@attr.s(auto_attribs=True)
class PullsupdateBranchJsonBody:
    """
    Attributes:
        expected_head_sha (Union[Unset, str]): The expected SHA of the pull request's HEAD ref. This is the most recent
            commit on the pull request's branch. If the expected SHA does not match the pull request's HEAD, you will
            receive a `422 Unprocessable Entity` status. You can use the "[List
            commits](https://docs.github.com/rest/reference/repos#list-commits)" endpoint to find the most recent commit
            SHA. Default: SHA of the pull request's current HEAD ref.
    """

    expected_head_sha: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        expected_head_sha = self.expected_head_sha

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expected_head_sha is not UNSET:
            field_dict["expected_head_sha"] = expected_head_sha

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        expected_head_sha = d.pop("expected_head_sha", UNSET)

        pullsupdate_branch_json_body = cls(
            expected_head_sha=expected_head_sha,
        )

        pullsupdate_branch_json_body.additional_properties = d
        return pullsupdate_branch_json_body

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
