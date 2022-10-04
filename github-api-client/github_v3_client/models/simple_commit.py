import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.simple_commit_author import SimpleCommitAuthor
from ..models.simple_commit_committer import SimpleCommitCommitter

T = TypeVar("T", bound="SimpleCommit")


@attr.s(auto_attribs=True)
class SimpleCommit:
    """Simple Commit

    Attributes:
        id (str):
        tree_id (str):
        message (str):
        timestamp (datetime.datetime):
        author (Optional[SimpleCommitAuthor]):
        committer (Optional[SimpleCommitCommitter]):
    """

    id: str
    tree_id: str
    message: str
    timestamp: datetime.datetime
    author: Optional[SimpleCommitAuthor]
    committer: Optional[SimpleCommitCommitter]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        tree_id = self.tree_id
        message = self.message
        timestamp = self.timestamp.isoformat()

        author = self.author.to_dict() if self.author else None

        committer = self.committer.to_dict() if self.committer else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "tree_id": tree_id,
                "message": message,
                "timestamp": timestamp,
                "author": author,
                "committer": committer,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        tree_id = d.pop("tree_id")

        message = d.pop("message")

        timestamp = isoparse(d.pop("timestamp"))

        _author = d.pop("author")
        author: Optional[SimpleCommitAuthor]
        if _author is None:
            author = None
        else:
            author = SimpleCommitAuthor.from_dict(_author)

        _committer = d.pop("committer")
        committer: Optional[SimpleCommitCommitter]
        if _committer is None:
            committer = None
        else:
            committer = SimpleCommitCommitter.from_dict(_committer)

        simple_commit = cls(
            id=id,
            tree_id=tree_id,
            message=message,
            timestamp=timestamp,
            author=author,
            committer=committer,
        )

        simple_commit.additional_properties = d
        return simple_commit

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
