from typing import Any, Dict, List, Optional, Type, TypeVar

import attr

from ..models.file_commit_commit import FileCommitCommit
from ..models.file_commit_content import FileCommitContent

T = TypeVar("T", bound="FileCommit")


@attr.s(auto_attribs=True)
class FileCommit:
    """File Commit

    Attributes:
        commit (FileCommitCommit):
        content (Optional[FileCommitContent]):
    """

    commit: FileCommitCommit
    content: Optional[FileCommitContent]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        commit = self.commit.to_dict()

        content = self.content.to_dict() if self.content else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "commit": commit,
                "content": content,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        commit = FileCommitCommit.from_dict(d.pop("commit"))

        _content = d.pop("content")
        content: Optional[FileCommitContent]
        if _content is None:
            content = None
        else:
            content = FileCommitContent.from_dict(_content)

        file_commit = cls(
            commit=commit,
            content=content,
        )

        file_commit.additional_properties = d
        return file_commit

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
