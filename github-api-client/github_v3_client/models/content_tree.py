from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..models.content_tree_entries_item import ContentTreeEntriesItem
from ..models.content_tree_links import ContentTreeLinks
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContentTree")


@attr.s(auto_attribs=True)
class ContentTree:
    """Content Tree

    Attributes:
        type (str):
        size (int):
        name (str):
        path (str):
        sha (str):
        url (str):
        links (ContentTreeLinks):
        git_url (Optional[str]):
        html_url (Optional[str]):
        download_url (Optional[str]):
        entries (Union[Unset, List[ContentTreeEntriesItem]]):
    """

    type: str
    size: int
    name: str
    path: str
    sha: str
    url: str
    links: ContentTreeLinks
    git_url: Optional[str]
    html_url: Optional[str]
    download_url: Optional[str]
    entries: Union[Unset, List[ContentTreeEntriesItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        size = self.size
        name = self.name
        path = self.path
        sha = self.sha
        url = self.url
        links = self.links.to_dict()

        git_url = self.git_url
        html_url = self.html_url
        download_url = self.download_url
        entries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()

                entries.append(entries_item)

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
        if entries is not UNSET:
            field_dict["entries"] = entries

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

        links = ContentTreeLinks.from_dict(d.pop("_links"))

        git_url = d.pop("git_url")

        html_url = d.pop("html_url")

        download_url = d.pop("download_url")

        entries = []
        _entries = d.pop("entries", UNSET)
        for entries_item_data in _entries or []:
            entries_item = ContentTreeEntriesItem.from_dict(entries_item_data)

            entries.append(entries_item)

        content_tree = cls(
            type=type,
            size=size,
            name=name,
            path=path,
            sha=sha,
            url=url,
            links=links,
            git_url=git_url,
            html_url=html_url,
            download_url=download_url,
            entries=entries,
        )

        content_tree.additional_properties = d
        return content_tree

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
