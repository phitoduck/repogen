from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..models.commit_commit import CommitCommit
from ..models.commit_parents_item import CommitParentsItem
from ..models.commit_stats import CommitStats
from ..models.diff_entry import DiffEntry
from ..models.simple_user import SimpleUser
from ..types import UNSET, Unset

T = TypeVar("T", bound="Commit")


@attr.s(auto_attribs=True)
class Commit:
    """Commit

    Attributes:
        url (str):  Example: https://api.github.com/repos/octocat/Hello-
            World/commits/6dcb09b5b57875f334f61aebed695e2e4193db5e.
        sha (str):  Example: 6dcb09b5b57875f334f61aebed695e2e4193db5e.
        node_id (str):  Example: MDY6Q29tbWl0NmRjYjA5YjViNTc4NzVmMzM0ZjYxYWViZWQ2OTVlMmU0MTkzZGI1ZQ==.
        html_url (str):  Example: https://github.com/octocat/Hello-
            World/commit/6dcb09b5b57875f334f61aebed695e2e4193db5e.
        comments_url (str):  Example: https://api.github.com/repos/octocat/Hello-
            World/commits/6dcb09b5b57875f334f61aebed695e2e4193db5e/comments.
        commit (CommitCommit):
        parents (List[CommitParentsItem]):
        author (Optional[SimpleUser]): Simple User
        committer (Optional[SimpleUser]): Simple User
        stats (Union[Unset, CommitStats]):
        files (Union[Unset, List[DiffEntry]]):
    """

    url: str
    sha: str
    node_id: str
    html_url: str
    comments_url: str
    commit: CommitCommit
    parents: List[CommitParentsItem]
    author: Optional[SimpleUser]
    committer: Optional[SimpleUser]
    stats: Union[Unset, CommitStats] = UNSET
    files: Union[Unset, List[DiffEntry]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        sha = self.sha
        node_id = self.node_id
        html_url = self.html_url
        comments_url = self.comments_url
        commit = self.commit.to_dict()

        parents = []
        for parents_item_data in self.parents:
            parents_item = parents_item_data.to_dict()

            parents.append(parents_item)

        author = self.author.to_dict() if self.author else None

        committer = self.committer.to_dict() if self.committer else None

        stats: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

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
                "sha": sha,
                "node_id": node_id,
                "html_url": html_url,
                "comments_url": comments_url,
                "commit": commit,
                "parents": parents,
                "author": author,
                "committer": committer,
            }
        )
        if stats is not UNSET:
            field_dict["stats"] = stats
        if files is not UNSET:
            field_dict["files"] = files

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        sha = d.pop("sha")

        node_id = d.pop("node_id")

        html_url = d.pop("html_url")

        comments_url = d.pop("comments_url")

        commit = CommitCommit.from_dict(d.pop("commit"))

        parents = []
        _parents = d.pop("parents")
        for parents_item_data in _parents:
            parents_item = CommitParentsItem.from_dict(parents_item_data)

            parents.append(parents_item)

        _author = d.pop("author")
        author: Optional[SimpleUser]
        if _author is None:
            author = None
        else:
            author = SimpleUser.from_dict(_author)

        _committer = d.pop("committer")
        committer: Optional[SimpleUser]
        if _committer is None:
            committer = None
        else:
            committer = SimpleUser.from_dict(_committer)

        _stats = d.pop("stats", UNSET)
        stats: Union[Unset, CommitStats]
        if isinstance(_stats, Unset):
            stats = UNSET
        else:
            stats = CommitStats.from_dict(_stats)

        files = []
        _files = d.pop("files", UNSET)
        for files_item_data in _files or []:
            files_item = DiffEntry.from_dict(files_item_data)

            files.append(files_item)

        commit = cls(
            url=url,
            sha=sha,
            node_id=node_id,
            html_url=html_url,
            comments_url=comments_url,
            commit=commit,
            parents=parents,
            author=author,
            committer=committer,
            stats=stats,
            files=files,
        )

        commit.additional_properties = d
        return commit

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
