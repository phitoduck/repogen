import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.reaction_content import ReactionContent
from ..models.simple_user import SimpleUser

T = TypeVar("T", bound="Reaction")


@attr.s(auto_attribs=True)
class Reaction:
    """Reactions to conversations provide a way to help people express their feelings more simply and effectively.

    Attributes:
        id (int):  Example: 1.
        node_id (str):  Example: MDg6UmVhY3Rpb24x.
        content (ReactionContent): The reaction to use Example: heart.
        created_at (datetime.datetime):  Example: 2016-05-20T20:09:31Z.
        user (Optional[SimpleUser]): Simple User
    """

    id: int
    node_id: str
    content: ReactionContent
    created_at: datetime.datetime
    user: Optional[SimpleUser]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        node_id = self.node_id
        content = self.content.value

        created_at = self.created_at.isoformat()

        user = self.user.to_dict() if self.user else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "node_id": node_id,
                "content": content,
                "created_at": created_at,
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        node_id = d.pop("node_id")

        content = ReactionContent(d.pop("content"))

        created_at = isoparse(d.pop("created_at"))

        _user = d.pop("user")
        user: Optional[SimpleUser]
        if _user is None:
            user = None
        else:
            user = SimpleUser.from_dict(_user)

        reaction = cls(
            id=id,
            node_id=node_id,
            content=content,
            created_at=created_at,
            user=user,
        )

        reaction.additional_properties = d
        return reaction

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
