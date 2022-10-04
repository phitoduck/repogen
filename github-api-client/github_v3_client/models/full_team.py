import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.full_team_privacy import FullTeamPrivacy
from ..models.team_organization import TeamOrganization
from ..models.team_simple import TeamSimple
from ..types import UNSET, Unset

T = TypeVar("T", bound="FullTeam")


@attr.s(auto_attribs=True)
class FullTeam:
    """Groups of organization members that gives permissions on specified repositories.

    Attributes:
        id (int): Unique identifier of the team Example: 42.
        node_id (str):  Example: MDQ6VGVhbTE=.
        url (str): URL for the team Example: https://api.github.com/organizations/1/team/1.
        html_url (str):  Example: https://github.com/orgs/rails/teams/core.
        name (str): Name of the team Example: Developers.
        slug (str):  Example: justice-league.
        permission (str): Permission that the team will have for its repositories Example: push.
        members_url (str):  Example: https://api.github.com/organizations/1/team/1/members{/member}.
        repositories_url (str):  Example: https://api.github.com/organizations/1/team/1/repos.
        members_count (int):  Example: 3.
        repos_count (int):  Example: 10.
        created_at (datetime.datetime):  Example: 2017-07-14T16:53:42Z.
        updated_at (datetime.datetime):  Example: 2017-08-17T12:37:15Z.
        organization (TeamOrganization): Team Organization
        description (Optional[str]):  Example: A great team..
        privacy (Union[Unset, FullTeamPrivacy]): The level of privacy this team should have Example: closed.
        parent (Union[Unset, None, TeamSimple]): Groups of organization members that gives permissions on specified
            repositories.
        ldap_dn (Union[Unset, str]): Distinguished Name (DN) that team maps to within LDAP environment Example:
            uid=example,ou=users,dc=github,dc=com.
    """

    id: int
    node_id: str
    url: str
    html_url: str
    name: str
    slug: str
    permission: str
    members_url: str
    repositories_url: str
    members_count: int
    repos_count: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    organization: TeamOrganization
    description: Optional[str]
    privacy: Union[Unset, FullTeamPrivacy] = UNSET
    parent: Union[Unset, None, TeamSimple] = UNSET
    ldap_dn: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        node_id = self.node_id
        url = self.url
        html_url = self.html_url
        name = self.name
        slug = self.slug
        permission = self.permission
        members_url = self.members_url
        repositories_url = self.repositories_url
        members_count = self.members_count
        repos_count = self.repos_count
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        organization = self.organization.to_dict()

        description = self.description
        privacy: Union[Unset, str] = UNSET
        if not isinstance(self.privacy, Unset):
            privacy = self.privacy.value

        parent: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict() if self.parent else None

        ldap_dn = self.ldap_dn

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "node_id": node_id,
                "url": url,
                "html_url": html_url,
                "name": name,
                "slug": slug,
                "permission": permission,
                "members_url": members_url,
                "repositories_url": repositories_url,
                "members_count": members_count,
                "repos_count": repos_count,
                "created_at": created_at,
                "updated_at": updated_at,
                "organization": organization,
                "description": description,
            }
        )
        if privacy is not UNSET:
            field_dict["privacy"] = privacy
        if parent is not UNSET:
            field_dict["parent"] = parent
        if ldap_dn is not UNSET:
            field_dict["ldap_dn"] = ldap_dn

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        node_id = d.pop("node_id")

        url = d.pop("url")

        html_url = d.pop("html_url")

        name = d.pop("name")

        slug = d.pop("slug")

        permission = d.pop("permission")

        members_url = d.pop("members_url")

        repositories_url = d.pop("repositories_url")

        members_count = d.pop("members_count")

        repos_count = d.pop("repos_count")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        organization = TeamOrganization.from_dict(d.pop("organization"))

        description = d.pop("description")

        _privacy = d.pop("privacy", UNSET)
        privacy: Union[Unset, FullTeamPrivacy]
        if isinstance(_privacy, Unset):
            privacy = UNSET
        else:
            privacy = FullTeamPrivacy(_privacy)

        _parent = d.pop("parent", UNSET)
        parent: Union[Unset, None, TeamSimple]
        if _parent is None:
            parent = None
        elif isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = TeamSimple.from_dict(_parent)

        ldap_dn = d.pop("ldap_dn", UNSET)

        full_team = cls(
            id=id,
            node_id=node_id,
            url=url,
            html_url=html_url,
            name=name,
            slug=slug,
            permission=permission,
            members_url=members_url,
            repositories_url=repositories_url,
            members_count=members_count,
            repos_count=repos_count,
            created_at=created_at,
            updated_at=updated_at,
            organization=organization,
            description=description,
            privacy=privacy,
            parent=parent,
            ldap_dn=ldap_dn,
        )

        full_team.additional_properties = d
        return full_team

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
