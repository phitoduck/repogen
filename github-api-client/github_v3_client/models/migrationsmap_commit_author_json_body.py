from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="MigrationsmapCommitAuthorJsonBody")


@attr.s(auto_attribs=True)
class MigrationsmapCommitAuthorJsonBody:
    """
    Attributes:
        email (Union[Unset, str]): The new Git author email.
        name (Union[Unset, str]): The new Git author name.
    """

    email: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        email = self.email
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email", UNSET)

        name = d.pop("name", UNSET)

        migrationsmap_commit_author_json_body = cls(
            email=email,
            name=name,
        )

        return migrationsmap_commit_author_json_body
