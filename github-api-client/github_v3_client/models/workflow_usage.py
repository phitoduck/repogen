from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.workflow_usage_billable import WorkflowUsageBillable

T = TypeVar("T", bound="WorkflowUsage")


@attr.s(auto_attribs=True)
class WorkflowUsage:
    """Workflow Usage

    Attributes:
        billable (WorkflowUsageBillable):
    """

    billable: WorkflowUsageBillable
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        billable = self.billable.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "billable": billable,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        billable = WorkflowUsageBillable.from_dict(d.pop("billable"))

        workflow_usage = cls(
            billable=billable,
        )

        workflow_usage.additional_properties = d
        return workflow_usage

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
