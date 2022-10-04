from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.commit import Commit
from ..models.commit_comparison_status import CommitComparisonStatus
from ..models.diff_entry import DiffEntry
from ..types import UNSET, Unset

T = TypeVar("T", bound="CommitComparison")


@attr.s(auto_attribs=True)
class CommitComparison:
    """Commit Comparison

    Attributes:
        url (str):  Example: https://api.github.com/repos/octocat/Hello-World/compare/master...topic.
        html_url (str):  Example: https://github.com/octocat/Hello-World/compare/master...topic.
        permalink_url (str):  Example: https://github.com/octocat/Hello-World/compare/octocat:bbcd538c8e72b8c175046e27cc
            8f907076331401...octocat:0328041d1152db8ae77652d1618a02e57f745f17.
        diff_url (str):  Example: https://github.com/octocat/Hello-World/compare/master...topic.diff.
        patch_url (str):  Example: https://github.com/octocat/Hello-World/compare/master...topic.patch.
        base_commit (Commit): Commit
        merge_base_commit (Commit): Commit
        status (CommitComparisonStatus):  Example: ahead.
        ahead_by (int):  Example: 4.
        behind_by (int):  Example: 5.
        total_commits (int):  Example: 6.
        commits (List[Commit]):
        files (Union[Unset, List[DiffEntry]]):
    """

    url: str
    html_url: str
    permalink_url: str
    diff_url: str
    patch_url: str
    base_commit: Commit
    merge_base_commit: Commit
    status: CommitComparisonStatus
    ahead_by: int
    behind_by: int
    total_commits: int
    commits: List[Commit]
    files: Union[Unset, List[DiffEntry]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        html_url = self.html_url
        permalink_url = self.permalink_url
        diff_url = self.diff_url
        patch_url = self.patch_url
        base_commit = self.base_commit.to_dict()

        merge_base_commit = self.merge_base_commit.to_dict()

        status = self.status.value

        ahead_by = self.ahead_by
        behind_by = self.behind_by
        total_commits = self.total_commits
        commits = []
        for commits_item_data in self.commits:
            commits_item = commits_item_data.to_dict()

            commits.append(commits_item)

        files: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()

                files.append(files_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "html_url": html_url,
                "permalink_url": permalink_url,
                "diff_url": diff_url,
                "patch_url": patch_url,
                "base_commit": base_commit,
                "merge_base_commit": merge_base_commit,
                "status": status,
                "ahead_by": ahead_by,
                "behind_by": behind_by,
                "total_commits": total_commits,
                "commits": commits,
            }
        )
        if files is not UNSET:
            field_dict["files"] = files

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        html_url = d.pop("html_url")

        permalink_url = d.pop("permalink_url")

        diff_url = d.pop("diff_url")

        patch_url = d.pop("patch_url")

        base_commit = Commit.from_dict(d.pop("base_commit"))

        merge_base_commit = Commit.from_dict(d.pop("merge_base_commit"))

        status = CommitComparisonStatus(d.pop("status"))

        ahead_by = d.pop("ahead_by")

        behind_by = d.pop("behind_by")

        total_commits = d.pop("total_commits")

        commits = []
        _commits = d.pop("commits")
        for commits_item_data in _commits:
            commits_item = Commit.from_dict(commits_item_data)

            commits.append(commits_item)

        files = []
        _files = d.pop("files", UNSET)
        for files_item_data in _files or []:
            files_item = DiffEntry.from_dict(files_item_data)

            files.append(files_item)

        commit_comparison = cls(
            url=url,
            html_url=html_url,
            permalink_url=permalink_url,
            diff_url=diff_url,
            patch_url=patch_url,
            base_commit=base_commit,
            merge_base_commit=merge_base_commit,
            status=status,
            ahead_by=ahead_by,
            behind_by=behind_by,
            total_commits=total_commits,
            commits=commits,
            files=files,
        )

        commit_comparison.additional_properties = d
        return commit_comparison

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
