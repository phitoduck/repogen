from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UsersupdateAuthenticatedJsonBody")


@attr.s(auto_attribs=True)
class UsersupdateAuthenticatedJsonBody:
    """
    Attributes:
        name (Union[Unset, str]): The new name of the user. Example: Omar Jahandar.
        email (Union[Unset, str]): The publicly visible email address of the user. Example: omar@example.com.
        blog (Union[Unset, str]): The new blog URL of the user. Example: blog.example.com.
        twitter_username (Union[Unset, None, str]): The new Twitter username of the user. Example: therealomarj.
        company (Union[Unset, str]): The new company of the user. Example: Acme corporation.
        location (Union[Unset, str]): The new location of the user. Example: Berlin, Germany.
        hireable (Union[Unset, bool]): The new hiring availability of the user.
        bio (Union[Unset, str]): The new short biography of the user.
    """

    name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    blog: Union[Unset, str] = UNSET
    twitter_username: Union[Unset, None, str] = UNSET
    company: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    hireable: Union[Unset, bool] = UNSET
    bio: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        email = self.email
        blog = self.blog
        twitter_username = self.twitter_username
        company = self.company
        location = self.location
        hireable = self.hireable
        bio = self.bio

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email
        if blog is not UNSET:
            field_dict["blog"] = blog
        if twitter_username is not UNSET:
            field_dict["twitter_username"] = twitter_username
        if company is not UNSET:
            field_dict["company"] = company
        if location is not UNSET:
            field_dict["location"] = location
        if hireable is not UNSET:
            field_dict["hireable"] = hireable
        if bio is not UNSET:
            field_dict["bio"] = bio

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        email = d.pop("email", UNSET)

        blog = d.pop("blog", UNSET)

        twitter_username = d.pop("twitter_username", UNSET)

        company = d.pop("company", UNSET)

        location = d.pop("location", UNSET)

        hireable = d.pop("hireable", UNSET)

        bio = d.pop("bio", UNSET)

        usersupdate_authenticated_json_body = cls(
            name=name,
            email=email,
            blog=blog,
            twitter_username=twitter_username,
            company=company,
            location=location,
            hireable=hireable,
            bio=bio,
        )

        usersupdate_authenticated_json_body.additional_properties = d
        return usersupdate_authenticated_json_body

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
