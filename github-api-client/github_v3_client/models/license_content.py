from typing import Any, Dict, List, Optional, Type, TypeVar

import attr

from ..models.license_content_links import LicenseContentLinks
from ..models.license_simple import LicenseSimple

T = TypeVar("T", bound="LicenseContent")


@attr.s(auto_attribs=True)
class LicenseContent:
    """License Content

    Attributes:
        name (str):
        path (str):
        sha (str):
        size (int):
        url (str):
        type (str):
        content (str):
        encoding (str):
        links (LicenseContentLinks):
        html_url (Optional[str]):
        git_url (Optional[str]):
        download_url (Optional[str]):
        license_ (Optional[LicenseSimple]): License Simple
    """

    name: str
    path: str
    sha: str
    size: int
    url: str
    type: str
    content: str
    encoding: str
    links: LicenseContentLinks
    html_url: Optional[str]
    git_url: Optional[str]
    download_url: Optional[str]
    license_: Optional[LicenseSimple]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        path = self.path
        sha = self.sha
        size = self.size
        url = self.url
        type = self.type
        content = self.content
        encoding = self.encoding
        links = self.links.to_dict()

        html_url = self.html_url
        git_url = self.git_url
        download_url = self.download_url
        license_ = self.license_.to_dict() if self.license_ else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "path": path,
                "sha": sha,
                "size": size,
                "url": url,
                "type": type,
                "content": content,
                "encoding": encoding,
                "_links": links,
                "html_url": html_url,
                "git_url": git_url,
                "download_url": download_url,
                "license": license_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        path = d.pop("path")

        sha = d.pop("sha")

        size = d.pop("size")

        url = d.pop("url")

        type = d.pop("type")

        content = d.pop("content")

        encoding = d.pop("encoding")

        links = LicenseContentLinks.from_dict(d.pop("_links"))

        html_url = d.pop("html_url")

        git_url = d.pop("git_url")

        download_url = d.pop("download_url")

        _license_ = d.pop("license")
        license_: Optional[LicenseSimple]
        if _license_ is None:
            license_ = None
        else:
            license_ = LicenseSimple.from_dict(_license_)

        license_content = cls(
            name=name,
            path=path,
            sha=sha,
            size=size,
            url=url,
            type=type,
            content=content,
            encoding=encoding,
            links=links,
            html_url=html_url,
            git_url=git_url,
            download_url=download_url,
            license_=license_,
        )

        license_content.additional_properties = d
        return license_content

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
