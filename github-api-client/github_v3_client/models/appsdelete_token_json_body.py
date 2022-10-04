from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="AppsdeleteTokenJsonBody")


@attr.s(auto_attribs=True)
class AppsdeleteTokenJsonBody:
    """
    Attributes:
        access_token (str): The OAuth access token used to authenticate to the GitHub API.
    """

    access_token: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access_token = self.access_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access_token": access_token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        access_token = d.pop("access_token")

        appsdelete_token_json_body = cls(
            access_token=access_token,
        )

        appsdelete_token_json_body.additional_properties = d
        return appsdelete_token_json_body

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
