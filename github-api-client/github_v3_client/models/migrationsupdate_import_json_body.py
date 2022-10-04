from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.migrationsupdate_import_json_body_vcs import MigrationsupdateImportJsonBodyVcs
from ..types import UNSET, Unset

T = TypeVar("T", bound="MigrationsupdateImportJsonBody")


@attr.s(auto_attribs=True)
class MigrationsupdateImportJsonBody:
    """
    Attributes:
        vcs_username (Union[Unset, str]): The username to provide to the originating repository.
        vcs_password (Union[Unset, str]): The password to provide to the originating repository.
        vcs (Union[Unset, MigrationsupdateImportJsonBodyVcs]): The type of version control system you are migrating
            from. Example: "git".
        tfvc_project (Union[Unset, str]): For a tfvc import, the name of the project that is being imported. Example:
            "project1".
    """

    vcs_username: Union[Unset, str] = UNSET
    vcs_password: Union[Unset, str] = UNSET
    vcs: Union[Unset, MigrationsupdateImportJsonBodyVcs] = UNSET
    tfvc_project: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        vcs_username = self.vcs_username
        vcs_password = self.vcs_password
        vcs: Union[Unset, str] = UNSET
        if not isinstance(self.vcs, Unset):
            vcs = self.vcs.value

        tfvc_project = self.tfvc_project

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vcs_username is not UNSET:
            field_dict["vcs_username"] = vcs_username
        if vcs_password is not UNSET:
            field_dict["vcs_password"] = vcs_password
        if vcs is not UNSET:
            field_dict["vcs"] = vcs
        if tfvc_project is not UNSET:
            field_dict["tfvc_project"] = tfvc_project

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        vcs_username = d.pop("vcs_username", UNSET)

        vcs_password = d.pop("vcs_password", UNSET)

        _vcs = d.pop("vcs", UNSET)
        vcs: Union[Unset, MigrationsupdateImportJsonBodyVcs]
        if isinstance(_vcs, Unset):
            vcs = UNSET
        else:
            vcs = MigrationsupdateImportJsonBodyVcs(_vcs)

        tfvc_project = d.pop("tfvc_project", UNSET)

        migrationsupdate_import_json_body = cls(
            vcs_username=vcs_username,
            vcs_password=vcs_password,
            vcs=vcs,
            tfvc_project=tfvc_project,
        )

        migrationsupdate_import_json_body.additional_properties = d
        return migrationsupdate_import_json_body

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
