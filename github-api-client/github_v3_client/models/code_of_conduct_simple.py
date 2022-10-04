from typing import Any, Dict, List, Optional, Type, TypeVar

import attr

T = TypeVar("T", bound="CodeOfConductSimple")


@attr.s(auto_attribs=True)
class CodeOfConductSimple:
    """Code of Conduct Simple

    Attributes:
        url (str):  Example: https://api.github.com/repos/github/docs/community/code_of_conduct.
        key (str):  Example: citizen_code_of_conduct.
        name (str):  Example: Citizen Code of Conduct.
        html_url (Optional[str]):  Example: https://github.com/github/docs/blob/main/CODE_OF_CONDUCT.md.
    """

    url: str
    key: str
    name: str
    html_url: Optional[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        key = self.key
        name = self.name
        html_url = self.html_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "key": key,
                "name": name,
                "html_url": html_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        key = d.pop("key")

        name = d.pop("name")

        html_url = d.pop("html_url")

        code_of_conduct_simple = cls(
            url=url,
            key=key,
            name=name,
            html_url=html_url,
        )

        code_of_conduct_simple.additional_properties = d
        return code_of_conduct_simple

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
