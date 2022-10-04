from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.pull_request_minimal_base import PullRequestMinimalBase
from ..models.pull_request_minimal_head import PullRequestMinimalHead

T = TypeVar("T", bound="PullRequestMinimal")


@attr.s(auto_attribs=True)
class PullRequestMinimal:
    """
    Attributes:
        id (int):
        number (int):
        url (str):
        head (PullRequestMinimalHead):
        base (PullRequestMinimalBase):
    """

    id: int
    number: int
    url: str
    head: PullRequestMinimalHead
    base: PullRequestMinimalBase
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        number = self.number
        url = self.url
        head = self.head.to_dict()

        base = self.base.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "number": number,
                "url": url,
                "head": head,
                "base": base,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        number = d.pop("number")

        url = d.pop("url")

        head = PullRequestMinimalHead.from_dict(d.pop("head"))

        base = PullRequestMinimalBase.from_dict(d.pop("base"))

        pull_request_minimal = cls(
            id=id,
            number=number,
            url=url,
            head=head,
            base=base,
        )

        pull_request_minimal.additional_properties = d
        return pull_request_minimal

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
