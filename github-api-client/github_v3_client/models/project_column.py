import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="ProjectColumn")


@attr.s(auto_attribs=True)
class ProjectColumn:
    """Project columns contain cards of work.

    Attributes:
        url (str):  Example: https://api.github.com/projects/columns/367.
        project_url (str):  Example: https://api.github.com/projects/120.
        cards_url (str):  Example: https://api.github.com/projects/columns/367/cards.
        id (int): The unique identifier of the project column Example: 42.
        node_id (str):  Example: MDEzOlByb2plY3RDb2x1bW4zNjc=.
        name (str): Name of the project column Example: Remaining tasks.
        created_at (datetime.datetime):  Example: 2016-09-05T14:18:44Z.
        updated_at (datetime.datetime):  Example: 2016-09-05T14:22:28Z.
    """

    url: str
    project_url: str
    cards_url: str
    id: int
    node_id: str
    name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        project_url = self.project_url
        cards_url = self.cards_url
        id = self.id
        node_id = self.node_id
        name = self.name
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "project_url": project_url,
                "cards_url": cards_url,
                "id": id,
                "node_id": node_id,
                "name": name,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        project_url = d.pop("project_url")

        cards_url = d.pop("cards_url")

        id = d.pop("id")

        node_id = d.pop("node_id")

        name = d.pop("name")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        project_column = cls(
            url=url,
            project_url=project_url,
            cards_url=cards_url,
            id=id,
            node_id=node_id,
            name=name,
            created_at=created_at,
            updated_at=updated_at,
        )

        project_column.additional_properties = d
        return project_column

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
