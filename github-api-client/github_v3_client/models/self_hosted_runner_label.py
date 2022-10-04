from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.self_hosted_runner_label_type import SelfHostedRunnerLabelType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SelfHostedRunnerLabel")


@attr.s(auto_attribs=True)
class SelfHostedRunnerLabel:
    """A label for a self hosted runner

    Attributes:
        name (str): Name of the label.
        id (Union[Unset, int]): Unique identifier of the label.
        type (Union[Unset, SelfHostedRunnerLabelType]): The type of label. Read-only labels are applied automatically
            when the runner is configured.
    """

    name: str
    id: Union[Unset, int] = UNSET
    type: Union[Unset, SelfHostedRunnerLabelType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        id = self.id
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        id = d.pop("id", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, SelfHostedRunnerLabelType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = SelfHostedRunnerLabelType(_type)

        self_hosted_runner_label = cls(
            name=name,
            id=id,
            type=type,
        )

        self_hosted_runner_label.additional_properties = d
        return self_hosted_runner_label

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
