from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.git_tree_tree_item import GitTreeTreeItem

T = TypeVar("T", bound="GitTree")


@attr.s(auto_attribs=True)
class GitTree:
    """The hierarchy between files in a Git repository.

    Attributes:
        sha (str):
        url (str):
        truncated (bool):
        tree (List[GitTreeTreeItem]): Objects specifying a tree structure Example: [{'path': 'file.rb', 'mode':
            '100644', 'type': 'blob', 'size': 30, 'sha': '44b4fc6d56897b048c772eb4087f854f46256132', 'url':
            'https://api.github.com/repos/octocat/Hello-World/git/blobs/44b4fc6d56897b048c772eb4087f854f46256132',
            'properties': {'path': {'type': 'string'}, 'mode': {'type': 'string'}, 'type': {'type': 'string'}, 'size':
            {'type': 'integer'}, 'sha': {'type': 'string'}, 'url': {'type': 'string'}}, 'required': ['path', 'mode', 'type',
            'sha', 'url', 'size']}].
    """

    sha: str
    url: str
    truncated: bool
    tree: List[GitTreeTreeItem]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sha = self.sha
        url = self.url
        truncated = self.truncated
        tree = []
        for tree_item_data in self.tree:
            tree_item = tree_item_data.to_dict()

            tree.append(tree_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sha": sha,
                "url": url,
                "truncated": truncated,
                "tree": tree,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sha = d.pop("sha")

        url = d.pop("url")

        truncated = d.pop("truncated")

        tree = []
        _tree = d.pop("tree")
        for tree_item_data in _tree:
            tree_item = GitTreeTreeItem.from_dict(tree_item_data)

            tree.append(tree_item)

        git_tree = cls(
            sha=sha,
            url=url,
            truncated=truncated,
            tree=tree,
        )

        git_tree.additional_properties = d
        return git_tree

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
