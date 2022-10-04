from typing import Any, Dict, List, Optional, Type, TypeVar

import attr

from ..models.simple_user import SimpleUser

T = TypeVar("T", bound="Status")


@attr.s(auto_attribs=True)
class Status:
    """The status of a commit.

    Attributes:
        url (str):
        id (int):
        node_id (str):
        state (str):
        context (str):
        created_at (str):
        updated_at (str):
        avatar_url (Optional[str]):
        description (Optional[str]):
        target_url (Optional[str]):
        creator (Optional[SimpleUser]): Simple User
    """

    url: str
    id: int
    node_id: str
    state: str
    context: str
    created_at: str
    updated_at: str
    avatar_url: Optional[str]
    description: Optional[str]
    target_url: Optional[str]
    creator: Optional[SimpleUser]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        node_id = self.node_id
        state = self.state
        context = self.context
        created_at = self.created_at
        updated_at = self.updated_at
        avatar_url = self.avatar_url
        description = self.description
        target_url = self.target_url
        creator = self.creator.to_dict() if self.creator else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "id": id,
                "node_id": node_id,
                "state": state,
                "context": context,
                "created_at": created_at,
                "updated_at": updated_at,
                "avatar_url": avatar_url,
                "description": description,
                "target_url": target_url,
                "creator": creator,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        id = d.pop("id")

        node_id = d.pop("node_id")

        state = d.pop("state")

        context = d.pop("context")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        avatar_url = d.pop("avatar_url")

        description = d.pop("description")

        target_url = d.pop("target_url")

        _creator = d.pop("creator")
        creator: Optional[SimpleUser]
        if _creator is None:
            creator = None
        else:
            creator = SimpleUser.from_dict(_creator)

        status = cls(
            url=url,
            id=id,
            node_id=node_id,
            state=state,
            context=context,
            created_at=created_at,
            updated_at=updated_at,
            avatar_url=avatar_url,
            description=description,
            target_url=target_url,
            creator=creator,
        )

        status.additional_properties = d
        return status

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
