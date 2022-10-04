from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.tag_commit import TagCommit

T = TypeVar("T", bound="Tag")


@attr.s(auto_attribs=True)
class Tag:
    """Tag

    Attributes:
        name (str):  Example: v0.1.
        commit (TagCommit):
        zipball_url (str):  Example: https://github.com/octocat/Hello-World/zipball/v0.1.
        tarball_url (str):  Example: https://github.com/octocat/Hello-World/tarball/v0.1.
        node_id (str):
    """

    name: str
    commit: TagCommit
    zipball_url: str
    tarball_url: str
    node_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        commit = self.commit.to_dict()

        zipball_url = self.zipball_url
        tarball_url = self.tarball_url
        node_id = self.node_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "commit": commit,
                "zipball_url": zipball_url,
                "tarball_url": tarball_url,
                "node_id": node_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        commit = TagCommit.from_dict(d.pop("commit"))

        zipball_url = d.pop("zipball_url")

        tarball_url = d.pop("tarball_url")

        node_id = d.pop("node_id")

        tag = cls(
            name=name,
            commit=commit,
            zipball_url=zipball_url,
            tarball_url=tarball_url,
            node_id=node_id,
        )

        tag.additional_properties = d
        return tag

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
