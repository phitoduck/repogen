from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="LicenseSimple")


@attr.s(auto_attribs=True)
class LicenseSimple:
    """License Simple

    Attributes:
        key (str):  Example: mit.
        name (str):  Example: MIT License.
        node_id (str):  Example: MDc6TGljZW5zZW1pdA==.
        url (Optional[str]):  Example: https://api.github.com/licenses/mit.
        spdx_id (Optional[str]):  Example: MIT.
        html_url (Union[Unset, str]):
    """

    key: str
    name: str
    node_id: str
    url: Optional[str]
    spdx_id: Optional[str]
    html_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key
        name = self.name
        node_id = self.node_id
        url = self.url
        spdx_id = self.spdx_id
        html_url = self.html_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "name": name,
                "node_id": node_id,
                "url": url,
                "spdx_id": spdx_id,
            }
        )
        if html_url is not UNSET:
            field_dict["html_url"] = html_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key = d.pop("key")

        name = d.pop("name")

        node_id = d.pop("node_id")

        url = d.pop("url")

        spdx_id = d.pop("spdx_id")

        html_url = d.pop("html_url", UNSET)

        license_simple = cls(
            key=key,
            name=name,
            node_id=node_id,
            url=url,
            spdx_id=spdx_id,
            html_url=html_url,
        )

        license_simple.additional_properties = d
        return license_simple

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
