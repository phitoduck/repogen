from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RunnerApplication")


@attr.s(auto_attribs=True)
class RunnerApplication:
    """Runner Application

    Attributes:
        os (str):
        architecture (str):
        download_url (str):
        filename (str):
        temp_download_token (Union[Unset, str]): A short lived bearer token used to download the runner, if needed.
        sha256_checksum (Union[Unset, str]):
    """

    os: str
    architecture: str
    download_url: str
    filename: str
    temp_download_token: Union[Unset, str] = UNSET
    sha256_checksum: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        os = self.os
        architecture = self.architecture
        download_url = self.download_url
        filename = self.filename
        temp_download_token = self.temp_download_token
        sha256_checksum = self.sha256_checksum

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "os": os,
                "architecture": architecture,
                "download_url": download_url,
                "filename": filename,
            }
        )
        if temp_download_token is not UNSET:
            field_dict["temp_download_token"] = temp_download_token
        if sha256_checksum is not UNSET:
            field_dict["sha256_checksum"] = sha256_checksum

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        os = d.pop("os")

        architecture = d.pop("architecture")

        download_url = d.pop("download_url")

        filename = d.pop("filename")

        temp_download_token = d.pop("temp_download_token", UNSET)

        sha256_checksum = d.pop("sha256_checksum", UNSET)

        runner_application = cls(
            os=os,
            architecture=architecture,
            download_url=download_url,
            filename=filename,
            temp_download_token=temp_download_token,
            sha256_checksum=sha256_checksum,
        )

        runner_application.additional_properties = d
        return runner_application

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
