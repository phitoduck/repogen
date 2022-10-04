from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.file_commit_content_links import FileCommitContentLinks
from ..types import UNSET, Unset

T = TypeVar("T", bound="FileCommitContent")


@attr.s(auto_attribs=True)
class FileCommitContent:
    """
    Attributes:
        name (Union[Unset, str]):
        path (Union[Unset, str]):
        sha (Union[Unset, str]):
        size (Union[Unset, int]):
        url (Union[Unset, str]):
        html_url (Union[Unset, str]):
        git_url (Union[Unset, str]):
        download_url (Union[Unset, str]):
        type (Union[Unset, str]):
        links (Union[Unset, FileCommitContentLinks]):
    """

    name: Union[Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    sha: Union[Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    url: Union[Unset, str] = UNSET
    html_url: Union[Unset, str] = UNSET
    git_url: Union[Unset, str] = UNSET
    download_url: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    links: Union[Unset, FileCommitContentLinks] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        path = self.path
        sha = self.sha
        size = self.size
        url = self.url
        html_url = self.html_url
        git_url = self.git_url
        download_url = self.download_url
        type = self.type
        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if path is not UNSET:
            field_dict["path"] = path
        if sha is not UNSET:
            field_dict["sha"] = sha
        if size is not UNSET:
            field_dict["size"] = size
        if url is not UNSET:
            field_dict["url"] = url
        if html_url is not UNSET:
            field_dict["html_url"] = html_url
        if git_url is not UNSET:
            field_dict["git_url"] = git_url
        if download_url is not UNSET:
            field_dict["download_url"] = download_url
        if type is not UNSET:
            field_dict["type"] = type
        if links is not UNSET:
            field_dict["_links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        path = d.pop("path", UNSET)

        sha = d.pop("sha", UNSET)

        size = d.pop("size", UNSET)

        url = d.pop("url", UNSET)

        html_url = d.pop("html_url", UNSET)

        git_url = d.pop("git_url", UNSET)

        download_url = d.pop("download_url", UNSET)

        type = d.pop("type", UNSET)

        _links = d.pop("_links", UNSET)
        links: Union[Unset, FileCommitContentLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = FileCommitContentLinks.from_dict(_links)

        file_commit_content = cls(
            name=name,
            path=path,
            sha=sha,
            size=size,
            url=url,
            html_url=html_url,
            git_url=git_url,
            download_url=download_url,
            type=type,
            links=links,
        )

        file_commit_content.additional_properties = d
        return file_commit_content

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
