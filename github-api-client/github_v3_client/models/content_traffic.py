from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ContentTraffic")


@attr.s(auto_attribs=True)
class ContentTraffic:
    """Content Traffic

    Attributes:
        path (str):  Example: /github/hubot.
        title (str):  Example: github/hubot: A customizable life embetterment robot..
        count (int):  Example: 3542.
        uniques (int):  Example: 2225.
    """

    path: str
    title: str
    count: int
    uniques: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        path = self.path
        title = self.title
        count = self.count
        uniques = self.uniques

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "title": title,
                "count": count,
                "uniques": uniques,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        path = d.pop("path")

        title = d.pop("title")

        count = d.pop("count")

        uniques = d.pop("uniques")

        content_traffic = cls(
            path=path,
            title=title,
            count=count,
            uniques=uniques,
        )

        content_traffic.additional_properties = d
        return content_traffic

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
