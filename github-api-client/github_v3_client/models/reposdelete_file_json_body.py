from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.reposdelete_file_json_body_author import ReposdeleteFileJsonBodyAuthor
from ..models.reposdelete_file_json_body_committer import ReposdeleteFileJsonBodyCommitter
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReposdeleteFileJsonBody")


@attr.s(auto_attribs=True)
class ReposdeleteFileJsonBody:
    """
    Attributes:
        message (str): The commit message.
        sha (str): The blob SHA of the file being deleted.
        branch (Union[Unset, str]): The branch name. Default: the repository’s default branch (usually `master`)
        committer (Union[Unset, ReposdeleteFileJsonBodyCommitter]): object containing information about the committer.
        author (Union[Unset, ReposdeleteFileJsonBodyAuthor]): object containing information about the author.
    """

    message: str
    sha: str
    branch: Union[Unset, str] = UNSET
    committer: Union[Unset, ReposdeleteFileJsonBodyCommitter] = UNSET
    author: Union[Unset, ReposdeleteFileJsonBodyAuthor] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message
        sha = self.sha
        branch = self.branch
        committer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.committer, Unset):
            committer = self.committer.to_dict()

        author: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "sha": sha,
            }
        )
        if branch is not UNSET:
            field_dict["branch"] = branch
        if committer is not UNSET:
            field_dict["committer"] = committer
        if author is not UNSET:
            field_dict["author"] = author

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        message = d.pop("message")

        sha = d.pop("sha")

        branch = d.pop("branch", UNSET)

        _committer = d.pop("committer", UNSET)
        committer: Union[Unset, ReposdeleteFileJsonBodyCommitter]
        if isinstance(_committer, Unset):
            committer = UNSET
        else:
            committer = ReposdeleteFileJsonBodyCommitter.from_dict(_committer)

        _author = d.pop("author", UNSET)
        author: Union[Unset, ReposdeleteFileJsonBodyAuthor]
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = ReposdeleteFileJsonBodyAuthor.from_dict(_author)

        reposdelete_file_json_body = cls(
            message=message,
            sha=sha,
            branch=branch,
            committer=committer,
            author=author,
        )

        reposdelete_file_json_body.additional_properties = d
        return reposdelete_file_json_body

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
