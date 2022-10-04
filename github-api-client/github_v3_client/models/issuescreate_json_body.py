from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.issuescreate_json_body_labels_item_type_1 import IssuescreateJsonBodyLabelsItemType1
from ..types import UNSET, Unset

T = TypeVar("T", bound="IssuescreateJsonBody")


@attr.s(auto_attribs=True)
class IssuescreateJsonBody:
    """
    Attributes:
        title (Union[int, str]): The title of the issue.
        body (Union[Unset, str]): The contents of the issue.
        assignee (Union[Unset, None, str]): Login for the user that this issue should be assigned to. _NOTE: Only users
            with push access can set the assignee for new issues. The assignee is silently dropped otherwise. **This field
            is deprecated.**_
        milestone (Union[None, Unset, int, str]):
        labels (Union[Unset, List[Union[IssuescreateJsonBodyLabelsItemType1, str]]]): Labels to associate with this
            issue. _NOTE: Only users with push access can set labels for new issues. Labels are silently dropped otherwise._
        assignees (Union[Unset, List[str]]): Logins for Users to assign to this issue. _NOTE: Only users with push
            access can set assignees for new issues. Assignees are silently dropped otherwise._
    """

    title: Union[int, str]
    body: Union[Unset, str] = UNSET
    assignee: Union[Unset, None, str] = UNSET
    milestone: Union[None, Unset, int, str] = UNSET
    labels: Union[Unset, List[Union[IssuescreateJsonBodyLabelsItemType1, str]]] = UNSET
    assignees: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title: Union[int, str]

        title = self.title

        body = self.body
        assignee = self.assignee
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

                if isinstance(labels_item_data, IssuescreateJsonBodyLabelsItemType1):
                    labels_item = labels_item_data.to_dict()

                else:
                    labels_item = labels_item_data

                labels.append(labels_item)

        assignees: Union[Unset, List[str]] = UNSET
        if not isinstance(self.assignees, Unset):
            assignees = self.assignees

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if body is not UNSET:
            field_dict["body"] = body
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
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

        def _parse_title(data: object) -> Union[int, str]:
            return cast(Union[int, str], data)

        title = _parse_title(d.pop("title"))

        body = d.pop("body", UNSET)

        assignee = d.pop("assignee", UNSET)

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

            def _parse_labels_item(data: object) -> Union[IssuescreateJsonBodyLabelsItemType1, str]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    labels_item_type_1 = IssuescreateJsonBodyLabelsItemType1.from_dict(data)

                    return labels_item_type_1
                except:  # noqa: E722
                    pass
                return cast(Union[IssuescreateJsonBodyLabelsItemType1, str], data)

            labels_item = _parse_labels_item(labels_item_data)

            labels.append(labels_item)

        assignees = cast(List[str], d.pop("assignees", UNSET))

        issuescreate_json_body = cls(
            title=title,
            body=body,
            assignee=assignee,
            milestone=milestone,
            labels=labels,
            assignees=assignees,
        )

        issuescreate_json_body.additional_properties = d
        return issuescreate_json_body

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
