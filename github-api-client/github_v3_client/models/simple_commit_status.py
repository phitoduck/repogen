import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SimpleCommitStatus")


@attr.s(auto_attribs=True)
class SimpleCommitStatus:
    """
    Attributes:
        id (int):
        node_id (str):
        state (str):
        context (str):
        url (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        description (Optional[str]):
        target_url (Optional[str]):
        required (Union[Unset, None, bool]):
        avatar_url (Optional[str]):
    """

    id: int
    node_id: str
    state: str
    context: str
    url: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    description: Optional[str]
    target_url: Optional[str]
    avatar_url: Optional[str]
    required: Union[Unset, None, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        node_id = self.node_id
        state = self.state
        context = self.context
        url = self.url
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        description = self.description
        target_url = self.target_url
        required = self.required
        avatar_url = self.avatar_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "node_id": node_id,
                "state": state,
                "context": context,
                "url": url,
                "created_at": created_at,
                "updated_at": updated_at,
                "description": description,
                "target_url": target_url,
                "avatar_url": avatar_url,
            }
        )
        if required is not UNSET:
            field_dict["required"] = required

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        node_id = d.pop("node_id")

        state = d.pop("state")

        context = d.pop("context")

        url = d.pop("url")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        description = d.pop("description")

        target_url = d.pop("target_url")

        required = d.pop("required", UNSET)

        avatar_url = d.pop("avatar_url")

        simple_commit_status = cls(
            id=id,
            node_id=node_id,
            state=state,
            context=context,
            url=url,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            target_url=target_url,
            required=required,
            avatar_url=avatar_url,
        )

        simple_commit_status.additional_properties = d
        return simple_commit_status

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
