from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.allowed_actions import AllowedActions
from ..models.enabled_organizations import EnabledOrganizations
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActionsEnterprisePermissions")


@attr.s(auto_attribs=True)
class ActionsEnterprisePermissions:
    """
    Attributes:
        enabled_organizations (EnabledOrganizations): The policy that controls the organizations in the enterprise that
            are allowed to run GitHub Actions.
        selected_organizations_url (Union[Unset, str]): The API URL to use to get or set the selected organizations that
            are allowed to run GitHub Actions, when `enabled_organizations` is set to `selected`.
        allowed_actions (Union[Unset, AllowedActions]): The permissions policy that controls the actions and reusable
            workflows that are allowed to run.
        selected_actions_url (Union[Unset, str]): The API URL to use to get or set the actions and reusable workflows
            that are allowed to run, when `allowed_actions` is set to `selected`.
    """

    enabled_organizations: EnabledOrganizations
    selected_organizations_url: Union[Unset, str] = UNSET
    allowed_actions: Union[Unset, AllowedActions] = UNSET
    selected_actions_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled_organizations = self.enabled_organizations.value

        selected_organizations_url = self.selected_organizations_url
        allowed_actions: Union[Unset, str] = UNSET
        if not isinstance(self.allowed_actions, Unset):
            allowed_actions = self.allowed_actions.value

        selected_actions_url = self.selected_actions_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled_organizations": enabled_organizations,
            }
        )
        if selected_organizations_url is not UNSET:
            field_dict["selected_organizations_url"] = selected_organizations_url
        if allowed_actions is not UNSET:
            field_dict["allowed_actions"] = allowed_actions
        if selected_actions_url is not UNSET:
            field_dict["selected_actions_url"] = selected_actions_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled_organizations = EnabledOrganizations(d.pop("enabled_organizations"))

        selected_organizations_url = d.pop("selected_organizations_url", UNSET)

        _allowed_actions = d.pop("allowed_actions", UNSET)
        allowed_actions: Union[Unset, AllowedActions]
        if isinstance(_allowed_actions, Unset):
            allowed_actions = UNSET
        else:
            allowed_actions = AllowedActions(_allowed_actions)

        selected_actions_url = d.pop("selected_actions_url", UNSET)

        actions_enterprise_permissions = cls(
            enabled_organizations=enabled_organizations,
            selected_organizations_url=selected_organizations_url,
            allowed_actions=allowed_actions,
            selected_actions_url=selected_actions_url,
        )

        actions_enterprise_permissions.additional_properties = d
        return actions_enterprise_permissions

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
