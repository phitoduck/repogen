from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReposcreateDeployKeyJsonBody")


@attr.s(auto_attribs=True)
class ReposcreateDeployKeyJsonBody:
    """
    Attributes:
        key (str): The contents of the key.
        title (Union[Unset, str]): A name for the key.
        read_only (Union[Unset, bool]): If `true`, the key will only be able to read repository contents. Otherwise, the
            key will be able to read and write.

            Deploy keys with write access can perform the same actions as an organization member with admin access, or a
            collaborator on a personal repository. For more information, see "[Repository permission levels for an
            organization](https://docs.github.com/articles/repository-permission-levels-for-an-organization/)" and
            "[Permission levels for a user account repository](https://docs.github.com/articles/permission-levels-for-a-
            user-account-repository/)."
    """

    key: str
    title: Union[Unset, str] = UNSET
    read_only: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key
        title = self.title
        read_only = self.read_only

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if read_only is not UNSET:
            field_dict["read_only"] = read_only

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key = d.pop("key")

        title = d.pop("title", UNSET)

        read_only = d.pop("read_only", UNSET)

        reposcreate_deploy_key_json_body = cls(
            key=key,
            title=title,
            read_only=read_only,
        )

        reposcreate_deploy_key_json_body.additional_properties = d
        return reposcreate_deploy_key_json_body

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
