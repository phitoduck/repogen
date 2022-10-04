from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReposupdateReleaseAssetJsonBody")


@attr.s(auto_attribs=True)
class ReposupdateReleaseAssetJsonBody:
    """
    Attributes:
        name (Union[Unset, str]): The file name of the asset.
        label (Union[Unset, str]): An alternate short description of the asset. Used in place of the filename.
        state (Union[Unset, str]):  Example: "uploaded".
    """

    name: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        label = self.label
        state = self.state

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if label is not UNSET:
            field_dict["label"] = label
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        label = d.pop("label", UNSET)

        state = d.pop("state", UNSET)

        reposupdate_release_asset_json_body = cls(
            name=name,
            label=label,
            state=state,
        )

        reposupdate_release_asset_json_body.additional_properties = d
        return reposupdate_release_asset_json_body

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
