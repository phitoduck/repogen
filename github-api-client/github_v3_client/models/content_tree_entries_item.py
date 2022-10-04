from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..models.content_tree_entries_item_links import ContentTreeEntriesItemLinks
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContentTreeEntriesItem")


@attr.s(auto_attribs=True)
class ContentTreeEntriesItem:
    """
    Attributes:
        type (str):
        size (int):
        name (str):
        path (str):
        sha (str):
        url (str):
        links (ContentTreeEntriesItemLinks):
        content (Union[Unset, str]):
        git_url (Optional[str]):
        html_url (Optional[str]):
        download_url (Optional[str]):
    """

    type: str
    size: int
    name: str
    path: str
    sha: str
    url: str
    links: ContentTreeEntriesItemLinks
    git_url: Optional[str]
    html_url: Optional[str]
    download_url: Optional[str]
    content: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        size = self.size
        name = self.name
        path = self.path
        sha = self.sha
        url = self.url
        links = self.links.to_dict()

        content = self.content
        git_url = self.git_url
        html_url = self.html_url
        download_url = self.download_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
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
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        size = d.pop("size")

        name = d.pop("name")

        path = d.pop("path")

        sha = d.pop("sha")

        url = d.pop("url")

        links = ContentTreeEntriesItemLinks.from_dict(d.pop("_links"))

        content = d.pop("content", UNSET)

        git_url = d.pop("git_url")

        html_url = d.pop("html_url")

        download_url = d.pop("download_url")

        content_tree_entries_item = cls(
            type=type,
            size=size,
            name=name,
            path=path,
            sha=sha,
            url=url,
            links=links,
            content=content,
            git_url=git_url,
            html_url=html_url,
            download_url=download_url,
        )

        content_tree_entries_item.additional_properties = d
        return content_tree_entries_item

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
