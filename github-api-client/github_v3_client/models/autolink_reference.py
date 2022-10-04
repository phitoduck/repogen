from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="AutolinkReference")


@attr.s(auto_attribs=True)
class AutolinkReference:
    """An autolink reference.

    Attributes:
        id (int):  Example: 3.
        key_prefix (str): The prefix of a key that is linkified. Example: TICKET-.
        url_template (str): A template for the target URL that is generated if a key was found. Example:
            https://example.com/TICKET?query=<num>.
        is_alphanumeric (bool): Whether this autolink reference matches alphanumeric characters. If false, this autolink
            reference only matches numeric characters. Example: True.
    """

    id: int
    key_prefix: str
    url_template: str
    is_alphanumeric: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        key_prefix = self.key_prefix
        url_template = self.url_template
        is_alphanumeric = self.is_alphanumeric

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "key_prefix": key_prefix,
                "url_template": url_template,
                "is_alphanumeric": is_alphanumeric,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        key_prefix = d.pop("key_prefix")

        url_template = d.pop("url_template")

        is_alphanumeric = d.pop("is_alphanumeric")

        autolink_reference = cls(
            id=id,
            key_prefix=key_prefix,
            url_template=url_template,
            is_alphanumeric=is_alphanumeric,
        )

        autolink_reference.additional_properties = d
        return autolink_reference

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
