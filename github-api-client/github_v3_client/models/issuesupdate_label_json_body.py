from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="IssuesupdateLabelJsonBody")


@attr.s(auto_attribs=True)
class IssuesupdateLabelJsonBody:
    """
    Attributes:
        new_name (Union[Unset, str]): The new name of the label. Emoji can be added to label names, using either native
            emoji or colon-style markup. For example, typing `:strawberry:` will render the emoji
            ![:strawberry:](https://github.githubassets.com/images/icons/emoji/unicode/1f353.png ":strawberry:"). For a full
            list of available emoji and codes, see "[Emoji cheat sheet](https://github.com/ikatyang/emoji-cheat-sheet)."
        color (Union[Unset, str]): The [hexadecimal color code](http://www.color-hex.com/) for the label, without the
            leading `#`.
        description (Union[Unset, str]): A short description of the label. Must be 100 characters or fewer.
    """

    new_name: Union[Unset, str] = UNSET
    color: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        new_name = self.new_name
        color = self.color
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if new_name is not UNSET:
            field_dict["new_name"] = new_name
        if color is not UNSET:
            field_dict["color"] = color
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        new_name = d.pop("new_name", UNSET)

        color = d.pop("color", UNSET)

        description = d.pop("description", UNSET)

        issuesupdate_label_json_body = cls(
            new_name=new_name,
            color=color,
            description=description,
        )

        issuesupdate_label_json_body.additional_properties = d
        return issuesupdate_label_json_body

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
