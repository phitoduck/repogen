from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..models.commit_commit_tree import CommitCommitTree
from ..models.git_user import GitUser
from ..models.verification import Verification
from ..types import UNSET, Unset

T = TypeVar("T", bound="CommitCommit")


@attr.s(auto_attribs=True)
class CommitCommit:
    """
    Attributes:
        url (str):  Example: https://api.github.com/repos/octocat/Hello-
            World/commits/6dcb09b5b57875f334f61aebed695e2e4193db5e.
        message (str):  Example: Fix all the bugs.
        comment_count (int):
        tree (CommitCommitTree):
        author (Optional[GitUser]): Metaproperties for Git author/committer information.
        committer (Optional[GitUser]): Metaproperties for Git author/committer information.
        verification (Union[Unset, Verification]):
    """

    url: str
    message: str
    comment_count: int
    tree: CommitCommitTree
    author: Optional[GitUser]
    committer: Optional[GitUser]
    verification: Union[Unset, Verification] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        message = self.message
        comment_count = self.comment_count
        tree = self.tree.to_dict()

        author = self.author.to_dict() if self.author else None

        committer = self.committer.to_dict() if self.committer else None

        verification: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.verification, Unset):
            verification = self.verification.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "message": message,
                "comment_count": comment_count,
                "tree": tree,
                "author": author,
                "committer": committer,
            }
        )
        if verification is not UNSET:
            field_dict["verification"] = verification

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        message = d.pop("message")

        comment_count = d.pop("comment_count")

        tree = CommitCommitTree.from_dict(d.pop("tree"))

        _author = d.pop("author")
        author: Optional[GitUser]
        if _author is None:
            author = None
        else:
            author = GitUser.from_dict(_author)

        _committer = d.pop("committer")
        committer: Optional[GitUser]
        if _committer is None:
            committer = None
        else:
            committer = GitUser.from_dict(_committer)

        _verification = d.pop("verification", UNSET)
        verification: Union[Unset, Verification]
        if isinstance(_verification, Unset):
            verification = UNSET
        else:
            verification = Verification.from_dict(_verification)

        commit_commit = cls(
            url=url,
            message=message,
            comment_count=comment_count,
            tree=tree,
            author=author,
            committer=committer,
            verification=verification,
        )

        commit_commit.additional_properties = d
        return commit_commit

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
