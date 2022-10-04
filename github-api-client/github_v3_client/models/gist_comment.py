import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.author_association import AuthorAssociation
from ..models.simple_user import SimpleUser

T = TypeVar("T", bound="GistComment")


@attr.s(auto_attribs=True)
class GistComment:
    """A comment made to a gist.

    Attributes:
        id (int):  Example: 1.
        node_id (str):  Example: MDExOkdpc3RDb21tZW50MQ==.
        url (str):  Example: https://api.github.com/gists/a6db0bec360bb87e9418/comments/1.
        body (str): The comment text. Example: Body of the attachment.
        created_at (datetime.datetime):  Example: 2011-04-18T23:23:56Z.
        updated_at (datetime.datetime):  Example: 2011-04-18T23:23:56Z.
        author_association (AuthorAssociation): How the author is associated with the repository. Example: OWNER.
        user (Optional[SimpleUser]): Simple User
    """

    id: int
    node_id: str
    url: str
    body: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    author_association: AuthorAssociation
    user: Optional[SimpleUser]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        node_id = self.node_id
        url = self.url
        body = self.body
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        author_association = self.author_association.value

        user = self.user.to_dict() if self.user else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "node_id": node_id,
                "url": url,
                "body": body,
                "created_at": created_at,
                "updated_at": updated_at,
                "author_association": author_association,
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        node_id = d.pop("node_id")

        url = d.pop("url")

        body = d.pop("body")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        author_association = AuthorAssociation(d.pop("author_association"))

        _user = d.pop("user")
        user: Optional[SimpleUser]
        if _user is None:
            user = None
        else:
            user = SimpleUser.from_dict(_user)

        gist_comment = cls(
            id=id,
            node_id=node_id,
            url=url,
            body=body,
            created_at=created_at,
            updated_at=updated_at,
            author_association=author_association,
            user=user,
        )

        gist_comment.additional_properties = d
        return gist_comment

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
