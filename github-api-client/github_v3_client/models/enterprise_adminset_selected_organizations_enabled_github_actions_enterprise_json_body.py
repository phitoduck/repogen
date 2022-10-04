from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="EnterpriseAdminsetSelectedOrganizationsEnabledGithubActionsEnterpriseJsonBody")


@attr.s(auto_attribs=True)
class EnterpriseAdminsetSelectedOrganizationsEnabledGithubActionsEnterpriseJsonBody:
    """
    Attributes:
        selected_organization_ids (List[int]): List of organization IDs to enable for GitHub Actions.
    """

    selected_organization_ids: List[int]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        selected_organization_ids = self.selected_organization_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "selected_organization_ids": selected_organization_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        selected_organization_ids = cast(List[int], d.pop("selected_organization_ids"))

        enterprise_adminset_selected_organizations_enabled_github_actions_enterprise_json_body = cls(
            selected_organization_ids=selected_organization_ids,
        )

        enterprise_adminset_selected_organizations_enabled_github_actions_enterprise_json_body.additional_properties = d
        return enterprise_adminset_selected_organizations_enabled_github_actions_enterprise_json_body

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
