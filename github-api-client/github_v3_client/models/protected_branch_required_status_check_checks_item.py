from typing import Any, Dict, List, Optional, Type, TypeVar

import attr

T = TypeVar("T", bound="ProtectedBranchRequiredStatusCheckChecksItem")


@attr.s(auto_attribs=True)
class ProtectedBranchRequiredStatusCheckChecksItem:
    """
    Attributes:
        context (str):
        app_id (Optional[int]):
    """

    context: str
    app_id: Optional[int]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        context = self.context
        app_id = self.app_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "context": context,
                "app_id": app_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        context = d.pop("context")

        app_id = d.pop("app_id")

        protected_branch_required_status_check_checks_item = cls(
            context=context,
            app_id=app_id,
        )

        protected_branch_required_status_check_checks_item.additional_properties = d
        return protected_branch_required_status_check_checks_item

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
