from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CodespacescreateForAuthenticatedUserJsonBodyType1PullRequest")


@attr.s(auto_attribs=True)
class CodespacescreateForAuthenticatedUserJsonBodyType1PullRequest:
    """Pull request number for this codespace

    Attributes:
        pull_request_number (int): Pull request number
        repository_id (int): Repository id for this codespace
    """

    pull_request_number: int
    repository_id: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pull_request_number = self.pull_request_number
        repository_id = self.repository_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pull_request_number": pull_request_number,
                "repository_id": repository_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        pull_request_number = d.pop("pull_request_number")

        repository_id = d.pop("repository_id")

        codespacescreate_for_authenticated_user_json_body_type_1_pull_request = cls(
            pull_request_number=pull_request_number,
            repository_id=repository_id,
        )

        codespacescreate_for_authenticated_user_json_body_type_1_pull_request.additional_properties = d
        return codespacescreate_for_authenticated_user_json_body_type_1_pull_request

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
