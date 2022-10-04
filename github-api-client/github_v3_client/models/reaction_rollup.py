from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ReactionRollup")


@attr.s(auto_attribs=True)
class ReactionRollup:
    """
    Attributes:
        url (str):
        total_count (int):
        field_1 (int):
        field_1 (int):
        laugh (int):
        confused (int):
        heart (int):
        hooray (int):
        eyes (int):
        rocket (int):
    """

    url: str
    total_count: int
    field_1: int
    # field_1: int
    laugh: int
    confused: int
    heart: int
    hooray: int
    eyes: int
    rocket: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        total_count = self.total_count
        field_1 = self.field_1
        # field_1 = self.field_1
        laugh = self.laugh
        confused = self.confused
        heart = self.heart
        hooray = self.hooray
        eyes = self.eyes
        rocket = self.rocket

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "total_count": total_count,
                "+1": field_1,
                "-1": field_1,
                "laugh": laugh,
                "confused": confused,
                "heart": heart,
                "hooray": hooray,
                "eyes": eyes,
                "rocket": rocket,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        total_count = d.pop("total_count")

        field_1 = d.pop("+1")

        field_1 = d.pop("-1")

        laugh = d.pop("laugh")

        confused = d.pop("confused")

        heart = d.pop("heart")

        hooray = d.pop("hooray")

        eyes = d.pop("eyes")

        rocket = d.pop("rocket")

        reaction_rollup = cls(
            url=url,
            total_count=total_count,
            field_1=field_1,
            # field_1=field_1,
            laugh=laugh,
            confused=confused,
            heart=heart,
            hooray=hooray,
            eyes=eyes,
            rocket=rocket,
        )

        reaction_rollup.additional_properties = d
        return reaction_rollup

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
