import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.simple_user import SimpleUser
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectCard")


@attr.s(auto_attribs=True)
class ProjectCard:
    """Project cards represent a scope of work.

    Attributes:
        url (str):  Example: https://api.github.com/projects/columns/cards/1478.
        id (int): The project card's ID Example: 42.
        node_id (str):  Example: MDExOlByb2plY3RDYXJkMTQ3OA==.
        created_at (datetime.datetime):  Example: 2016-09-05T14:21:06Z.
        updated_at (datetime.datetime):  Example: 2016-09-05T14:20:22Z.
        column_url (str):  Example: https://api.github.com/projects/columns/367.
        project_url (str):  Example: https://api.github.com/projects/120.
        note (Optional[str]):  Example: Add payload for delete Project column.
        creator (Optional[SimpleUser]): Simple User
        archived (Union[Unset, bool]): Whether or not the card is archived
        column_name (Union[Unset, str]):
        project_id (Union[Unset, str]):
        content_url (Union[Unset, str]):  Example: https://api.github.com/repos/api-playground/projects-test/issues/3.
    """

    url: str
    id: int
    node_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    column_url: str
    project_url: str
    note: Optional[str]
    creator: Optional[SimpleUser]
    archived: Union[Unset, bool] = UNSET
    column_name: Union[Unset, str] = UNSET
    project_id: Union[Unset, str] = UNSET
    content_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        node_id = self.node_id
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        column_url = self.column_url
        project_url = self.project_url
        note = self.note
        creator = self.creator.to_dict() if self.creator else None

        archived = self.archived
        column_name = self.column_name
        project_id = self.project_id
        content_url = self.content_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "id": id,
                "node_id": node_id,
                "created_at": created_at,
                "updated_at": updated_at,
                "column_url": column_url,
                "project_url": project_url,
                "note": note,
                "creator": creator,
            }
        )
        if archived is not UNSET:
            field_dict["archived"] = archived
        if column_name is not UNSET:
            field_dict["column_name"] = column_name
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if content_url is not UNSET:
            field_dict["content_url"] = content_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        id = d.pop("id")

        node_id = d.pop("node_id")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        column_url = d.pop("column_url")

        project_url = d.pop("project_url")

        note = d.pop("note")

        _creator = d.pop("creator")
        creator: Optional[SimpleUser]
        if _creator is None:
            creator = None
        else:
            creator = SimpleUser.from_dict(_creator)

        archived = d.pop("archived", UNSET)

        column_name = d.pop("column_name", UNSET)

        project_id = d.pop("project_id", UNSET)

        content_url = d.pop("content_url", UNSET)

        project_card = cls(
            url=url,
            id=id,
            node_id=node_id,
            created_at=created_at,
            updated_at=updated_at,
            column_url=column_url,
            project_url=project_url,
            note=note,
            creator=creator,
            archived=archived,
            column_name=column_name,
            project_id=project_id,
            content_url=content_url,
        )

        project_card.additional_properties = d
        return project_card

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
