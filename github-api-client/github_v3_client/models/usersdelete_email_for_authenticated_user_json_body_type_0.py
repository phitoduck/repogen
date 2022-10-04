from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="UsersdeleteEmailForAuthenticatedUserJsonBodyType0")


@attr.s(auto_attribs=True)
class UsersdeleteEmailForAuthenticatedUserJsonBodyType0:
    """Deletes one or more email addresses from your GitHub account. Must contain at least one email address. **Note:**
    Alternatively, you can pass a single email address or an `array` of emails addresses directly, but we recommend that
    you pass an object using the `emails` key.

        Example:
            {'emails': ['octocat@github.com', 'mona@github.com']}

        Attributes:
            emails (List[str]): Email addresses associated with the GitHub user account.
    """

    emails: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        emails = self.emails

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "emails": emails,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        emails = cast(List[str], d.pop("emails"))

        usersdelete_email_for_authenticated_user_json_body_type_0 = cls(
            emails=emails,
        )

        usersdelete_email_for_authenticated_user_json_body_type_0.additional_properties = d
        return usersdelete_email_for_authenticated_user_json_body_type_0

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
