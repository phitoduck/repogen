from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.git_commit_author import GitCommitAuthor
from ..models.git_commit_committer import GitCommitCommitter
from ..models.git_commit_parents_item import GitCommitParentsItem
from ..models.git_commit_tree import GitCommitTree
from ..models.git_commit_verification import GitCommitVerification

T = TypeVar("T", bound="GitCommit")


@attr.s(auto_attribs=True)
class GitCommit:
    """Low-level Git commit operations within a repository

    Attributes:
        sha (str): SHA for the commit Example: 7638417db6d59f3c431d3e1f261cc637155684cd.
        node_id (str):
        url (str):
        author (GitCommitAuthor): Identifying information for the git-user
        committer (GitCommitCommitter): Identifying information for the git-user
        message (str): Message describing the purpose of the commit Example: Fix #42.
        tree (GitCommitTree):
        parents (List[GitCommitParentsItem]):
        verification (GitCommitVerification):
        html_url (str):
    """

    sha: str
    node_id: str
    url: str
    author: GitCommitAuthor
    committer: GitCommitCommitter
    message: str
    tree: GitCommitTree
    parents: List[GitCommitParentsItem]
    verification: GitCommitVerification
    html_url: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sha = self.sha
        node_id = self.node_id
        url = self.url
        author = self.author.to_dict()

        committer = self.committer.to_dict()

        message = self.message
        tree = self.tree.to_dict()

        parents = []
        for parents_item_data in self.parents:
            parents_item = parents_item_data.to_dict()

            parents.append(parents_item)

        verification = self.verification.to_dict()

        html_url = self.html_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sha": sha,
                "node_id": node_id,
                "url": url,
                "author": author,
                "committer": committer,
                "message": message,
                "tree": tree,
                "parents": parents,
                "verification": verification,
                "html_url": html_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sha = d.pop("sha")

        node_id = d.pop("node_id")

        url = d.pop("url")

        author = GitCommitAuthor.from_dict(d.pop("author"))

        committer = GitCommitCommitter.from_dict(d.pop("committer"))

        message = d.pop("message")

        tree = GitCommitTree.from_dict(d.pop("tree"))

        parents = []
        _parents = d.pop("parents")
        for parents_item_data in _parents:
            parents_item = GitCommitParentsItem.from_dict(parents_item_data)

            parents.append(parents_item)

        verification = GitCommitVerification.from_dict(d.pop("verification"))

        html_url = d.pop("html_url")

        git_commit = cls(
            sha=sha,
            node_id=node_id,
            url=url,
            author=author,
            committer=committer,
            message=message,
            tree=tree,
            parents=parents,
            verification=verification,
            html_url=html_url,
        )

        git_commit.additional_properties = d
        return git_commit

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
