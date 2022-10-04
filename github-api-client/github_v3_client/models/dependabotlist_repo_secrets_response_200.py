from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.dependabot_secret import DependabotSecret

T = TypeVar("T", bound="DependabotlistRepoSecretsResponse200")


@attr.s(auto_attribs=True)
class DependabotlistRepoSecretsResponse200:
    """
    Attributes:
        total_count (int):
        secrets (List[DependabotSecret]):
    """

    total_count: int
    secrets: List[DependabotSecret]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_count = self.total_count
        secrets = []
        for secrets_item_data in self.secrets:
            secrets_item = secrets_item_data.to_dict()

            secrets.append(secrets_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_count": total_count,
                "secrets": secrets,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_count = d.pop("total_count")

        secrets = []
        _secrets = d.pop("secrets")
        for secrets_item_data in _secrets:
            secrets_item = DependabotSecret.from_dict(secrets_item_data)

            secrets.append(secrets_item)

        dependabotlist_repo_secrets_response_200 = cls(
            total_count=total_count,
            secrets=secrets,
        )

        dependabotlist_repo_secrets_response_200.additional_properties = d
        return dependabotlist_repo_secrets_response_200

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
