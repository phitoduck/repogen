from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PullRequestMinimalHeadRepo")


@attr.s(auto_attribs=True)
class PullRequestMinimalHeadRepo:
    """
    Attributes:
        id (int):
        url (str):
        name (str):
    """

    id: int
    url: str
    name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        name = d.pop("name")

        pull_request_minimal_head_repo = cls(
            id=id,
            url=url,
            name=name,
        )

        pull_request_minimal_head_repo.additional_properties = d
        return pull_request_minimal_head_repo

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
