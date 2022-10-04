from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.codespaceslist_devcontainers_in_repository_for_authenticated_user_response_200_devcontainers_item import (
    CodespaceslistDevcontainersInRepositoryForAuthenticatedUserResponse200DevcontainersItem,
)

T = TypeVar("T", bound="CodespaceslistDevcontainersInRepositoryForAuthenticatedUserResponse200")


@attr.s(auto_attribs=True)
class CodespaceslistDevcontainersInRepositoryForAuthenticatedUserResponse200:
    """
    Attributes:
        total_count (int):
        devcontainers (List[CodespaceslistDevcontainersInRepositoryForAuthenticatedUserResponse200DevcontainersItem]):
    """

    total_count: int
    devcontainers: List[CodespaceslistDevcontainersInRepositoryForAuthenticatedUserResponse200DevcontainersItem]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_count = self.total_count
        devcontainers = []
        for devcontainers_item_data in self.devcontainers:
            devcontainers_item = devcontainers_item_data.to_dict()

            devcontainers.append(devcontainers_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_count": total_count,
                "devcontainers": devcontainers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_count = d.pop("total_count")

        devcontainers = []
        _devcontainers = d.pop("devcontainers")
        for devcontainers_item_data in _devcontainers:
            devcontainers_item = (
                CodespaceslistDevcontainersInRepositoryForAuthenticatedUserResponse200DevcontainersItem.from_dict(
                    devcontainers_item_data
                )
            )

            devcontainers.append(devcontainers_item)

        codespaceslist_devcontainers_in_repository_for_authenticated_user_response_200 = cls(
            total_count=total_count,
            devcontainers=devcontainers,
        )

        codespaceslist_devcontainers_in_repository_for_authenticated_user_response_200.additional_properties = d
        return codespaceslist_devcontainers_in_repository_for_authenticated_user_response_200

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
