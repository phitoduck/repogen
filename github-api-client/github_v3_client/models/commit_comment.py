import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.author_association import AuthorAssociation
from ..models.reaction_rollup import ReactionRollup
from ..models.simple_user import SimpleUser
from ..types import UNSET, Unset

T = TypeVar("T", bound="CommitComment")


@attr.s(auto_attribs=True)
class CommitComment:
    """Commit Comment

    Attributes:
        html_url (str):
        url (str):
        id (int):
        node_id (str):
        body (str):
        commit_id (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        author_association (AuthorAssociation): How the author is associated with the repository. Example: OWNER.
        path (Optional[str]):
        position (Optional[int]):
        line (Optional[int]):
        user (Optional[SimpleUser]): Simple User
        reactions (Union[Unset, ReactionRollup]):
    """

    html_url: str
    url: str
    id: int
    node_id: str
    body: str
    commit_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    author_association: AuthorAssociation
    path: Optional[str]
    position: Optional[int]
    line: Optional[int]
    user: Optional[SimpleUser]
    reactions: Union[Unset, ReactionRollup] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        html_url = self.html_url
        url = self.url
        id = self.id
        node_id = self.node_id
        body = self.body
        commit_id = self.commit_id
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        author_association = self.author_association.value

        path = self.path
        position = self.position
        line = self.line
        user = self.user.to_dict() if self.user else None

        reactions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reactions, Unset):
            reactions = self.reactions.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "html_url": html_url,
                "url": url,
                "id": id,
                "node_id": node_id,
                "body": body,
                "commit_id": commit_id,
                "created_at": created_at,
                "updated_at": updated_at,
                "author_association": author_association,
                "path": path,
                "position": position,
                "line": line,
                "user": user,
            }
        )
        if reactions is not UNSET:
            field_dict["reactions"] = reactions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        html_url = d.pop("html_url")

        url = d.pop("url")

        id = d.pop("id")

        node_id = d.pop("node_id")

        body = d.pop("body")

        commit_id = d.pop("commit_id")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        author_association = AuthorAssociation(d.pop("author_association"))

        path = d.pop("path")

        position = d.pop("position")

        line = d.pop("line")

        _user = d.pop("user")
        user: Optional[SimpleUser]
        if _user is None:
            user = None
        else:
            user = SimpleUser.from_dict(_user)

        _reactions = d.pop("reactions", UNSET)
        reactions: Union[Unset, ReactionRollup]
        if isinstance(_reactions, Unset):
            reactions = UNSET
        else:
            reactions = ReactionRollup.from_dict(_reactions)

        commit_comment = cls(
            html_url=html_url,
            url=url,
            id=id,
            node_id=node_id,
            body=body,
            commit_id=commit_id,
            created_at=created_at,
            updated_at=updated_at,
            author_association=author_association,
            path=path,
            position=position,
            line=line,
            user=user,
            reactions=reactions,
        )

        commit_comment.additional_properties = d
        return commit_comment

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
