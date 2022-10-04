from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImportProjectChoicesItem")


@attr.s(auto_attribs=True)
class ImportProjectChoicesItem:
    """
    Attributes:
        vcs (Union[Unset, str]):
        tfvc_project (Union[Unset, str]):
        human_name (Union[Unset, str]):
    """

    vcs: Union[Unset, str] = UNSET
    tfvc_project: Union[Unset, str] = UNSET
    human_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        vcs = self.vcs
        tfvc_project = self.tfvc_project
        human_name = self.human_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vcs is not UNSET:
            field_dict["vcs"] = vcs
        if tfvc_project is not UNSET:
            field_dict["tfvc_project"] = tfvc_project
        if human_name is not UNSET:
            field_dict["human_name"] = human_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        vcs = d.pop("vcs", UNSET)

        tfvc_project = d.pop("tfvc_project", UNSET)

        human_name = d.pop("human_name", UNSET)

        import_project_choices_item = cls(
            vcs=vcs,
            tfvc_project=tfvc_project,
            human_name=human_name,
        )

        import_project_choices_item.additional_properties = d
        return import_project_choices_item

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
