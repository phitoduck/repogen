from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.self_hosted_runner_label import SelfHostedRunnerLabel

T = TypeVar("T", bound="SelfHostedRunners")


@attr.s(auto_attribs=True)
class SelfHostedRunners:
    """A self hosted runner

    Attributes:
        id (int): The id of the runner. Example: 5.
        name (str): The name of the runner. Example: iMac.
        os (str): The Operating System of the runner. Example: macos.
        status (str): The status of the runner. Example: online.
        busy (bool):
        labels (List[SelfHostedRunnerLabel]):
    """

    id: int
    name: str
    os: str
    status: str
    busy: bool
    labels: List[SelfHostedRunnerLabel]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        os = self.os
        status = self.status
        busy = self.busy
        labels = []
        for labels_item_data in self.labels:
            labels_item = labels_item_data.to_dict()

            labels.append(labels_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "os": os,
                "status": status,
                "busy": busy,
                "labels": labels,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        os = d.pop("os")

        status = d.pop("status")

        busy = d.pop("busy")

        labels = []
        _labels = d.pop("labels")
        for labels_item_data in _labels:
            labels_item = SelfHostedRunnerLabel.from_dict(labels_item_data)

            labels.append(labels_item)

        self_hosted_runners = cls(
            id=id,
            name=name,
            os=os,
            status=status,
            busy=busy,
            labels=labels,
        )

        self_hosted_runners.additional_properties = d
        return self_hosted_runners

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
