from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectsupdateCardJsonBody")


@attr.s(auto_attribs=True)
class ProjectsupdateCardJsonBody:
    """
    Attributes:
        note (Union[Unset, None, str]): The project card's note Example: Update all gems.
        archived (Union[Unset, bool]): Whether or not the card is archived
    """

    note: Union[Unset, None, str] = UNSET
    archived: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        note = self.note
        archived = self.archived

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if note is not UNSET:
            field_dict["note"] = note
        if archived is not UNSET:
            field_dict["archived"] = archived

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        note = d.pop("note", UNSET)

        archived = d.pop("archived", UNSET)

        projectsupdate_card_json_body = cls(
            note=note,
            archived=archived,
        )

        projectsupdate_card_json_body.additional_properties = d
        return projectsupdate_card_json_body

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
