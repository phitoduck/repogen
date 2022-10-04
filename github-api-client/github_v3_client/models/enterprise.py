import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Enterprise")


@attr.s(auto_attribs=True)
class Enterprise:
    """An enterprise account

    Attributes:
        html_url (str):  Example: https://github.com/enterprises/octo-business.
        id (int): Unique identifier of the enterprise Example: 42.
        node_id (str):  Example: MDEwOlJlcG9zaXRvcnkxMjk2MjY5.
        name (str): The name of the enterprise. Example: Octo Business.
        slug (str): The slug url identifier for the enterprise. Example: octo-business.
        avatar_url (str):
        description (Union[Unset, None, str]): A short description of the enterprise.
        website_url (Union[Unset, None, str]): The enterprise's website URL.
        created_at (Optional[datetime.datetime]):  Example: 2019-01-26T19:01:12Z.
        updated_at (Optional[datetime.datetime]):  Example: 2019-01-26T19:14:43Z.
    """

    html_url: str
    id: int
    node_id: str
    name: str
    slug: str
    avatar_url: str
    created_at: Optional[datetime.datetime]
    updated_at: Optional[datetime.datetime]
    description: Union[Unset, None, str] = UNSET
    website_url: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        html_url = self.html_url
        id = self.id
        node_id = self.node_id
        name = self.name
        slug = self.slug
        avatar_url = self.avatar_url
        description = self.description
        website_url = self.website_url
        created_at = self.created_at.isoformat() if self.created_at else None

        updated_at = self.updated_at.isoformat() if self.updated_at else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "html_url": html_url,
                "id": id,
                "node_id": node_id,
                "name": name,
                "slug": slug,
                "avatar_url": avatar_url,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if website_url is not UNSET:
            field_dict["website_url"] = website_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        html_url = d.pop("html_url")

        id = d.pop("id")

        node_id = d.pop("node_id")

        name = d.pop("name")

        slug = d.pop("slug")

        avatar_url = d.pop("avatar_url")

        description = d.pop("description", UNSET)

        website_url = d.pop("website_url", UNSET)

        _created_at = d.pop("created_at")
        created_at: Optional[datetime.datetime]
        if _created_at is None:
            created_at = None
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at")
        updated_at: Optional[datetime.datetime]
        if _updated_at is None:
            updated_at = None
        else:
            updated_at = isoparse(_updated_at)

        enterprise = cls(
            html_url=html_url,
            id=id,
            node_id=node_id,
            name=name,
            slug=slug,
            avatar_url=avatar_url,
            description=description,
            website_url=website_url,
            created_at=created_at,
            updated_at=updated_at,
        )

        enterprise.additional_properties = d
        return enterprise

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
