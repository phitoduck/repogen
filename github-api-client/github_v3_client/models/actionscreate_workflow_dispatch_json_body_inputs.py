from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ActionscreateWorkflowDispatchJsonBodyInputs")


@attr.s(auto_attribs=True)
class ActionscreateWorkflowDispatchJsonBodyInputs:
    """Input keys and values configured in the workflow file. The maximum number of properties is 10. Any default
    properties configured in the workflow file will be used when `inputs` are omitted.

    """

    additional_properties: Dict[str, str] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        actionscreate_workflow_dispatch_json_body_inputs = cls()

        actionscreate_workflow_dispatch_json_body_inputs.additional_properties = d
        return actionscreate_workflow_dispatch_json_body_inputs

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> str:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: str) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
