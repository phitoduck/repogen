from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectsmoveCardJsonBody")


@attr.s(auto_attribs=True)
class ProjectsmoveCardJsonBody:
    """
    Attributes:
        position (str): The position of the card in a column. Can be one of: `top`, `bottom`, or `after:<card_id>` to
            place after the specified card. Example: bottom.
        column_id (Union[Unset, int]): The unique identifier of the column the card should be moved to Example: 42.
    """

    position: str
    column_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        position = self.position
        column_id = self.column_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "position": position,
            }
        )
        if column_id is not UNSET:
            field_dict["column_id"] = column_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        position = d.pop("position")

        column_id = d.pop("column_id", UNSET)

        projectsmove_card_json_body = cls(
            position=position,
            column_id=column_id,
        )

        projectsmove_card_json_body.additional_properties = d
        return projectsmove_card_json_body

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
