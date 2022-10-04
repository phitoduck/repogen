from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.issuesupdate_json_body_labels_item_type_1 import IssuesupdateJsonBodyLabelsItemType1
from ..models.issuesupdate_json_body_state import IssuesupdateJsonBodyState
from ..models.issuesupdate_json_body_state_reason import IssuesupdateJsonBodyStateReason
from ..types import UNSET, Unset

T = TypeVar("T", bound="IssuesupdateJsonBody")


@attr.s(auto_attribs=True)
class IssuesupdateJsonBody:
    """
    Attributes:
        title (Union[None, Unset, int, str]): The title of the issue.
        body (Union[Unset, None, str]): The contents of the issue.
        assignee (Union[Unset, None, str]): Login for the user that this issue should be assigned to. **This field is
            deprecated.**
        state (Union[Unset, IssuesupdateJsonBodyState]): State of the issue. Either `open` or `closed`.
        state_reason (Union[Unset, None, IssuesupdateJsonBodyStateReason]): The reason for the current state Example:
            not_planned.
        milestone (Union[None, Unset, int, str]):
        labels (Union[Unset, List[Union[IssuesupdateJsonBodyLabelsItemType1, str]]]): Labels to associate with this
            issue. Pass one or more Labels to _replace_ the set of Labels on this Issue. Send an empty array (`[]`) to clear
            all Labels from the Issue. _NOTE: Only users with push access can set labels for issues. Labels are silently
            dropped otherwise._
        assignees (Union[Unset, List[str]]): Logins for Users to assign to this issue. Pass one or more user logins to
            _replace_ the set of assignees on this Issue. Send an empty array (`[]`) to clear all assignees from the Issue.
            _NOTE: Only users with push access can set assignees for new issues. Assignees are silently dropped otherwise._
    """

    title: Union[None, Unset, int, str] = UNSET
    body: Union[Unset, None, str] = UNSET
    assignee: Union[Unset, None, str] = UNSET
    state: Union[Unset, IssuesupdateJsonBodyState] = UNSET
    state_reason: Union[Unset, None, IssuesupdateJsonBodyStateReason] = UNSET
    milestone: Union[None, Unset, int, str] = UNSET
    labels: Union[Unset, List[Union[IssuesupdateJsonBodyLabelsItemType1, str]]] = UNSET
    assignees: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title: Union[None, Unset, int, str]
        if isinstance(self.title, Unset):
            title = UNSET
        elif self.title is None:
            title = None

        else:
            title = self.title

        body = self.body
        assignee = self.assignee
        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        state_reason: Union[Unset, None, str] = UNSET
        if not isinstance(self.state_reason, Unset):
            state_reason = self.state_reason.value if self.state_reason else None

        milestone: Union[None, Unset, int, str]
        if isinstance(self.milestone, Unset):
            milestone = UNSET
        elif self.milestone is None:
            milestone = None

        else:
            milestone = self.milestone

        labels: Union[Unset, List[Union[Dict[str, Any], str]]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item: Union[Dict[str, Any], str]

                if isinstance(labels_item_data, IssuesupdateJsonBodyLabelsItemType1):
                    labels_item = labels_item_data.to_dict()

                else:
                    labels_item = labels_item_data

                labels.append(labels_item)

        assignees: Union[Unset, List[str]] = UNSET
        if not isinstance(self.assignees, Unset):
            assignees = self.assignees

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if body is not UNSET:
            field_dict["body"] = body
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if state is not UNSET:
            field_dict["state"] = state
        if state_reason is not UNSET:
            field_dict["state_reason"] = state_reason
        if milestone is not UNSET:
            field_dict["milestone"] = milestone
        if labels is not UNSET:
            field_dict["labels"] = labels
        if assignees is not UNSET:
            field_dict["assignees"] = assignees

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_title(data: object) -> Union[None, Unset, int, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int, str], data)

        title = _parse_title(d.pop("title", UNSET))

        body = d.pop("body", UNSET)

        assignee = d.pop("assignee", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, IssuesupdateJsonBodyState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = IssuesupdateJsonBodyState(_state)

        _state_reason = d.pop("state_reason", UNSET)
        state_reason: Union[Unset, None, IssuesupdateJsonBodyStateReason]
        if _state_reason is None:
            state_reason = None
        elif isinstance(_state_reason, Unset):
            state_reason = UNSET
        else:
            state_reason = IssuesupdateJsonBodyStateReason(_state_reason)

        def _parse_milestone(data: object) -> Union[None, Unset, int, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int, str], data)

        milestone = _parse_milestone(d.pop("milestone", UNSET))

        labels = []
        _labels = d.pop("labels", UNSET)
        for labels_item_data in _labels or []:

            def _parse_labels_item(data: object) -> Union[IssuesupdateJsonBodyLabelsItemType1, str]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    labels_item_type_1 = IssuesupdateJsonBodyLabelsItemType1.from_dict(data)

                    return labels_item_type_1
                except:  # noqa: E722
                    pass
                return cast(Union[IssuesupdateJsonBodyLabelsItemType1, str], data)

            labels_item = _parse_labels_item(labels_item_data)

            labels.append(labels_item)

        assignees = cast(List[str], d.pop("assignees", UNSET))

        issuesupdate_json_body = cls(
            title=title,
            body=body,
            assignee=assignee,
            state=state,
            state_reason=state_reason,
            milestone=milestone,
            labels=labels,
            assignees=assignees,
        )

        issuesupdate_json_body.additional_properties = d
        return issuesupdate_json_body

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
