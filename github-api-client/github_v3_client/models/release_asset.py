import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.release_asset_state import ReleaseAssetState
from ..models.simple_user import SimpleUser

T = TypeVar("T", bound="ReleaseAsset")


@attr.s(auto_attribs=True)
class ReleaseAsset:
    """Data related to a release.

    Attributes:
        url (str):
        browser_download_url (str):
        id (int):
        node_id (str):
        name (str): The file name of the asset. Example: Team Environment.
        state (ReleaseAssetState): State of the release asset.
        content_type (str):
        size (int):
        download_count (int):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        label (Optional[str]):
        uploader (Optional[SimpleUser]): Simple User
    """

    url: str
    browser_download_url: str
    id: int
    node_id: str
    name: str
    state: ReleaseAssetState
    content_type: str
    size: int
    download_count: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    label: Optional[str]
    uploader: Optional[SimpleUser]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        browser_download_url = self.browser_download_url
        id = self.id
        node_id = self.node_id
        name = self.name
        state = self.state.value

        content_type = self.content_type
        size = self.size
        download_count = self.download_count
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        label = self.label
        uploader = self.uploader.to_dict() if self.uploader else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "browser_download_url": browser_download_url,
                "id": id,
                "node_id": node_id,
                "name": name,
                "state": state,
                "content_type": content_type,
                "size": size,
                "download_count": download_count,
                "created_at": created_at,
                "updated_at": updated_at,
                "label": label,
                "uploader": uploader,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        browser_download_url = d.pop("browser_download_url")

        id = d.pop("id")

        node_id = d.pop("node_id")

        name = d.pop("name")

        state = ReleaseAssetState(d.pop("state"))

        content_type = d.pop("content_type")

        size = d.pop("size")

        download_count = d.pop("download_count")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        label = d.pop("label")

        _uploader = d.pop("uploader")
        uploader: Optional[SimpleUser]
        if _uploader is None:
            uploader = None
        else:
            uploader = SimpleUser.from_dict(_uploader)

        release_asset = cls(
            url=url,
            browser_download_url=browser_download_url,
            id=id,
            node_id=node_id,
            name=name,
            state=state,
            content_type=content_type,
            size=size,
            download_count=download_count,
            created_at=created_at,
            updated_at=updated_at,
            label=label,
            uploader=uploader,
        )

        release_asset.additional_properties = d
        return release_asset

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
