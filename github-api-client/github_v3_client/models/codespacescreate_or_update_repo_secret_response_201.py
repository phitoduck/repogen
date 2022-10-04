from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="CodespacescreateOrUpdateRepoSecretResponse201")


@attr.s(auto_attribs=True)
class CodespacescreateOrUpdateRepoSecretResponse201:
    """ """

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        src_dict.copy()
        codespacescreate_or_update_repo_secret_response_201 = cls()

        return codespacescreate_or_update_repo_secret_response_201
