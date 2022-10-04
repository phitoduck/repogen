from typing import Any, Dict, List, Optional, Type, TypeVar

import attr

T = TypeVar("T", bound="Label")


@attr.s(auto_attribs=True)
class Label:
    """Color-coded labels help you categorize and filter your issues (just like labels in Gmail).

    Attributes:
        id (int):  Example: 208045946.
        node_id (str):  Example: MDU6TGFiZWwyMDgwNDU5NDY=.
        url (str): URL for the label Example: https://api.github.com/repositories/42/labels/bug.
        name (str): The name of the label. Example: bug.
        color (str): 6-character hex code, without the leading #, identifying the color Example: FFFFFF.
        default (bool):  Example: True.
        description (Optional[str]):  Example: Something isn't working.
    """

    id: int
    node_id: str
    url: str
    name: str
    color: str
    default: bool
    description: Optional[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        node_id = self.node_id
        url = self.url
        name = self.name
        color = self.color
        default = self.default
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "node_id": node_id,
                "url": url,
                "name": name,
                "color": color,
                "default": default,
                "description": description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        node_id = d.pop("node_id")

        url = d.pop("url")

        name = d.pop("name")

        color = d.pop("color")

        default = d.pop("default")

        description = d.pop("description")

        label = cls(
            id=id,
            node_id=node_id,
            url=url,
            name=name,
            color=color,
            default=default,
            description=description,
        )

        label.additional_properties = d
        return label

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
