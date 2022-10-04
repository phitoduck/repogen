from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="ProjectsmoveCardResponse201")


@attr.s(auto_attribs=True)
class ProjectsmoveCardResponse201:
    """ """

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        src_dict.copy()
        projectsmove_card_response_201 = cls()

        return projectsmove_card_response_201
