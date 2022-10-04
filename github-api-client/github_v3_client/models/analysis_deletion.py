from typing import Any, Dict, List, Optional, Type, TypeVar

import attr

T = TypeVar("T", bound="AnalysisDeletion")


@attr.s(auto_attribs=True)
class AnalysisDeletion:
    """Successful deletion of a code scanning analysis

    Attributes:
        next_analysis_url (Optional[str]): Next deletable analysis in chain, without last analysis deletion confirmation
        confirm_delete_url (Optional[str]): Next deletable analysis in chain, with last analysis deletion confirmation
    """

    next_analysis_url: Optional[str]
    confirm_delete_url: Optional[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        next_analysis_url = self.next_analysis_url
        confirm_delete_url = self.confirm_delete_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "next_analysis_url": next_analysis_url,
                "confirm_delete_url": confirm_delete_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        next_analysis_url = d.pop("next_analysis_url")

        confirm_delete_url = d.pop("confirm_delete_url")

        analysis_deletion = cls(
            next_analysis_url=next_analysis_url,
            confirm_delete_url=confirm_delete_url,
        )

        analysis_deletion.additional_properties = d
        return analysis_deletion

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
