from typing import Any, Dict, List, Optional, Type, TypeVar

import attr

from ..models.contributor_activity_weeks_item import ContributorActivityWeeksItem
from ..models.simple_user import SimpleUser

T = TypeVar("T", bound="ContributorActivity")


@attr.s(auto_attribs=True)
class ContributorActivity:
    """Contributor Activity

    Attributes:
        total (int):  Example: 135.
        weeks (List[ContributorActivityWeeksItem]):  Example: [{'w': '1367712000', 'a': 6898, 'd': 77, 'c': 10}].
        author (Optional[SimpleUser]): Simple User
    """

    total: int
    weeks: List[ContributorActivityWeeksItem]
    author: Optional[SimpleUser]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total = self.total
        weeks = []
        for weeks_item_data in self.weeks:
            weeks_item = weeks_item_data.to_dict()

            weeks.append(weeks_item)

        author = self.author.to_dict() if self.author else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "weeks": weeks,
                "author": author,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total = d.pop("total")

        weeks = []
        _weeks = d.pop("weeks")
        for weeks_item_data in _weeks:
            weeks_item = ContributorActivityWeeksItem.from_dict(weeks_item_data)

            weeks.append(weeks_item)

        _author = d.pop("author")
        author: Optional[SimpleUser]
        if _author is None:
            author = None
        else:
            author = SimpleUser.from_dict(_author)

        contributor_activity = cls(
            total=total,
            weeks=weeks,
            author=author,
        )

        contributor_activity.additional_properties = d
        return contributor_activity

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
