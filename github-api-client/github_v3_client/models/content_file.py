from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..models.content_file_links import ContentFileLinks
from ..models.content_file_type import ContentFileType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContentFile")


@attr.s(auto_attribs=True)
class ContentFile:
    """Content File

    Attributes:
        type (ContentFileType):
        encoding (str):
        size (int):
        name (str):
        path (str):
        content (str):
        sha (str):
        url (str):
        links (ContentFileLinks):
        git_url (Optional[str]):
        html_url (Optional[str]):
        download_url (Optional[str]):
        target (Union[Unset, str]):  Example: "actual/actual.md".
        submodule_git_url (Union[Unset, str]):  Example: "git://example.com/defunkt/dotjs.git".
    """

    type: ContentFileType
    encoding: str
    size: int
    name: str
    path: str
    content: str
    sha: str
    url: str
    links: ContentFileLinks
    git_url: Optional[str]
    html_url: Optional[str]
    download_url: Optional[str]
    target: Union[Unset, str] = UNSET
    submodule_git_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        encoding = self.encoding
        size = self.size
        name = self.name
        path = self.path
        content = self.content
        sha = self.sha
        url = self.url
        links = self.links.to_dict()

        git_url = self.git_url
        html_url = self.html_url
        download_url = self.download_url
        target = self.target
        submodule_git_url = self.submodule_git_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "encoding": encoding,
                "size": size,
                "name": name,
                "path": path,
                "content": content,
                "sha": sha,
                "url": url,
                "_links": links,
                "git_url": git_url,
                "html_url": html_url,
                "download_url": download_url,
            }
        )
        if target is not UNSET:
            field_dict["target"] = target
        if submodule_git_url is not UNSET:
            field_dict["submodule_git_url"] = submodule_git_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = ContentFileType(d.pop("type"))

        encoding = d.pop("encoding")

        size = d.pop("size")

        name = d.pop("name")

        path = d.pop("path")

        content = d.pop("content")

        sha = d.pop("sha")

        url = d.pop("url")

        links = ContentFileLinks.from_dict(d.pop("_links"))

        git_url = d.pop("git_url")

        html_url = d.pop("html_url")

        download_url = d.pop("download_url")

        target = d.pop("target", UNSET)

        submodule_git_url = d.pop("submodule_git_url", UNSET)

        content_file = cls(
            type=type,
            encoding=encoding,
            size=size,
            name=name,
            path=path,
            content=content,
            sha=sha,
            url=url,
            links=links,
            git_url=git_url,
            html_url=html_url,
            download_url=download_url,
            target=target,
            submodule_git_url=submodule_git_url,
        )

        content_file.additional_properties = d
        return content_file

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
