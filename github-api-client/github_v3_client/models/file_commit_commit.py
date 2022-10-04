from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.file_commit_commit_author import FileCommitCommitAuthor
from ..models.file_commit_commit_committer import FileCommitCommitCommitter
from ..models.file_commit_commit_parents_item import FileCommitCommitParentsItem
from ..models.file_commit_commit_tree import FileCommitCommitTree
from ..models.file_commit_commit_verification import FileCommitCommitVerification
from ..types import UNSET, Unset

T = TypeVar("T", bound="FileCommitCommit")


@attr.s(auto_attribs=True)
class FileCommitCommit:
    """
    Attributes:
        sha (Union[Unset, str]):
        node_id (Union[Unset, str]):
        url (Union[Unset, str]):
        html_url (Union[Unset, str]):
        author (Union[Unset, FileCommitCommitAuthor]):
        committer (Union[Unset, FileCommitCommitCommitter]):
        message (Union[Unset, str]):
        tree (Union[Unset, FileCommitCommitTree]):
        parents (Union[Unset, List[FileCommitCommitParentsItem]]):
        verification (Union[Unset, FileCommitCommitVerification]):
    """

    sha: Union[Unset, str] = UNSET
    node_id: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    html_url: Union[Unset, str] = UNSET
    author: Union[Unset, FileCommitCommitAuthor] = UNSET
    committer: Union[Unset, FileCommitCommitCommitter] = UNSET
    message: Union[Unset, str] = UNSET
    tree: Union[Unset, FileCommitCommitTree] = UNSET
    parents: Union[Unset, List[FileCommitCommitParentsItem]] = UNSET
    verification: Union[Unset, FileCommitCommitVerification] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sha = self.sha
        node_id = self.node_id
        url = self.url
        html_url = self.html_url
        author: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        committer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.committer, Unset):
            committer = self.committer.to_dict()

        message = self.message
        tree: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tree, Unset):
            tree = self.tree.to_dict()

        parents: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.parents, Unset):
            parents = []
            for parents_item_data in self.parents:
                parents_item = parents_item_data.to_dict()

                parents.append(parents_item)

        verification: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.verification, Unset):
            verification = self.verification.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sha is not UNSET:
            field_dict["sha"] = sha
        if node_id is not UNSET:
            field_dict["node_id"] = node_id
        if url is not UNSET:
            field_dict["url"] = url
        if html_url is not UNSET:
            field_dict["html_url"] = html_url
        if author is not UNSET:
            field_dict["author"] = author
        if committer is not UNSET:
            field_dict["committer"] = committer
        if message is not UNSET:
            field_dict["message"] = message
        if tree is not UNSET:
            field_dict["tree"] = tree
        if parents is not UNSET:
            field_dict["parents"] = parents
        if verification is not UNSET:
            field_dict["verification"] = verification

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sha = d.pop("sha", UNSET)

        node_id = d.pop("node_id", UNSET)

        url = d.pop("url", UNSET)

        html_url = d.pop("html_url", UNSET)

        _author = d.pop("author", UNSET)
        author: Union[Unset, FileCommitCommitAuthor]
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = FileCommitCommitAuthor.from_dict(_author)

        _committer = d.pop("committer", UNSET)
        committer: Union[Unset, FileCommitCommitCommitter]
        if isinstance(_committer, Unset):
            committer = UNSET
        else:
            committer = FileCommitCommitCommitter.from_dict(_committer)

        message = d.pop("message", UNSET)

        _tree = d.pop("tree", UNSET)
        tree: Union[Unset, FileCommitCommitTree]
        if isinstance(_tree, Unset):
            tree = UNSET
        else:
            tree = FileCommitCommitTree.from_dict(_tree)

        parents = []
        _parents = d.pop("parents", UNSET)
        for parents_item_data in _parents or []:
            parents_item = FileCommitCommitParentsItem.from_dict(parents_item_data)

            parents.append(parents_item)

        _verification = d.pop("verification", UNSET)
        verification: Union[Unset, FileCommitCommitVerification]
        if isinstance(_verification, Unset):
            verification = UNSET
        else:
            verification = FileCommitCommitVerification.from_dict(_verification)

        file_commit_commit = cls(
            sha=sha,
            node_id=node_id,
            url=url,
            html_url=html_url,
            author=author,
            committer=committer,
            message=message,
            tree=tree,
            parents=parents,
            verification=verification,
        )

        file_commit_commit.additional_properties = d
        return file_commit_commit

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
