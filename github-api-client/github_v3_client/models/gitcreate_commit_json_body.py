from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.gitcreate_commit_json_body_author import GitcreateCommitJsonBodyAuthor
from ..models.gitcreate_commit_json_body_committer import GitcreateCommitJsonBodyCommitter
from ..types import UNSET, Unset

T = TypeVar("T", bound="GitcreateCommitJsonBody")


@attr.s(auto_attribs=True)
class GitcreateCommitJsonBody:
    """
    Attributes:
        message (str): The commit message
        tree (str): The SHA of the tree object this commit points to
        parents (Union[Unset, List[str]]): The SHAs of the commits that were the parents of this commit. If omitted or
            empty, the commit will be written as a root commit. For a single parent, an array of one SHA should be provided;
            for a merge commit, an array of more than one should be provided.
        author (Union[Unset, GitcreateCommitJsonBodyAuthor]): Information about the author of the commit. By default,
            the `author` will be the authenticated user and the current date. See the `author` and `committer` object below
            for details.
        committer (Union[Unset, GitcreateCommitJsonBodyCommitter]): Information about the person who is making the
            commit. By default, `committer` will use the information set in `author`. See the `author` and `committer`
            object below for details.
        signature (Union[Unset, str]): The [PGP signature](https://en.wikipedia.org/wiki/Pretty_Good_Privacy) of the
            commit. GitHub adds the signature to the `gpgsig` header of the created commit. For a commit signature to be
            verifiable by Git or GitHub, it must be an ASCII-armored detached PGP signature over the string commit as it
            would be written to the object database. To pass a `signature` parameter, you need to first manually create a
            valid PGP signature, which can be complicated. You may find it easier to [use the command line](https://git-
            scm.com/book/id/v2/Git-Tools-Signing-Your-Work) to create signed commits.
    """

    message: str
    tree: str
    parents: Union[Unset, List[str]] = UNSET
    author: Union[Unset, GitcreateCommitJsonBodyAuthor] = UNSET
    committer: Union[Unset, GitcreateCommitJsonBodyCommitter] = UNSET
    signature: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message
        tree = self.tree
        parents: Union[Unset, List[str]] = UNSET
        if not isinstance(self.parents, Unset):
            parents = self.parents

        author: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        committer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.committer, Unset):
            committer = self.committer.to_dict()

        signature = self.signature

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "tree": tree,
            }
        )
        if parents is not UNSET:
            field_dict["parents"] = parents
        if author is not UNSET:
            field_dict["author"] = author
        if committer is not UNSET:
            field_dict["committer"] = committer
        if signature is not UNSET:
            field_dict["signature"] = signature

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        message = d.pop("message")

        tree = d.pop("tree")

        parents = cast(List[str], d.pop("parents", UNSET))

        _author = d.pop("author", UNSET)
        author: Union[Unset, GitcreateCommitJsonBodyAuthor]
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = GitcreateCommitJsonBodyAuthor.from_dict(_author)

        _committer = d.pop("committer", UNSET)
        committer: Union[Unset, GitcreateCommitJsonBodyCommitter]
        if isinstance(_committer, Unset):
            committer = UNSET
        else:
            committer = GitcreateCommitJsonBodyCommitter.from_dict(_committer)

        signature = d.pop("signature", UNSET)

        gitcreate_commit_json_body = cls(
            message=message,
            tree=tree,
            parents=parents,
            author=author,
            committer=committer,
            signature=signature,
        )

        gitcreate_commit_json_body.additional_properties = d
        return gitcreate_commit_json_body

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
