from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodespaceslistDevcontainersInRepositoryForAuthenticatedUserResponse200DevcontainersItem")


@attr.s(auto_attribs=True)
class CodespaceslistDevcontainersInRepositoryForAuthenticatedUserResponse200DevcontainersItem:
    """
    Attributes:
        path (str):
        name (Union[Unset, str]):
    """

    path: str
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        path = self.path
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        path = d.pop("path")

        name = d.pop("name", UNSET)

        codespaceslist_devcontainers_in_repository_for_authenticated_user_response_200_devcontainers_item = cls(
            path=path,
            name=name,
        )

        codespaceslist_devcontainers_in_repository_for_authenticated_user_response_200_devcontainers_item.additional_properties = (
            d
        )
        return codespaceslist_devcontainers_in_repository_for_authenticated_user_response_200_devcontainers_item

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
