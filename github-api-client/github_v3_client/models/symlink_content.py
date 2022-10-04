from typing import Any, Dict, List, Optional, Type, TypeVar

import attr

from ..models.symlink_content_links import SymlinkContentLinks
from ..models.symlink_content_type import SymlinkContentType

T = TypeVar("T", bound="SymlinkContent")


@attr.s(auto_attribs=True)
class SymlinkContent:
    """An object describing a symlink

    Attributes:
        type (SymlinkContentType):
        target (str):
        size (int):
        name (str):
        path (str):
        sha (str):
        url (str):
        links (SymlinkContentLinks):
        git_url (Optional[str]):
        html_url (Optional[str]):
        download_url (Optional[str]):
    """

    type: SymlinkContentType
    target: str
    size: int
    name: str
    path: str
    sha: str
    url: str
    links: SymlinkContentLinks
    git_url: Optional[str]
    html_url: Optional[str]
    download_url: Optional[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        target = self.target
        size = self.size
        name = self.name
        path = self.path
        sha = self.sha
        url = self.url
        links = self.links.to_dict()

        git_url = self.git_url
        html_url = self.html_url
        download_url = self.download_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "target": target,
                "size": size,
                "name": name,
                "path": path,
                "sha": sha,
                "url": url,
                "_links": links,
                "git_url": git_url,
                "html_url": html_url,
                "download_url": download_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = SymlinkContentType(d.pop("type"))

        target = d.pop("target")

        size = d.pop("size")

        name = d.pop("name")

        path = d.pop("path")

        sha = d.pop("sha")

        url = d.pop("url")

        links = SymlinkContentLinks.from_dict(d.pop("_links"))

        git_url = d.pop("git_url")

        html_url = d.pop("html_url")

        download_url = d.pop("download_url")

        symlink_content = cls(
            type=type,
            target=target,
            size=size,
            name=name,
            path=path,
            sha=sha,
            url=url,
            links=links,
            git_url=git_url,
            html_url=html_url,
            download_url=download_url,
        )

        symlink_content.additional_properties = d
        return symlink_content

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
