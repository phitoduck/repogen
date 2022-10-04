from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="CommitActivity")


@attr.s(auto_attribs=True)
class CommitActivity:
    """Commit Activity

    Attributes:
        days (List[int]):  Example: [0, 3, 26, 20, 39, 1, 0].
        total (int):  Example: 89.
        week (int):  Example: 1336280400.
    """

    days: List[int]
    total: int
    week: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        days = self.days

        total = self.total
        week = self.week

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "days": days,
                "total": total,
                "week": week,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        days = cast(List[int], d.pop("days"))

        total = d.pop("total")

        week = d.pop("week")

        commit_activity = cls(
            days=days,
            total=total,
            week=week,
        )

        commit_activity.additional_properties = d
        return commit_activity

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
