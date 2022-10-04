from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.issuesset_labels_json_body_type_2_labels_item import IssuessetLabelsJsonBodyType2LabelsItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="IssuessetLabelsJsonBodyType2")


@attr.s(auto_attribs=True)
class IssuessetLabelsJsonBodyType2:
    """
    Attributes:
        labels (Union[Unset, List[IssuessetLabelsJsonBodyType2LabelsItem]]):
    """

    labels: Union[Unset, List[IssuessetLabelsJsonBodyType2LabelsItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        labels: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()

                labels.append(labels_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        labels = []
        _labels = d.pop("labels", UNSET)
        for labels_item_data in _labels or []:
            labels_item = IssuessetLabelsJsonBodyType2LabelsItem.from_dict(labels_item_data)

            labels.append(labels_item)

        issuesset_labels_json_body_type_2 = cls(
            labels=labels,
        )

        issuesset_labels_json_body_type_2.additional_properties = d
        return issuesset_labels_json_body_type_2

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
