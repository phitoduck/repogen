from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="IssuesaddAssigneesJsonBody")


@attr.s(auto_attribs=True)
class IssuesaddAssigneesJsonBody:
    """
    Attributes:
        assignees (Union[Unset, List[str]]): Usernames of people to assign this issue to. _NOTE: Only users with push
            access can add assignees to an issue. Assignees are silently ignored otherwise._
    """

    assignees: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        assignees: Union[Unset, List[str]] = UNSET
        if not isinstance(self.assignees, Unset):
            assignees = self.assignees

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assignees is not UNSET:
            field_dict["assignees"] = assignees

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        assignees = cast(List[str], d.pop("assignees", UNSET))

        issuesadd_assignees_json_body = cls(
            assignees=assignees,
        )

        issuesadd_assignees_json_body.additional_properties = d
        return issuesadd_assignees_json_body

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
