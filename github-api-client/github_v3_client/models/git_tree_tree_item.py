from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GitTreeTreeItem")


@attr.s(auto_attribs=True)
class GitTreeTreeItem:
    """
    Attributes:
        path (Union[Unset, str]):  Example: test/file.rb.
        mode (Union[Unset, str]):  Example: 040000.
        type (Union[Unset, str]):  Example: tree.
        sha (Union[Unset, str]):  Example: 23f6827669e43831def8a7ad935069c8bd418261.
        size (Union[Unset, int]):  Example: 12.
        url (Union[Unset, str]):  Example: https://api.github.com/repos/owner-
            482f3203ecf01f67e9deb18e/BBB_Private_Repo/git/blobs/23f6827669e43831def8a7ad935069c8bd418261.
    """

    path: Union[Unset, str] = UNSET
    mode: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    sha: Union[Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        path = self.path
        mode = self.mode
        type = self.type
        sha = self.sha
        size = self.size
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if mode is not UNSET:
            field_dict["mode"] = mode
        if type is not UNSET:
            field_dict["type"] = type
        if sha is not UNSET:
            field_dict["sha"] = sha
        if size is not UNSET:
            field_dict["size"] = size
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        path = d.pop("path", UNSET)

        mode = d.pop("mode", UNSET)

        type = d.pop("type", UNSET)

        sha = d.pop("sha", UNSET)

        size = d.pop("size", UNSET)

        url = d.pop("url", UNSET)

        git_tree_tree_item = cls(
            path=path,
            mode=mode,
            type=type,
            sha=sha,
            size=size,
            url=url,
        )

        git_tree_tree_item.additional_properties = d
        return git_tree_tree_item

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
