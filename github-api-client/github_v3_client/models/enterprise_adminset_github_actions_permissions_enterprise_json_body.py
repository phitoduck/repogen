from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.allowed_actions import AllowedActions
from ..models.enabled_organizations import EnabledOrganizations
from ..types import UNSET, Unset

T = TypeVar("T", bound="EnterpriseAdminsetGithubActionsPermissionsEnterpriseJsonBody")


@attr.s(auto_attribs=True)
class EnterpriseAdminsetGithubActionsPermissionsEnterpriseJsonBody:
    """
    Attributes:
        enabled_organizations (EnabledOrganizations): The policy that controls the organizations in the enterprise that
            are allowed to run GitHub Actions.
        allowed_actions (Union[Unset, AllowedActions]): The permissions policy that controls the actions and reusable
            workflows that are allowed to run.
    """

    enabled_organizations: EnabledOrganizations
    allowed_actions: Union[Unset, AllowedActions] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled_organizations = self.enabled_organizations.value

        allowed_actions: Union[Unset, str] = UNSET
        if not isinstance(self.allowed_actions, Unset):
            allowed_actions = self.allowed_actions.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled_organizations": enabled_organizations,
            }
        )
        if allowed_actions is not UNSET:
            field_dict["allowed_actions"] = allowed_actions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled_organizations = EnabledOrganizations(d.pop("enabled_organizations"))

        _allowed_actions = d.pop("allowed_actions", UNSET)
        allowed_actions: Union[Unset, AllowedActions]
        if isinstance(_allowed_actions, Unset):
            allowed_actions = UNSET
        else:
            allowed_actions = AllowedActions(_allowed_actions)

        enterprise_adminset_github_actions_permissions_enterprise_json_body = cls(
            enabled_organizations=enabled_organizations,
            allowed_actions=allowed_actions,
        )

        enterprise_adminset_github_actions_permissions_enterprise_json_body.additional_properties = d
        return enterprise_adminset_github_actions_permissions_enterprise_json_body

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
