from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PullsremoveRequestedReviewersJsonBody")


@attr.s(auto_attribs=True)
class PullsremoveRequestedReviewersJsonBody:
    """
    Attributes:
        reviewers (List[str]): An array of user `login`s that will be removed.
        team_reviewers (Union[Unset, List[str]]): An array of team `slug`s that will be removed.
    """

    reviewers: List[str]
    team_reviewers: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reviewers = self.reviewers

        team_reviewers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.team_reviewers, Unset):
            team_reviewers = self.team_reviewers

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reviewers": reviewers,
            }
        )
        if team_reviewers is not UNSET:
            field_dict["team_reviewers"] = team_reviewers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        reviewers = cast(List[str], d.pop("reviewers"))

        team_reviewers = cast(List[str], d.pop("team_reviewers", UNSET))

        pullsremove_requested_reviewers_json_body = cls(
            reviewers=reviewers,
            team_reviewers=team_reviewers,
        )

        pullsremove_requested_reviewers_json_body.additional_properties = d
        return pullsremove_requested_reviewers_json_body

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
