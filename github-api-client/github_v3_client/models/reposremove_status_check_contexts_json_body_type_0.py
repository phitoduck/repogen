from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="ReposremoveStatusCheckContextsJsonBodyType0")


@attr.s(auto_attribs=True)
class ReposremoveStatusCheckContextsJsonBodyType0:
    """
    Example:
        {'contexts': ['contexts']}

    Attributes:
        contexts (List[str]): The name of the status checks
    """

    contexts: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contexts = self.contexts

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contexts": contexts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        contexts = cast(List[str], d.pop("contexts"))

        reposremove_status_check_contexts_json_body_type_0 = cls(
            contexts=contexts,
        )

        reposremove_status_check_contexts_json_body_type_0.additional_properties = d
        return reposremove_status_check_contexts_json_body_type_0

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
