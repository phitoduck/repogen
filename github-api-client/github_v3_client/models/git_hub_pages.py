import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.git_hub_pages_build_type import GitHubPagesBuildType
from ..models.git_hub_pages_protected_domain_state import GitHubPagesProtectedDomainState
from ..models.git_hub_pages_status import GitHubPagesStatus
from ..models.pages_https_certificate import PagesHttpsCertificate
from ..models.pages_source_hash import PagesSourceHash
from ..types import UNSET, Unset

T = TypeVar("T", bound="GitHubPages")


@attr.s(auto_attribs=True)
class GitHubPages:
    """The configuration for GitHub Pages for a repository.

    Attributes:
        url (str): The API address for accessing this Page resource. Example: https://api.github.com/repos/github/hello-
            world/pages.
        custom_404 (bool): Whether the Page has a custom 404 page.
        public (bool): Whether the GitHub Pages site is publicly visible. If set to `true`, the site is accessible to
            anyone on the internet. If set to `false`, the site will only be accessible to users who have at least `read`
            access to the repository that published the site. Example: True.
        status (Optional[GitHubPagesStatus]): The status of the most recent build of the Page. Example: built.
        cname (Optional[str]): The Pages site's custom domain Example: example.com.
        protected_domain_state (Union[Unset, None, GitHubPagesProtectedDomainState]): The state if the domain is
            verified Example: pending.
        pending_domain_unverified_at (Union[Unset, None, datetime.datetime]): The timestamp when a pending domain
            becomes unverified.
        html_url (Union[Unset, str]): The web address the Page can be accessed from. Example: https://example.com.
        build_type (Union[Unset, None, GitHubPagesBuildType]): The process in which the Page will be built. Example:
            legacy.
        source (Union[Unset, PagesSourceHash]):
        https_certificate (Union[Unset, PagesHttpsCertificate]):
        https_enforced (Union[Unset, bool]): Whether https is enabled on the domain Example: True.
    """

    url: str
    public: bool
    status: Optional[GitHubPagesStatus]
    cname: Optional[str]
    custom_404: bool = False
    protected_domain_state: Union[Unset, None, GitHubPagesProtectedDomainState] = UNSET
    pending_domain_unverified_at: Union[Unset, None, datetime.datetime] = UNSET
    html_url: Union[Unset, str] = UNSET
    build_type: Union[Unset, None, GitHubPagesBuildType] = UNSET
    source: Union[Unset, PagesSourceHash] = UNSET
    https_certificate: Union[Unset, PagesHttpsCertificate] = UNSET
    https_enforced: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        custom_404 = self.custom_404
        public = self.public
        status = self.status.value if self.status else None

        cname = self.cname
        protected_domain_state: Union[Unset, None, str] = UNSET
        if not isinstance(self.protected_domain_state, Unset):
            protected_domain_state = self.protected_domain_state.value if self.protected_domain_state else None

        pending_domain_unverified_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.pending_domain_unverified_at, Unset):
            pending_domain_unverified_at = (
                self.pending_domain_unverified_at.isoformat() if self.pending_domain_unverified_at else None
            )

        html_url = self.html_url
        build_type: Union[Unset, None, str] = UNSET
        if not isinstance(self.build_type, Unset):
            build_type = self.build_type.value if self.build_type else None

        source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        https_certificate: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.https_certificate, Unset):
            https_certificate = self.https_certificate.to_dict()

        https_enforced = self.https_enforced

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "custom_404": custom_404,
                "public": public,
                "status": status,
                "cname": cname,
            }
        )
        if protected_domain_state is not UNSET:
            field_dict["protected_domain_state"] = protected_domain_state
        if pending_domain_unverified_at is not UNSET:
            field_dict["pending_domain_unverified_at"] = pending_domain_unverified_at
        if html_url is not UNSET:
            field_dict["html_url"] = html_url
        if build_type is not UNSET:
            field_dict["build_type"] = build_type
        if source is not UNSET:
            field_dict["source"] = source
        if https_certificate is not UNSET:
            field_dict["https_certificate"] = https_certificate
        if https_enforced is not UNSET:
            field_dict["https_enforced"] = https_enforced

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        custom_404 = d.pop("custom_404")

        public = d.pop("public")

        _status = d.pop("status")
        status: Optional[GitHubPagesStatus]
        if _status is None:
            status = None
        else:
            status = GitHubPagesStatus(_status)

        cname = d.pop("cname")

        _protected_domain_state = d.pop("protected_domain_state", UNSET)
        protected_domain_state: Union[Unset, None, GitHubPagesProtectedDomainState]
        if _protected_domain_state is None:
            protected_domain_state = None
        elif isinstance(_protected_domain_state, Unset):
            protected_domain_state = UNSET
        else:
            protected_domain_state = GitHubPagesProtectedDomainState(_protected_domain_state)

        _pending_domain_unverified_at = d.pop("pending_domain_unverified_at", UNSET)
        pending_domain_unverified_at: Union[Unset, None, datetime.datetime]
        if _pending_domain_unverified_at is None:
            pending_domain_unverified_at = None
        elif isinstance(_pending_domain_unverified_at, Unset):
            pending_domain_unverified_at = UNSET
        else:
            pending_domain_unverified_at = isoparse(_pending_domain_unverified_at)

        html_url = d.pop("html_url", UNSET)

        _build_type = d.pop("build_type", UNSET)
        build_type: Union[Unset, None, GitHubPagesBuildType]
        if _build_type is None:
            build_type = None
        elif isinstance(_build_type, Unset):
            build_type = UNSET
        else:
            build_type = GitHubPagesBuildType(_build_type)

        _source = d.pop("source", UNSET)
        source: Union[Unset, PagesSourceHash]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = PagesSourceHash.from_dict(_source)

        _https_certificate = d.pop("https_certificate", UNSET)
        https_certificate: Union[Unset, PagesHttpsCertificate]
        if isinstance(_https_certificate, Unset):
            https_certificate = UNSET
        else:
            https_certificate = PagesHttpsCertificate.from_dict(_https_certificate)

        https_enforced = d.pop("https_enforced", UNSET)

        git_hub_pages = cls(
            url=url,
            custom_404=custom_404,
            public=public,
            status=status,
            cname=cname,
            protected_domain_state=protected_domain_state,
            pending_domain_unverified_at=pending_domain_unverified_at,
            html_url=html_url,
            build_type=build_type,
            source=source,
            https_certificate=https_certificate,
            https_enforced=https_enforced,
        )

        git_hub_pages.additional_properties = d
        return git_hub_pages

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
