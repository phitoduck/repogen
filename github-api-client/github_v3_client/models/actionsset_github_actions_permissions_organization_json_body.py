from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.allowed_actions import AllowedActions
from ..models.enabled_repositories import EnabledRepositories
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActionssetGithubActionsPermissionsOrganizationJsonBody")


@attr.s(auto_attribs=True)
class ActionssetGithubActionsPermissionsOrganizationJsonBody:
    """
    Attributes:
        enabled_repositories (EnabledRepositories): The policy that controls the repositories in the organization that
            are allowed to run GitHub Actions.
        allowed_actions (Union[Unset, AllowedActions]): The permissions policy that controls the actions and reusable
            workflows that are allowed to run.
    """

    enabled_repositories: EnabledRepositories
    allowed_actions: Union[Unset, AllowedActions] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled_repositories = self.enabled_repositories.value

        allowed_actions: Union[Unset, str] = UNSET
        if not isinstance(self.allowed_actions, Unset):
            allowed_actions = self.allowed_actions.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled_repositories": enabled_repositories,
            }
        )
        if allowed_actions is not UNSET:
            field_dict["allowed_actions"] = allowed_actions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled_repositories = EnabledRepositories(d.pop("enabled_repositories"))

        _allowed_actions = d.pop("allowed_actions", UNSET)
        allowed_actions: Union[Unset, AllowedActions]
        if isinstance(_allowed_actions, Unset):
            allowed_actions = UNSET
        else:
            allowed_actions = AllowedActions(_allowed_actions)

        actionsset_github_actions_permissions_organization_json_body = cls(
            enabled_repositories=enabled_repositories,
            allowed_actions=allowed_actions,
        )

        actionsset_github_actions_permissions_organization_json_body.additional_properties = d
        return actionsset_github_actions_permissions_organization_json_body

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
