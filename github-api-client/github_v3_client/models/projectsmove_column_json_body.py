from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ProjectsmoveColumnJsonBody")


@attr.s(auto_attribs=True)
class ProjectsmoveColumnJsonBody:
    """
    Attributes:
        position (str): The position of the column in a project. Can be one of: `first`, `last`, or `after:<column_id>`
            to place after the specified column. Example: last.
    """

    position: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        position = self.position

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "position": position,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        position = d.pop("position")

        projectsmove_column_json_body = cls(
            position=position,
        )

        projectsmove_column_json_body.additional_properties = d
        return projectsmove_column_json_body

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
