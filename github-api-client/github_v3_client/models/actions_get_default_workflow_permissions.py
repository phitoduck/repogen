from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.actions_default_workflow_permissions import ActionsDefaultWorkflowPermissions

T = TypeVar("T", bound="ActionsGetDefaultWorkflowPermissions")


@attr.s(auto_attribs=True)
class ActionsGetDefaultWorkflowPermissions:
    """
    Attributes:
        default_workflow_permissions (ActionsDefaultWorkflowPermissions): The default workflow permissions granted to
            the GITHUB_TOKEN when running workflows.
        can_approve_pull_request_reviews (bool): Whether GitHub Actions can approve pull requests. Enabling this can be
            a security risk.
    """

    default_workflow_permissions: ActionsDefaultWorkflowPermissions
    can_approve_pull_request_reviews: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        default_workflow_permissions = self.default_workflow_permissions.value

        can_approve_pull_request_reviews = self.can_approve_pull_request_reviews

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "default_workflow_permissions": default_workflow_permissions,
                "can_approve_pull_request_reviews": can_approve_pull_request_reviews,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        default_workflow_permissions = ActionsDefaultWorkflowPermissions(d.pop("default_workflow_permissions"))

        can_approve_pull_request_reviews = d.pop("can_approve_pull_request_reviews")

        actions_get_default_workflow_permissions = cls(
            default_workflow_permissions=default_workflow_permissions,
            can_approve_pull_request_reviews=can_approve_pull_request_reviews,
        )

        actions_get_default_workflow_permissions.additional_properties = d
        return actions_get_default_workflow_permissions

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
