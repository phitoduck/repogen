import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.dependabot_secret_for_an_organization_visibility import DependabotSecretForAnOrganizationVisibility
from ..types import UNSET, Unset

T = TypeVar("T", bound="DependabotSecretForAnOrganization")


@attr.s(auto_attribs=True)
class DependabotSecretForAnOrganization:
    """Secrets for GitHub Dependabot for an organization.

    Attributes:
        name (str): The name of the secret. Example: SECRET_TOKEN.
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        visibility (DependabotSecretForAnOrganizationVisibility): Visibility of a secret
        selected_repositories_url (Union[Unset, str]):  Example:
            https://api.github.com/organizations/org/dependabot/secrets/my_secret/repositories.
    """

    name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    visibility: DependabotSecretForAnOrganizationVisibility
    selected_repositories_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        visibility = self.visibility.value

        selected_repositories_url = self.selected_repositories_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "created_at": created_at,
                "updated_at": updated_at,
                "visibility": visibility,
            }
        )
        if selected_repositories_url is not UNSET:
            field_dict["selected_repositories_url"] = selected_repositories_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        visibility = DependabotSecretForAnOrganizationVisibility(d.pop("visibility"))

        selected_repositories_url = d.pop("selected_repositories_url", UNSET)

        dependabot_secret_for_an_organization = cls(
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            visibility=visibility,
            selected_repositories_url=selected_repositories_url,
        )

        dependabot_secret_for_an_organization.additional_properties = d
        return dependabot_secret_for_an_organization

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
