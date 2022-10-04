from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="IssuessetLabelsJsonBodyType0")


@attr.s(auto_attribs=True)
class IssuessetLabelsJsonBodyType0:
    """
    Attributes:
        labels (Union[Unset, List[str]]): The names of the labels to set for the issue. The labels you set replace any
            existing labels. You can pass an empty array to remove all labels. Alternatively, you can pass a single label as
            a `string` or an `array` of labels directly, but GitHub recommends passing an object with the `labels` key. You
            can also add labels to the existing labels for an issue. For more information, see "[Add labels to an
            issue](https://docs.github.com/rest/reference/issues#add-labels-to-an-issue)."
    """

    labels: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        labels: Union[Unset, List[str]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        labels = cast(List[str], d.pop("labels", UNSET))

        issuesset_labels_json_body_type_0 = cls(
            labels=labels,
        )

        issuesset_labels_json_body_type_0.additional_properties = d
        return issuesset_labels_json_body_type_0

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
