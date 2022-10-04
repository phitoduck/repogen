from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReposcreateAutolinkJsonBody")


@attr.s(auto_attribs=True)
class ReposcreateAutolinkJsonBody:
    """
    Attributes:
        key_prefix (str): This prefix appended by certain characters will generate a link any time it is found in an
            issue, pull request, or commit.
        url_template (str): The URL must contain `<num>` for the reference number. `<num>` matches different characters
            depending on the value of `is_alphanumeric`.
        is_alphanumeric (Union[Unset, bool]): Whether this autolink reference matches alphanumeric characters. If true,
            the `<num>` parameter of the `url_template` matches alphanumeric characters `A-Z` (case insensitive), `0-9`, and
            `-`. If false, this autolink reference only matches numeric characters. Default: True.
    """

    key_prefix: str
    url_template: str
    is_alphanumeric: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key_prefix = self.key_prefix
        url_template = self.url_template
        is_alphanumeric = self.is_alphanumeric

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key_prefix": key_prefix,
                "url_template": url_template,
            }
        )
        if is_alphanumeric is not UNSET:
            field_dict["is_alphanumeric"] = is_alphanumeric

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key_prefix = d.pop("key_prefix")

        url_template = d.pop("url_template")

        is_alphanumeric = d.pop("is_alphanumeric", UNSET)

        reposcreate_autolink_json_body = cls(
            key_prefix=key_prefix,
            url_template=url_template,
            is_alphanumeric=is_alphanumeric,
        )

        reposcreate_autolink_json_body.additional_properties = d
        return reposcreate_autolink_json_body

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
