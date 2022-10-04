from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="CodespacessetRepositoriesForSecretForAuthenticatedUserJsonBody")


@attr.s(auto_attribs=True)
class CodespacessetRepositoriesForSecretForAuthenticatedUserJsonBody:
    """
    Attributes:
        selected_repository_ids (List[int]): An array of repository ids for which a codespace can access the secret. You
            can manage the list of selected repositories using the [List selected repositories for a user
            secret](https://docs.github.com/rest/reference/codespaces#list-selected-repositories-for-a-user-secret), [Add a
            selected repository to a user secret](https://docs.github.com/rest/reference/codespaces#add-a-selected-
            repository-to-a-user-secret), and [Remove a selected repository from a user
            secret](https://docs.github.com/rest/reference/codespaces#remove-a-selected-repository-from-a-user-secret)
            endpoints.
    """

    selected_repository_ids: List[int]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        selected_repository_ids = self.selected_repository_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "selected_repository_ids": selected_repository_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        selected_repository_ids = cast(List[int], d.pop("selected_repository_ids"))

        codespacesset_repositories_for_secret_for_authenticated_user_json_body = cls(
            selected_repository_ids=selected_repository_ids,
        )

        codespacesset_repositories_for_secret_for_authenticated_user_json_body.additional_properties = d
        return codespacesset_repositories_for_secret_for_authenticated_user_json_body

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
