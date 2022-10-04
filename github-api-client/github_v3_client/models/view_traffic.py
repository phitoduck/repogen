from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.traffic import Traffic

T = TypeVar("T", bound="ViewTraffic")


@attr.s(auto_attribs=True)
class ViewTraffic:
    """View Traffic

    Attributes:
        count (int):  Example: 14850.
        uniques (int):  Example: 3782.
        views (List[Traffic]):
    """

    count: int
    uniques: int
    views: List[Traffic]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count = self.count
        uniques = self.uniques
        views = []
        for views_item_data in self.views:
            views_item = views_item_data.to_dict()

            views.append(views_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "uniques": uniques,
                "views": views,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        count = d.pop("count")

        uniques = d.pop("uniques")

        views = []
        _views = d.pop("views")
        for views_item_data in _views:
            views_item = Traffic.from_dict(views_item_data)

            views.append(views_item)

        view_traffic = cls(
            count=count,
            uniques=uniques,
            views=views,
        )

        view_traffic.additional_properties = d
        return view_traffic

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
