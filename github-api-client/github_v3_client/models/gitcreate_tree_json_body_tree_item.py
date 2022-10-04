from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.gitcreate_tree_json_body_tree_item_mode import GitcreateTreeJsonBodyTreeItemMode
from ..models.gitcreate_tree_json_body_tree_item_type import GitcreateTreeJsonBodyTreeItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GitcreateTreeJsonBodyTreeItem")


@attr.s(auto_attribs=True)
class GitcreateTreeJsonBodyTreeItem:
    """
    Attributes:
        path (Union[Unset, str]): The file referenced in the tree.
        mode (Union[Unset, GitcreateTreeJsonBodyTreeItemMode]): The file mode; one of `100644` for file (blob), `100755`
            for executable (blob), `040000` for subdirectory (tree), `160000` for submodule (commit), or `120000` for a blob
            that specifies the path of a symlink.
        type (Union[Unset, GitcreateTreeJsonBodyTreeItemType]): Either `blob`, `tree`, or `commit`.
        sha (Union[Unset, None, str]): The SHA1 checksum ID of the object in the tree. Also called `tree.sha`. If the
            value is `null` then the file will be deleted.

            **Note:** Use either `tree.sha` or `content` to specify the contents of the entry. Using both `tree.sha` and
            `content` will return an error.
        content (Union[Unset, str]): The content you want this file to have. GitHub will write this blob out and use
            that SHA for this entry. Use either this, or `tree.sha`.

            **Note:** Use either `tree.sha` or `content` to specify the contents of the entry. Using both `tree.sha` and
            `content` will return an error.
    """

    path: Union[Unset, str] = UNSET
    mode: Union[Unset, GitcreateTreeJsonBodyTreeItemMode] = UNSET
    type: Union[Unset, GitcreateTreeJsonBodyTreeItemType] = UNSET
    sha: Union[Unset, None, str] = UNSET
    content: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        path = self.path
        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        sha = self.sha
        content = self.content

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
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        path = d.pop("path", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, GitcreateTreeJsonBodyTreeItemMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = GitcreateTreeJsonBodyTreeItemMode(_mode)

        _type = d.pop("type", UNSET)
        type: Union[Unset, GitcreateTreeJsonBodyTreeItemType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = GitcreateTreeJsonBodyTreeItemType(_type)

        sha = d.pop("sha", UNSET)

        content = d.pop("content", UNSET)

        gitcreate_tree_json_body_tree_item = cls(
            path=path,
            mode=mode,
            type=type,
            sha=sha,
            content=content,
        )

        gitcreate_tree_json_body_tree_item.additional_properties = d
        return gitcreate_tree_json_body_tree_item

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
