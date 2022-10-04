from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.reposcreate_or_update_file_contents_json_body_author import ReposcreateOrUpdateFileContentsJsonBodyAuthor
from ..models.reposcreate_or_update_file_contents_json_body_committer import (
    ReposcreateOrUpdateFileContentsJsonBodyCommitter,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReposcreateOrUpdateFileContentsJsonBody")


@attr.s(auto_attribs=True)
class ReposcreateOrUpdateFileContentsJsonBody:
    """
    Attributes:
        message (str): The commit message.
        content (str): The new file content, using Base64 encoding.
        sha (Union[Unset, str]): **Required if you are updating a file**. The blob SHA of the file being replaced.
        branch (Union[Unset, str]): The branch name. Default: the repository’s default branch (usually `master`)
        committer (Union[Unset, ReposcreateOrUpdateFileContentsJsonBodyCommitter]): The person that committed the file.
            Default: the authenticated user.
        author (Union[Unset, ReposcreateOrUpdateFileContentsJsonBodyAuthor]): The author of the file. Default: The
            `committer` or the authenticated user if you omit `committer`.
    """

    message: str
    content: str
    sha: Union[Unset, str] = UNSET
    branch: Union[Unset, str] = UNSET
    committer: Union[Unset, ReposcreateOrUpdateFileContentsJsonBodyCommitter] = UNSET
    author: Union[Unset, ReposcreateOrUpdateFileContentsJsonBodyAuthor] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message
        content = self.content
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
                "content": content,
            }
        )
        if sha is not UNSET:
            field_dict["sha"] = sha
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

        content = d.pop("content")

        sha = d.pop("sha", UNSET)

        branch = d.pop("branch", UNSET)

        _committer = d.pop("committer", UNSET)
        committer: Union[Unset, ReposcreateOrUpdateFileContentsJsonBodyCommitter]
        if isinstance(_committer, Unset):
            committer = UNSET
        else:
            committer = ReposcreateOrUpdateFileContentsJsonBodyCommitter.from_dict(_committer)

        _author = d.pop("author", UNSET)
        author: Union[Unset, ReposcreateOrUpdateFileContentsJsonBodyAuthor]
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = ReposcreateOrUpdateFileContentsJsonBodyAuthor.from_dict(_author)

        reposcreate_or_update_file_contents_json_body = cls(
            message=message,
            content=content,
            sha=sha,
            branch=branch,
            committer=committer,
            author=author,
        )

        reposcreate_or_update_file_contents_json_body.additional_properties = d
        return reposcreate_or_update_file_contents_json_body

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
