from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.git_tag_object import GitTagObject
from ..models.git_tag_tagger import GitTagTagger
from ..models.verification import Verification
from ..types import UNSET, Unset

T = TypeVar("T", bound="GitTag")


@attr.s(auto_attribs=True)
class GitTag:
    """Metadata for a Git tag

    Attributes:
        node_id (str):  Example: MDM6VGFnOTQwYmQzMzYyNDhlZmFlMGY5ZWU1YmM3YjJkNWM5ODU4ODdiMTZhYw==.
        tag (str): Name of the tag Example: v0.0.1.
        sha (str):  Example: 940bd336248efae0f9ee5bc7b2d5c985887b16ac.
        url (str): URL for the tag Example:
            https://api.github.com/repositories/42/git/tags/940bd336248efae0f9ee5bc7b2d5c985887b16ac.
        message (str): Message describing the purpose of the tag Example: Initial public release.
        tagger (GitTagTagger):
        object_ (GitTagObject):
        verification (Union[Unset, Verification]):
    """

    node_id: str
    tag: str
    sha: str
    url: str
    message: str
    tagger: GitTagTagger
    object_: GitTagObject
    verification: Union[Unset, Verification] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        node_id = self.node_id
        tag = self.tag
        sha = self.sha
        url = self.url
        message = self.message
        tagger = self.tagger.to_dict()

        object_ = self.object_.to_dict()

        verification: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.verification, Unset):
            verification = self.verification.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "node_id": node_id,
                "tag": tag,
                "sha": sha,
                "url": url,
                "message": message,
                "tagger": tagger,
                "object": object_,
            }
        )
        if verification is not UNSET:
            field_dict["verification"] = verification

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        node_id = d.pop("node_id")

        tag = d.pop("tag")

        sha = d.pop("sha")

        url = d.pop("url")

        message = d.pop("message")

        tagger = GitTagTagger.from_dict(d.pop("tagger"))

        object_ = GitTagObject.from_dict(d.pop("object"))

        _verification = d.pop("verification", UNSET)
        verification: Union[Unset, Verification]
        if isinstance(_verification, Unset):
            verification = UNSET
        else:
            verification = Verification.from_dict(_verification)

        git_tag = cls(
            node_id=node_id,
            tag=tag,
            sha=sha,
            url=url,
            message=message,
            tagger=tagger,
            object_=object_,
            verification=verification,
        )

        git_tag.additional_properties = d
        return git_tag

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
