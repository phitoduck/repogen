from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="ChecksrerequestRunResponse201")


@attr.s(auto_attribs=True)
class ChecksrerequestRunResponse201:
    """ """

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        src_dict.copy()
        checksrerequest_run_response_201 = cls()

        return checksrerequest_run_response_201
