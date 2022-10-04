import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.git_hub_app_permissions import GitHubAppPermissions
from ..models.simple_user import SimpleUser
from ..types import UNSET, Unset

T = TypeVar("T", bound="GitHubApp")


@attr.s(auto_attribs=True)
class GitHubApp:
    """GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and
    granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are
    first class actors within GitHub.

        Attributes:
            id (int): Unique identifier of the GitHub app Example: 37.
            node_id (str):  Example: MDExOkludGVncmF0aW9uMQ==.
            name (str): The name of the GitHub app Example: Probot Owners.
            external_url (str):  Example: https://example.com.
            html_url (str):  Example: https://github.com/apps/super-ci.
            created_at (datetime.datetime):  Example: 2017-07-08T16:18:44-04:00.
            updated_at (datetime.datetime):  Example: 2017-07-08T16:18:44-04:00.
            permissions (GitHubAppPermissions): The set of permissions for the GitHub app Example: {'issues': 'read',
                'deployments': 'write'}.
            events (List[str]): The list of events for the GitHub app Example: ['label', 'deployment'].
            slug (Union[Unset, str]): The slug name of the GitHub app Example: probot-owners.
            owner (Optional[SimpleUser]): Simple User
            description (Optional[str]):  Example: The description of the app..
            installations_count (Union[Unset, int]): The number of installations associated with the GitHub app Example: 5.
            client_id (Union[Unset, str]):  Example: "Iv1.25b5d1e65ffc4022".
            client_secret (Union[Unset, str]):  Example: "1d4b2097ac622ba702d19de498f005747a8b21d3".
            webhook_secret (Union[Unset, None, str]):  Example: "6fba8f2fc8a7e8f2cca5577eddd82ca7586b3b6b".
            pem (Union[Unset, str]):  Example: "-----BEGIN RSA PRIVATE KEY-----
                \nMIIEogIBAAKCAQEArYxrNYD/iT5CZVpRJu4rBKmmze3PVmT/gCo2ATUvDvZTPTey\nxcGJ3vvrJXazKk06pN05TN29o98jrYz4cengG3YGsXPN
                EpKsIrEl8NhbnxapEnM9\nJCMRe0P5JcPsfZlX6hmiT7136GRWiGOUba2X9+HKh8QJVLG5rM007TBER9/z9mWm\nrJuNh+m5l320oBQY/Qq3A7wz
                dEfZw8qm/mIN0FCeoXH1L6B8xXWaAYBwhTEh6SSn\nZHlO1Xu1JWDmAvBCi0RO5aRSKM8q9QEkvvHP4yweAtK3N8+aAbZ7ovaDhyGz8r6r\nzhU1
                b8Uo0Z2ysf503WqzQgIajr7Fry7/kUwpgQIDAQABAoIBADwJp80Ko1xHPZDy\nfcCKBDfIuPvkmSW6KumbsLMaQv1aGdHDwwTGv3t0ixSay8CGlx
                MRtRDyZPib6SvQ\n6OH/lpfpbMdW2ErkksgtoIKBVrDilfrcAvrNZu7NxRNbhCSvN8q0s4ICecjbbVQh\nnueSdlA6vGXbW58BHMq68uRbHkP+k+
                mM9U0mDJ1HMch67wlg5GbayVRt63H7R2+r\nVxcna7B80J/lCEjIYZznawgiTvp3MSanTglqAYi+m1EcSsP14bJIB9vgaxS79kTu\noiSo93leJb
                BvuGo8QEiUqTwMw4tDksmkLsoqNKQ1q9P7LZ9DGcujtPy4EZsamSJT\ny8OJt0ECgYEA2lxOxJsQk2kI325JgKFjo92mQeUObIvPfSNWUIZQDTjn
                iOI6Gv63\nGLWVFrZcvQBWjMEQraJA9xjPbblV8PtfO87MiJGLWCHFxmPz2dzoedN+2Coxom8m\nV95CLz8QUShuao6u/RYcvUaZEoYs5bHcTmy5
                sBK80JyEmafJPtCQVxMCgYEAy3ar\nZr3yv4xRPEPMat4rseswmuMooSaK3SKub19WFI5IAtB/e7qR1Rj9JhOGcZz+OQrl\nT78O2OFYlgOIkJPv
                RMrPpK5V9lslc7tz1FSh3BZMRGq5jSyD7ETSOQ0c8T2O/s7v\nbeEPbVbDe4mwvM24XByH0GnWveVxaDl51ABD65sCgYB3ZAspUkOA5egVCh8kNp
                nd\nSd6SnuQBE3ySRlT2WEnCwP9Ph6oPgn+oAfiPX4xbRqkL8q/k0BdHQ4h+zNwhk7+h\nWtPYRAP1Xxnc/F+jGjb+DVaIaKGU18MWPg7f+FI6na
                mpl3Q0KvfxwX0GdNhtio8T\nTj1E+SnFwh56SRQuxSh2gwKBgHKjlIO5NtNSflsUYFM+hyQiPiqnHzddfhSG+/3o\nm5nNaSmczJesUYreH5San7
                /YEy2UxAugvP7aSY2MxB+iGsiJ9WD2kZzTUlDZJ7RV\nUzWsoqBR+eZfVJ2FUWWvy8TpSG6trh4dFxImNtKejCR1TREpSiTV3Zb1dmahK9GV\nrK
                9NAoGAbBxRLoC01xfxCTgt5BDiBcFVh4fp5yYKwavJPLzHSpuDOrrI9jDn1oKN\nonq5sDU1i391zfQvdrbX4Ova48BN+B7p63FocP/MK5tyyBoT
                8zQEk2+vWDOw7H/Z\nu5dTCPxTIsoIwUw1I+7yIxqJzLPFgR2gVBwY1ra/8iAqCj+zeBw=\n-----END RSA PRIVATE KEY-----\n".
    """

    id: int
    node_id: str
    name: str
    external_url: str
    html_url: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    permissions: GitHubAppPermissions
    events: List[str]
    owner: Optional[SimpleUser]
    description: Optional[str]
    slug: Union[Unset, str] = UNSET
    installations_count: Union[Unset, int] = UNSET
    client_id: Union[Unset, str] = UNSET
    client_secret: Union[Unset, str] = UNSET
    webhook_secret: Union[Unset, None, str] = UNSET
    pem: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        node_id = self.node_id
        name = self.name
        external_url = self.external_url
        html_url = self.html_url
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        permissions = self.permissions.to_dict()

        events = self.events

        slug = self.slug
        owner = self.owner.to_dict() if self.owner else None

        description = self.description
        installations_count = self.installations_count
        client_id = self.client_id
        client_secret = self.client_secret
        webhook_secret = self.webhook_secret
        pem = self.pem

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "node_id": node_id,
                "name": name,
                "external_url": external_url,
                "html_url": html_url,
                "created_at": created_at,
                "updated_at": updated_at,
                "permissions": permissions,
                "events": events,
                "owner": owner,
                "description": description,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if installations_count is not UNSET:
            field_dict["installations_count"] = installations_count
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if client_secret is not UNSET:
            field_dict["client_secret"] = client_secret
        if webhook_secret is not UNSET:
            field_dict["webhook_secret"] = webhook_secret
        if pem is not UNSET:
            field_dict["pem"] = pem

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        node_id = d.pop("node_id")

        name = d.pop("name")

        external_url = d.pop("external_url")

        html_url = d.pop("html_url")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        permissions = GitHubAppPermissions.from_dict(d.pop("permissions"))

        events = cast(List[str], d.pop("events"))

        slug = d.pop("slug", UNSET)

        _owner = d.pop("owner")
        owner: Optional[SimpleUser]
        if _owner is None:
            owner = None
        else:
            owner = SimpleUser.from_dict(_owner)

        description = d.pop("description")

        installations_count = d.pop("installations_count", UNSET)

        client_id = d.pop("client_id", UNSET)

        client_secret = d.pop("client_secret", UNSET)

        webhook_secret = d.pop("webhook_secret", UNSET)

        pem = d.pop("pem", UNSET)

        git_hub_app = cls(
            id=id,
            node_id=node_id,
            name=name,
            external_url=external_url,
            html_url=html_url,
            created_at=created_at,
            updated_at=updated_at,
            permissions=permissions,
            events=events,
            slug=slug,
            owner=owner,
            description=description,
            installations_count=installations_count,
            client_id=client_id,
            client_secret=client_secret,
            webhook_secret=webhook_secret,
            pem=pem,
        )

        git_hub_app.additional_properties = d
        return git_hub_app

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
