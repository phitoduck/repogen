import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.issuescreate_milestone_json_body_state import IssuescreateMilestoneJsonBodyState
from ..types import UNSET, Unset

T = TypeVar("T", bound="IssuescreateMilestoneJsonBody")


@attr.s(auto_attribs=True)
class IssuescreateMilestoneJsonBody:
    """
    Attributes:
        title (str): The title of the milestone.
        state (Union[Unset, IssuescreateMilestoneJsonBodyState]): The state of the milestone. Either `open` or `closed`.
            Default: IssuescreateMilestoneJsonBodyState.OPEN.
        description (Union[Unset, str]): A description of the milestone.
        due_on (Union[Unset, datetime.datetime]): The milestone due date. This is a timestamp in [ISO
            8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
    """

    title: str
    state: Union[Unset, IssuescreateMilestoneJsonBodyState] = IssuescreateMilestoneJsonBodyState.OPEN
    description: Union[Unset, str] = UNSET
    due_on: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        description = self.description
        due_on: Union[Unset, str] = UNSET
        if not isinstance(self.due_on, Unset):
            due_on = self.due_on.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if state is not UNSET:
            field_dict["state"] = state
        if description is not UNSET:
            field_dict["description"] = description
        if due_on is not UNSET:
            field_dict["due_on"] = due_on

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title")

        _state = d.pop("state", UNSET)
        state: Union[Unset, IssuescreateMilestoneJsonBodyState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = IssuescreateMilestoneJsonBodyState(_state)

        description = d.pop("description", UNSET)

        _due_on = d.pop("due_on", UNSET)
        due_on: Union[Unset, datetime.datetime]
        if isinstance(_due_on, Unset):
            due_on = UNSET
        else:
            due_on = isoparse(_due_on)

        issuescreate_milestone_json_body = cls(
            title=title,
            state=state,
            description=description,
            due_on=due_on,
        )

        issuescreate_milestone_json_body.additional_properties = d
        return issuescreate_milestone_json_body

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
