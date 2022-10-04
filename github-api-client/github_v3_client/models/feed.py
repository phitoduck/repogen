from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.feed_links import FeedLinks
from ..types import UNSET, Unset

T = TypeVar("T", bound="Feed")


@attr.s(auto_attribs=True)
class Feed:
    """Feed

    Attributes:
        timeline_url (str):  Example: https://github.com/timeline.
        user_url (str):  Example: https://github.com/{user}.
        links (FeedLinks):
        current_user_public_url (Union[Unset, str]):  Example: https://github.com/octocat.
        current_user_url (Union[Unset, str]):  Example: https://github.com/octocat.private?token=abc123.
        current_user_actor_url (Union[Unset, str]):  Example: https://github.com/octocat.private.actor?token=abc123.
        current_user_organization_url (Union[Unset, str]):  Example: https://github.com/octocat-org.
        current_user_organization_urls (Union[Unset, List[str]]):  Example:
            ['https://github.com/organizations/github/octocat.private.atom?token=abc123'].
        security_advisories_url (Union[Unset, str]):  Example: https://github.com/security-advisories.
    """

    timeline_url: str
    user_url: str
    links: FeedLinks
    current_user_public_url: Union[Unset, str] = UNSET
    current_user_url: Union[Unset, str] = UNSET
    current_user_actor_url: Union[Unset, str] = UNSET
    current_user_organization_url: Union[Unset, str] = UNSET
    current_user_organization_urls: Union[Unset, List[str]] = UNSET
    security_advisories_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timeline_url = self.timeline_url
        user_url = self.user_url
        links = self.links.to_dict()

        current_user_public_url = self.current_user_public_url
        current_user_url = self.current_user_url
        current_user_actor_url = self.current_user_actor_url
        current_user_organization_url = self.current_user_organization_url
        current_user_organization_urls: Union[Unset, List[str]] = UNSET
        if not isinstance(self.current_user_organization_urls, Unset):
            current_user_organization_urls = self.current_user_organization_urls

        security_advisories_url = self.security_advisories_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timeline_url": timeline_url,
                "user_url": user_url,
                "_links": links,
            }
        )
        if current_user_public_url is not UNSET:
            field_dict["current_user_public_url"] = current_user_public_url
        if current_user_url is not UNSET:
            field_dict["current_user_url"] = current_user_url
        if current_user_actor_url is not UNSET:
            field_dict["current_user_actor_url"] = current_user_actor_url
        if current_user_organization_url is not UNSET:
            field_dict["current_user_organization_url"] = current_user_organization_url
        if current_user_organization_urls is not UNSET:
            field_dict["current_user_organization_urls"] = current_user_organization_urls
        if security_advisories_url is not UNSET:
            field_dict["security_advisories_url"] = security_advisories_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        timeline_url = d.pop("timeline_url")

        user_url = d.pop("user_url")

        links = FeedLinks.from_dict(d.pop("_links"))

        current_user_public_url = d.pop("current_user_public_url", UNSET)

        current_user_url = d.pop("current_user_url", UNSET)

        current_user_actor_url = d.pop("current_user_actor_url", UNSET)

        current_user_organization_url = d.pop("current_user_organization_url", UNSET)

        current_user_organization_urls = cast(List[str], d.pop("current_user_organization_urls", UNSET))

        security_advisories_url = d.pop("security_advisories_url", UNSET)

        feed = cls(
            timeline_url=timeline_url,
            user_url=user_url,
            links=links,
            current_user_public_url=current_user_public_url,
            current_user_url=current_user_url,
            current_user_actor_url=current_user_actor_url,
            current_user_organization_url=current_user_organization_url,
            current_user_organization_urls=current_user_organization_urls,
            security_advisories_url=security_advisories_url,
        )

        feed.additional_properties = d
        return feed

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
