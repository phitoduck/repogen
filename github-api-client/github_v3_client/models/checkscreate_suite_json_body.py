from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CheckscreateSuiteJsonBody")


@attr.s(auto_attribs=True)
class CheckscreateSuiteJsonBody:
    """
    Attributes:
        head_sha (str): The sha of the head commit.
    """

    head_sha: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        head_sha = self.head_sha

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "head_sha": head_sha,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        head_sha = d.pop("head_sha")

        checkscreate_suite_json_body = cls(
            head_sha=head_sha,
        )

        checkscreate_suite_json_body.additional_properties = d
        return checkscreate_suite_json_body

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
