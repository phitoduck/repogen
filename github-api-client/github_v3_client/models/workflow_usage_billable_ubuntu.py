from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowUsageBillableUBUNTU")


@attr.s(auto_attribs=True)
class WorkflowUsageBillableUBUNTU:
    """
    Attributes:
        total_ms (Union[Unset, int]):
    """

    total_ms: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_ms = self.total_ms

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_ms is not UNSET:
            field_dict["total_ms"] = total_ms

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_ms = d.pop("total_ms", UNSET)

        workflow_usage_billable_ubuntu = cls(
            total_ms=total_ms,
        )

        workflow_usage_billable_ubuntu.additional_properties = d
        return workflow_usage_billable_ubuntu

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
