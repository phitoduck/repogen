from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.pull_request_minimal_head_repo import PullRequestMinimalHeadRepo

T = TypeVar("T", bound="PullRequestMinimalHead")


@attr.s(auto_attribs=True)
class PullRequestMinimalHead:
    """
    Attributes:
        ref (str):
        sha (str):
        repo (PullRequestMinimalHeadRepo):
    """

    ref: str
    sha: str
    repo: PullRequestMinimalHeadRepo
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ref = self.ref
        sha = self.sha
        repo = self.repo.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ref": ref,
                "sha": sha,
                "repo": repo,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ref = d.pop("ref")

        sha = d.pop("sha")

        repo = PullRequestMinimalHeadRepo.from_dict(d.pop("repo"))

        pull_request_minimal_head = cls(
            ref=ref,
            sha=sha,
            repo=repo,
        )

        pull_request_minimal_head.additional_properties = d
        return pull_request_minimal_head

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
