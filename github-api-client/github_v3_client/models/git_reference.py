from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.git_reference_object import GitReferenceObject

T = TypeVar("T", bound="GitReference")


@attr.s(auto_attribs=True)
class GitReference:
    """Git references within a repository

    Attributes:
        ref (str):
        node_id (str):
        url (str):
        object_ (GitReferenceObject):
    """

    ref: str
    node_id: str
    url: str
    object_: GitReferenceObject
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ref = self.ref
        node_id = self.node_id
        url = self.url
        object_ = self.object_.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ref": ref,
                "node_id": node_id,
                "url": url,
                "object": object_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ref = d.pop("ref")

        node_id = d.pop("node_id")

        url = d.pop("url")

        object_ = GitReferenceObject.from_dict(d.pop("object"))

        git_reference = cls(
            ref=ref,
            node_id=node_id,
            url=url,
            object_=object_,
        )

        git_reference.additional_properties = d
        return git_reference

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
