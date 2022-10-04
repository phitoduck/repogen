from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.link_with_type import LinkWithType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FeedLinks")


@attr.s(auto_attribs=True)
class FeedLinks:
    """
    Attributes:
        timeline (LinkWithType): Hypermedia Link with Type
        user (LinkWithType): Hypermedia Link with Type
        security_advisories (Union[Unset, LinkWithType]): Hypermedia Link with Type
        current_user (Union[Unset, LinkWithType]): Hypermedia Link with Type
        current_user_public (Union[Unset, LinkWithType]): Hypermedia Link with Type
        current_user_actor (Union[Unset, LinkWithType]): Hypermedia Link with Type
        current_user_organization (Union[Unset, LinkWithType]): Hypermedia Link with Type
        current_user_organizations (Union[Unset, List[LinkWithType]]):
    """

    timeline: LinkWithType
    user: LinkWithType
    security_advisories: Union[Unset, LinkWithType] = UNSET
    current_user: Union[Unset, LinkWithType] = UNSET
    current_user_public: Union[Unset, LinkWithType] = UNSET
    current_user_actor: Union[Unset, LinkWithType] = UNSET
    current_user_organization: Union[Unset, LinkWithType] = UNSET
    current_user_organizations: Union[Unset, List[LinkWithType]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timeline = self.timeline.to_dict()

        user = self.user.to_dict()

        security_advisories: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.security_advisories, Unset):
            security_advisories = self.security_advisories.to_dict()

        current_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.current_user, Unset):
            current_user = self.current_user.to_dict()

        current_user_public: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.current_user_public, Unset):
            current_user_public = self.current_user_public.to_dict()

        current_user_actor: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.current_user_actor, Unset):
            current_user_actor = self.current_user_actor.to_dict()

        current_user_organization: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.current_user_organization, Unset):
            current_user_organization = self.current_user_organization.to_dict()

        current_user_organizations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.current_user_organizations, Unset):
            current_user_organizations = []
            for current_user_organizations_item_data in self.current_user_organizations:
                current_user_organizations_item = current_user_organizations_item_data.to_dict()

                current_user_organizations.append(current_user_organizations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timeline": timeline,
                "user": user,
            }
        )
        if security_advisories is not UNSET:
            field_dict["security_advisories"] = security_advisories
        if current_user is not UNSET:
            field_dict["current_user"] = current_user
        if current_user_public is not UNSET:
            field_dict["current_user_public"] = current_user_public
        if current_user_actor is not UNSET:
            field_dict["current_user_actor"] = current_user_actor
        if current_user_organization is not UNSET:
            field_dict["current_user_organization"] = current_user_organization
        if current_user_organizations is not UNSET:
            field_dict["current_user_organizations"] = current_user_organizations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        timeline = LinkWithType.from_dict(d.pop("timeline"))

        user = LinkWithType.from_dict(d.pop("user"))

        _security_advisories = d.pop("security_advisories", UNSET)
        security_advisories: Union[Unset, LinkWithType]
        if isinstance(_security_advisories, Unset):
            security_advisories = UNSET
        else:
            security_advisories = LinkWithType.from_dict(_security_advisories)

        _current_user = d.pop("current_user", UNSET)
        current_user: Union[Unset, LinkWithType]
        if isinstance(_current_user, Unset):
            current_user = UNSET
        else:
            current_user = LinkWithType.from_dict(_current_user)

        _current_user_public = d.pop("current_user_public", UNSET)
        current_user_public: Union[Unset, LinkWithType]
        if isinstance(_current_user_public, Unset):
            current_user_public = UNSET
        else:
            current_user_public = LinkWithType.from_dict(_current_user_public)

        _current_user_actor = d.pop("current_user_actor", UNSET)
        current_user_actor: Union[Unset, LinkWithType]
        if isinstance(_current_user_actor, Unset):
            current_user_actor = UNSET
        else:
            current_user_actor = LinkWithType.from_dict(_current_user_actor)

        _current_user_organization = d.pop("current_user_organization", UNSET)
        current_user_organization: Union[Unset, LinkWithType]
        if isinstance(_current_user_organization, Unset):
            current_user_organization = UNSET
        else:
            current_user_organization = LinkWithType.from_dict(_current_user_organization)

        current_user_organizations = []
        _current_user_organizations = d.pop("current_user_organizations", UNSET)
        for current_user_organizations_item_data in _current_user_organizations or []:
            current_user_organizations_item = LinkWithType.from_dict(current_user_organizations_item_data)

            current_user_organizations.append(current_user_organizations_item)

        feed_links = cls(
            timeline=timeline,
            user=user,
            security_advisories=security_advisories,
            current_user=current_user,
            current_user_public=current_user_public,
            current_user_actor=current_user_actor,
            current_user_organization=current_user_organization,
            current_user_organizations=current_user_organizations,
        )

        feed_links.additional_properties = d
        return feed_links

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
