from typing import Any, Dict, List, Optional, Type, TypeVar

import attr

T = TypeVar("T", bound="ContentDirectoryItemLinks")


@attr.s(auto_attribs=True)
class ContentDirectoryItemLinks:
    """
    Attributes:
        self_ (str):
        git (Optional[str]):
        html (Optional[str]):
    """

    self_: str
    git: Optional[str]
    html: Optional[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        self_ = self.self_
        git = self.git
        html = self.html

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
                "git": git,
                "html": html,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        self_ = d.pop("self")

        git = d.pop("git")

        html = d.pop("html")

        content_directory_item_links = cls(
            self_=self_,
            git=git,
            html=html,
        )

        content_directory_item_links.additional_properties = d
        return content_directory_item_links

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
