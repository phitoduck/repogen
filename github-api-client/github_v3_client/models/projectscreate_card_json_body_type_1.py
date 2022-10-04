from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ProjectscreateCardJsonBodyType1")


@attr.s(auto_attribs=True)
class ProjectscreateCardJsonBodyType1:
    """
    Attributes:
        content_id (int): The unique identifier of the content associated with the card Example: 42.
        content_type (str): The piece of content associated with the card Example: PullRequest.
    """

    content_id: int
    content_type: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content_id = self.content_id
        content_type = self.content_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content_id": content_id,
                "content_type": content_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        content_id = d.pop("content_id")

        content_type = d.pop("content_type")

        projectscreate_card_json_body_type_1 = cls(
            content_id=content_id,
            content_type=content_type,
        )

        projectscreate_card_json_body_type_1.additional_properties = d
        return projectscreate_card_json_body_type_1

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
