from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GitupdateRefJsonBody")


@attr.s(auto_attribs=True)
class GitupdateRefJsonBody:
    """
    Attributes:
        sha (str): The SHA1 value to set this reference to
        force (Union[Unset, bool]): Indicates whether to force the update or to make sure the update is a fast-forward
            update. Leaving this out or setting it to `false` will make sure you're not overwriting work.
    """

    sha: str
    force: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sha = self.sha
        force = self.force

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sha": sha,
            }
        )
        if force is not UNSET:
            field_dict["force"] = force

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sha = d.pop("sha")

        force = d.pop("force", UNSET)

        gitupdate_ref_json_body = cls(
            sha=sha,
            force=force,
        )

        gitupdate_ref_json_body.additional_properties = d
        return gitupdate_ref_json_body

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
