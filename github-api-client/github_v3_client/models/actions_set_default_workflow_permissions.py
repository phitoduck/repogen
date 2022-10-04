from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.actions_default_workflow_permissions import ActionsDefaultWorkflowPermissions
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActionsSetDefaultWorkflowPermissions")


@attr.s(auto_attribs=True)
class ActionsSetDefaultWorkflowPermissions:
    """
    Attributes:
        default_workflow_permissions (Union[Unset, ActionsDefaultWorkflowPermissions]): The default workflow permissions
            granted to the GITHUB_TOKEN when running workflows.
        can_approve_pull_request_reviews (Union[Unset, bool]): Whether GitHub Actions can approve pull requests.
            Enabling this can be a security risk.
    """

    default_workflow_permissions: Union[Unset, ActionsDefaultWorkflowPermissions] = UNSET
    can_approve_pull_request_reviews: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        default_workflow_permissions: Union[Unset, str] = UNSET
        if not isinstance(self.default_workflow_permissions, Unset):
            default_workflow_permissions = self.default_workflow_permissions.value

        can_approve_pull_request_reviews = self.can_approve_pull_request_reviews

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_workflow_permissions is not UNSET:
            field_dict["default_workflow_permissions"] = default_workflow_permissions
        if can_approve_pull_request_reviews is not UNSET:
            field_dict["can_approve_pull_request_reviews"] = can_approve_pull_request_reviews

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _default_workflow_permissions = d.pop("default_workflow_permissions", UNSET)
        default_workflow_permissions: Union[Unset, ActionsDefaultWorkflowPermissions]
        if isinstance(_default_workflow_permissions, Unset):
            default_workflow_permissions = UNSET
        else:
            default_workflow_permissions = ActionsDefaultWorkflowPermissions(_default_workflow_permissions)

        can_approve_pull_request_reviews = d.pop("can_approve_pull_request_reviews", UNSET)

        actions_set_default_workflow_permissions = cls(
            default_workflow_permissions=default_workflow_permissions,
            can_approve_pull_request_reviews=can_approve_pull_request_reviews,
        )

        actions_set_default_workflow_permissions.additional_properties = d
        return actions_set_default_workflow_permissions

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
