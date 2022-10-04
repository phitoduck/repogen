from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="IssuescreateLabelJsonBody")


@attr.s(auto_attribs=True)
class IssuescreateLabelJsonBody:
    """
    Attributes:
        name (str): The name of the label. Emoji can be added to label names, using either native emoji or colon-style
            markup. For example, typing `:strawberry:` will render the emoji
            ![:strawberry:](https://github.githubassets.com/images/icons/emoji/unicode/1f353.png ":strawberry:"). For a full
            list of available emoji and codes, see "[Emoji cheat sheet](https://github.com/ikatyang/emoji-cheat-sheet)."
        color (Union[Unset, str]): The [hexadecimal color code](http://www.color-hex.com/) for the label, without the
            leading `#`.
        description (Union[Unset, str]): A short description of the label. Must be 100 characters or fewer.
    """

    name: str
    color: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        color = self.color
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if color is not UNSET:
            field_dict["color"] = color
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        color = d.pop("color", UNSET)

        description = d.pop("description", UNSET)

        issuescreate_label_json_body = cls(
            name=name,
            color=color,
            description=description,
        )

        issuescreate_label_json_body.additional_properties = d
        return issuescreate_label_json_body

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
