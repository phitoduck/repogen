from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.organization_simple import OrganizationSimple

T = TypeVar("T", bound="EnterpriseAdminlistSelectedOrganizationsEnabledGithubActionsEnterpriseResponse200")


@attr.s(auto_attribs=True)
class EnterpriseAdminlistSelectedOrganizationsEnabledGithubActionsEnterpriseResponse200:
    """
    Attributes:
        total_count (float):
        organizations (List[OrganizationSimple]):
    """

    total_count: float
    organizations: List[OrganizationSimple]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_count = self.total_count
        organizations = []
        for organizations_item_data in self.organizations:
            organizations_item = organizations_item_data.to_dict()

            organizations.append(organizations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_count": total_count,
                "organizations": organizations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_count = d.pop("total_count")

        organizations = []
        _organizations = d.pop("organizations")
        for organizations_item_data in _organizations:
            organizations_item = OrganizationSimple.from_dict(organizations_item_data)

            organizations.append(organizations_item)

        enterprise_adminlist_selected_organizations_enabled_github_actions_enterprise_response_200 = cls(
            total_count=total_count,
            organizations=organizations,
        )

        enterprise_adminlist_selected_organizations_enabled_github_actions_enterprise_response_200.additional_properties = (
            d
        )
        return enterprise_adminlist_selected_organizations_enabled_github_actions_enterprise_response_200

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
