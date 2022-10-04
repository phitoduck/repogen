from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.gitcreate_tree_json_body_tree_item import GitcreateTreeJsonBodyTreeItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="GitcreateTreeJsonBody")


@attr.s(auto_attribs=True)
class GitcreateTreeJsonBody:
    """
    Attributes:
        tree (List[GitcreateTreeJsonBodyTreeItem]): Objects (of `path`, `mode`, `type`, and `sha`) specifying a tree
            structure.
        base_tree (Union[Unset, str]): The SHA1 of an existing Git tree object which will be used as the base for the
            new tree. If provided, a new Git tree object will be created from entries in the Git tree object pointed to by
            `base_tree` and entries defined in the `tree` parameter. Entries defined in the `tree` parameter will overwrite
            items from `base_tree` with the same `path`. If you're creating new changes on a branch, then normally you'd set
            `base_tree` to the SHA1 of the Git tree object of the current latest commit on the branch you're working on.
            If not provided, GitHub will create a new Git tree object from only the entries defined in the `tree` parameter.
            If you create a new commit pointing to such a tree, then all files which were a part of the parent commit's tree
            and were not defined in the `tree` parameter will be listed as deleted by the new commit.
    """

    tree: List[GitcreateTreeJsonBodyTreeItem]
    base_tree: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tree = []
        for tree_item_data in self.tree:
            tree_item = tree_item_data.to_dict()

            tree.append(tree_item)

        base_tree = self.base_tree

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tree": tree,
            }
        )
        if base_tree is not UNSET:
            field_dict["base_tree"] = base_tree

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tree = []
        _tree = d.pop("tree")
        for tree_item_data in _tree:
            tree_item = GitcreateTreeJsonBodyTreeItem.from_dict(tree_item_data)

            tree.append(tree_item)

        base_tree = d.pop("base_tree", UNSET)

        gitcreate_tree_json_body = cls(
            tree=tree,
            base_tree=base_tree,
        )

        gitcreate_tree_json_body.additional_properties = d
        return gitcreate_tree_json_body

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
