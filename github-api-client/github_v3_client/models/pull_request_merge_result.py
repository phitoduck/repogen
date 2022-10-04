from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PullRequestMergeResult")


@attr.s(auto_attribs=True)
class PullRequestMergeResult:
    """Pull Request Merge Result

    Attributes:
        sha (str):
        merged (bool):
        message (str):
    """

    sha: str
    merged: bool
    message: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sha = self.sha
        merged = self.merged
        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sha": sha,
                "merged": merged,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sha = d.pop("sha")

        merged = d.pop("merged")

        message = d.pop("message")

        pull_request_merge_result = cls(
            sha=sha,
            merged=merged,
            message=message,
        )

        pull_request_merge_result.additional_properties = d
        return pull_request_merge_result

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
