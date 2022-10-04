from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.migrationsstart_import_json_body_vcs import MigrationsstartImportJsonBodyVcs
from ..types import UNSET, Unset

T = TypeVar("T", bound="MigrationsstartImportJsonBody")


@attr.s(auto_attribs=True)
class MigrationsstartImportJsonBody:
    """
    Attributes:
        vcs_url (str): The URL of the originating repository.
        vcs (Union[Unset, MigrationsstartImportJsonBodyVcs]): The originating VCS type. Without this parameter, the
            import job will take additional time to detect the VCS type before beginning the import. This detection step
            will be reflected in the response.
        vcs_username (Union[Unset, str]): If authentication is required, the username to provide to `vcs_url`.
        vcs_password (Union[Unset, str]): If authentication is required, the password to provide to `vcs_url`.
        tfvc_project (Union[Unset, str]): For a tfvc import, the name of the project that is being imported.
    """

    vcs_url: str
    vcs: Union[Unset, MigrationsstartImportJsonBodyVcs] = UNSET
    vcs_username: Union[Unset, str] = UNSET
    vcs_password: Union[Unset, str] = UNSET
    tfvc_project: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        vcs_url = self.vcs_url
        vcs: Union[Unset, str] = UNSET
        if not isinstance(self.vcs, Unset):
            vcs = self.vcs.value

        vcs_username = self.vcs_username
        vcs_password = self.vcs_password
        tfvc_project = self.tfvc_project

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vcs_url": vcs_url,
            }
        )
        if vcs is not UNSET:
            field_dict["vcs"] = vcs
        if vcs_username is not UNSET:
            field_dict["vcs_username"] = vcs_username
        if vcs_password is not UNSET:
            field_dict["vcs_password"] = vcs_password
        if tfvc_project is not UNSET:
            field_dict["tfvc_project"] = tfvc_project

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        vcs_url = d.pop("vcs_url")

        _vcs = d.pop("vcs", UNSET)
        vcs: Union[Unset, MigrationsstartImportJsonBodyVcs]
        if isinstance(_vcs, Unset):
            vcs = UNSET
        else:
            vcs = MigrationsstartImportJsonBodyVcs(_vcs)

        vcs_username = d.pop("vcs_username", UNSET)

        vcs_password = d.pop("vcs_password", UNSET)

        tfvc_project = d.pop("tfvc_project", UNSET)

        migrationsstart_import_json_body = cls(
            vcs_url=vcs_url,
            vcs=vcs,
            vcs_username=vcs_username,
            vcs_password=vcs_password,
            tfvc_project=tfvc_project,
        )

        migrationsstart_import_json_body.additional_properties = d
        return migrationsstart_import_json_body

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
