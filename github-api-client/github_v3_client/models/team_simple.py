from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamSimple")


@attr.s(auto_attribs=True)
class TeamSimple:
    """Groups of organization members that gives permissions on specified repositories.

    Attributes:
        id (int): Unique identifier of the team Example: 1.
        node_id (str):  Example: MDQ6VGVhbTE=.
        url (str): URL for the team Example: https://api.github.com/organizations/1/team/1.
        members_url (str):  Example: https://api.github.com/organizations/1/team/1/members{/member}.
        name (str): Name of the team Example: Justice League.
        permission (str): Permission that the team will have for its repositories Example: admin.
        html_url (str):  Example: https://github.com/orgs/rails/teams/core.
        repositories_url (str):  Example: https://api.github.com/organizations/1/team/1/repos.
        slug (str):  Example: justice-league.
        description (Optional[str]): Description of the team Example: A great team..
        privacy (Union[Unset, str]): The level of privacy this team should have Example: closed.
        ldap_dn (Union[Unset, str]): Distinguished Name (DN) that team maps to within LDAP environment Example:
            uid=example,ou=users,dc=github,dc=com.
    """

    id: int
    node_id: str
    url: str
    members_url: str
    name: str
    permission: str
    html_url: str
    repositories_url: str
    slug: str
    description: Optional[str]
    privacy: Union[Unset, str] = UNSET
    ldap_dn: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        node_id = self.node_id
        url = self.url
        members_url = self.members_url
        name = self.name
        permission = self.permission
        html_url = self.html_url
        repositories_url = self.repositories_url
        slug = self.slug
        description = self.description
        privacy = self.privacy
        ldap_dn = self.ldap_dn

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "node_id": node_id,
                "url": url,
                "members_url": members_url,
                "name": name,
                "permission": permission,
                "html_url": html_url,
                "repositories_url": repositories_url,
                "slug": slug,
                "description": description,
            }
        )
        if privacy is not UNSET:
            field_dict["privacy"] = privacy
        if ldap_dn is not UNSET:
            field_dict["ldap_dn"] = ldap_dn

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        node_id = d.pop("node_id")

        url = d.pop("url")

        members_url = d.pop("members_url")

        name = d.pop("name")

        permission = d.pop("permission")

        html_url = d.pop("html_url")

        repositories_url = d.pop("repositories_url")

        slug = d.pop("slug")

        description = d.pop("description")

        privacy = d.pop("privacy", UNSET)

        ldap_dn = d.pop("ldap_dn", UNSET)

        team_simple = cls(
            id=id,
            node_id=node_id,
            url=url,
            members_url=members_url,
            name=name,
            permission=permission,
            html_url=html_url,
            repositories_url=repositories_url,
            slug=slug,
            description=description,
            privacy=privacy,
            ldap_dn=ldap_dn,
        )

        team_simple.additional_properties = d
        return team_simple

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
