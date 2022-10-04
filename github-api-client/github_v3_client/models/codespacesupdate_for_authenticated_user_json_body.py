from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodespacesupdateForAuthenticatedUserJsonBody")


@attr.s(auto_attribs=True)
class CodespacesupdateForAuthenticatedUserJsonBody:
    """
    Attributes:
        machine (Union[Unset, str]): A valid machine to transition this codespace to.
        display_name (Union[Unset, str]): Display name for this codespace
        recent_folders (Union[Unset, List[str]]): Recently opened folders inside the codespace. It is currently used by
            the clients to determine the folder path to load the codespace in.
    """

    machine: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    recent_folders: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        machine = self.machine
        display_name = self.display_name
        recent_folders: Union[Unset, List[str]] = UNSET
        if not isinstance(self.recent_folders, Unset):
            recent_folders = self.recent_folders

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if machine is not UNSET:
            field_dict["machine"] = machine
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if recent_folders is not UNSET:
            field_dict["recent_folders"] = recent_folders

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        machine = d.pop("machine", UNSET)

        display_name = d.pop("display_name", UNSET)

        recent_folders = cast(List[str], d.pop("recent_folders", UNSET))

        codespacesupdate_for_authenticated_user_json_body = cls(
            machine=machine,
            display_name=display_name,
            recent_folders=recent_folders,
        )

        codespacesupdate_for_authenticated_user_json_body.additional_properties = d
        return codespacesupdate_for_authenticated_user_json_body

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
