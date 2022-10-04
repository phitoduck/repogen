from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GitcreateRefJsonBody")


@attr.s(auto_attribs=True)
class GitcreateRefJsonBody:
    """
    Attributes:
        ref (str): The name of the fully qualified reference (ie: `refs/heads/master`). If it doesn't start with 'refs'
            and have at least two slashes, it will be rejected.
        sha (str): The SHA1 value for this reference.
        key (Union[Unset, str]):  Example: "refs/heads/newbranch".
    """

    ref: str
    sha: str
    key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ref = self.ref
        sha = self.sha
        key = self.key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ref": ref,
                "sha": sha,
            }
        )
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ref = d.pop("ref")

        sha = d.pop("sha")

        key = d.pop("key", UNSET)

        gitcreate_ref_json_body = cls(
            ref=ref,
            sha=sha,
            key=key,
        )

        gitcreate_ref_json_body.additional_properties = d
        return gitcreate_ref_json_body

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
