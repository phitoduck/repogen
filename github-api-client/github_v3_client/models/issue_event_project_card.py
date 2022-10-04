from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="IssueEventProjectCard")


@attr.s(auto_attribs=True)
class IssueEventProjectCard:
    """Issue Event Project Card

    Attributes:
        url (str):
        id (int):
        project_url (str):
        project_id (int):
        column_name (str):
        previous_column_name (Union[Unset, str]):
    """

    url: str
    id: int
    project_url: str
    project_id: int
    column_name: str
    previous_column_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        id = self.id
        project_url = self.project_url
        project_id = self.project_id
        column_name = self.column_name
        previous_column_name = self.previous_column_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "id": id,
                "project_url": project_url,
                "project_id": project_id,
                "column_name": column_name,
            }
        )
        if previous_column_name is not UNSET:
            field_dict["previous_column_name"] = previous_column_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        id = d.pop("id")

        project_url = d.pop("project_url")

        project_id = d.pop("project_id")

        column_name = d.pop("column_name")

        previous_column_name = d.pop("previous_column_name", UNSET)

        issue_event_project_card = cls(
            url=url,
            id=id,
            project_url=project_url,
            project_id=project_id,
            column_name=column_name,
            previous_column_name=previous_column_name,
        )

        issue_event_project_card.additional_properties = d
        return issue_event_project_card

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
