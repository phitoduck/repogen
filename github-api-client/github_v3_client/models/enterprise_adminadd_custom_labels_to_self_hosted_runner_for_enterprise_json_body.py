from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="EnterpriseAdminaddCustomLabelsToSelfHostedRunnerForEnterpriseJsonBody")


@attr.s(auto_attribs=True)
class EnterpriseAdminaddCustomLabelsToSelfHostedRunnerForEnterpriseJsonBody:
    """
    Attributes:
        labels (List[str]): The names of the custom labels to add to the runner.
    """

    labels: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        labels = self.labels

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "labels": labels,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        labels = cast(List[str], d.pop("labels"))

        enterprise_adminadd_custom_labels_to_self_hosted_runner_for_enterprise_json_body = cls(
            labels=labels,
        )

        enterprise_adminadd_custom_labels_to_self_hosted_runner_for_enterprise_json_body.additional_properties = d
        return enterprise_adminadd_custom_labels_to_self_hosted_runner_for_enterprise_json_body

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
