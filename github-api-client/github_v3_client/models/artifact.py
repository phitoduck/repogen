import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.artifact_workflow_run import ArtifactWorkflowRun
from ..types import UNSET, Unset

T = TypeVar("T", bound="Artifact")


@attr.s(auto_attribs=True)
class Artifact:
    """An artifact

    Attributes:
        id (int):  Example: 5.
        node_id (str):  Example: MDEwOkNoZWNrU3VpdGU1.
        name (str): The name of the artifact. Example: AdventureWorks.Framework.
        size_in_bytes (int): The size in bytes of the artifact. Example: 12345.
        url (str):  Example: https://api.github.com/repos/github/hello-world/actions/artifacts/5.
        archive_download_url (str):  Example: https://api.github.com/repos/github/hello-world/actions/artifacts/5/zip.
        expired (bool): Whether or not the artifact has expired.
        created_at (Optional[datetime.datetime]):
        expires_at (Optional[datetime.datetime]):
        updated_at (Optional[datetime.datetime]):
        workflow_run (Union[Unset, None, ArtifactWorkflowRun]):
    """

    id: int
    node_id: str
    name: str
    size_in_bytes: int
    url: str
    archive_download_url: str
    expired: bool
    created_at: Optional[datetime.datetime]
    expires_at: Optional[datetime.datetime]
    updated_at: Optional[datetime.datetime]
    workflow_run: Union[Unset, None, ArtifactWorkflowRun] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        node_id = self.node_id
        name = self.name
        size_in_bytes = self.size_in_bytes
        url = self.url
        archive_download_url = self.archive_download_url
        expired = self.expired
        created_at = self.created_at.isoformat() if self.created_at else None

        expires_at = self.expires_at.isoformat() if self.expires_at else None

        updated_at = self.updated_at.isoformat() if self.updated_at else None

        workflow_run: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.workflow_run, Unset):
            workflow_run = self.workflow_run.to_dict() if self.workflow_run else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "node_id": node_id,
                "name": name,
                "size_in_bytes": size_in_bytes,
                "url": url,
                "archive_download_url": archive_download_url,
                "expired": expired,
                "created_at": created_at,
                "expires_at": expires_at,
                "updated_at": updated_at,
            }
        )
        if workflow_run is not UNSET:
            field_dict["workflow_run"] = workflow_run

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        node_id = d.pop("node_id")

        name = d.pop("name")

        size_in_bytes = d.pop("size_in_bytes")

        url = d.pop("url")

        archive_download_url = d.pop("archive_download_url")

        expired = d.pop("expired")

        _created_at = d.pop("created_at")
        created_at: Optional[datetime.datetime]
        if _created_at is None:
            created_at = None
        else:
            created_at = isoparse(_created_at)

        _expires_at = d.pop("expires_at")
        expires_at: Optional[datetime.datetime]
        if _expires_at is None:
            expires_at = None
        else:
            expires_at = isoparse(_expires_at)

        _updated_at = d.pop("updated_at")
        updated_at: Optional[datetime.datetime]
        if _updated_at is None:
            updated_at = None
        else:
            updated_at = isoparse(_updated_at)

        _workflow_run = d.pop("workflow_run", UNSET)
        workflow_run: Union[Unset, None, ArtifactWorkflowRun]
        if _workflow_run is None:
            workflow_run = None
        elif isinstance(_workflow_run, Unset):
            workflow_run = UNSET
        else:
            workflow_run = ArtifactWorkflowRun.from_dict(_workflow_run)

        artifact = cls(
            id=id,
            node_id=node_id,
            name=name,
            size_in_bytes=size_in_bytes,
            url=url,
            archive_download_url=archive_download_url,
            expired=expired,
            created_at=created_at,
            expires_at=expires_at,
            updated_at=updated_at,
            workflow_run=workflow_run,
        )

        artifact.additional_properties = d
        return artifact

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
