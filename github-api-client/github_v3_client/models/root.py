from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Root")


@attr.s(auto_attribs=True)
class Root:
    """
    Attributes:
        current_user_url (str):
        current_user_authorizations_html_url (str):
        authorizations_url (str):
        code_search_url (str):
        commit_search_url (str):
        emails_url (str):
        emojis_url (str):
        events_url (str):
        feeds_url (str):
        followers_url (str):
        following_url (str):
        gists_url (str):
        hub_url (str):
        issue_search_url (str):
        issues_url (str):
        keys_url (str):
        label_search_url (str):
        notifications_url (str):
        organization_url (str):
        organization_repositories_url (str):
        organization_teams_url (str):
        public_gists_url (str):
        rate_limit_url (str):
        repository_url (str):
        repository_search_url (str):
        current_user_repositories_url (str):
        starred_url (str):
        starred_gists_url (str):
        user_url (str):
        user_organizations_url (str):
        user_repositories_url (str):
        user_search_url (str):
        topic_search_url (Union[Unset, str]):
    """

    current_user_url: str
    current_user_authorizations_html_url: str
    authorizations_url: str
    code_search_url: str
    commit_search_url: str
    emails_url: str
    emojis_url: str
    events_url: str
    feeds_url: str
    followers_url: str
    following_url: str
    gists_url: str
    hub_url: str
    issue_search_url: str
    issues_url: str
    keys_url: str
    label_search_url: str
    notifications_url: str
    organization_url: str
    organization_repositories_url: str
    organization_teams_url: str
    public_gists_url: str
    rate_limit_url: str
    repository_url: str
    repository_search_url: str
    current_user_repositories_url: str
    starred_url: str
    starred_gists_url: str
    user_url: str
    user_organizations_url: str
    user_repositories_url: str
    user_search_url: str
    topic_search_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        current_user_url = self.current_user_url
        current_user_authorizations_html_url = self.current_user_authorizations_html_url
        authorizations_url = self.authorizations_url
        code_search_url = self.code_search_url
        commit_search_url = self.commit_search_url
        emails_url = self.emails_url
        emojis_url = self.emojis_url
        events_url = self.events_url
        feeds_url = self.feeds_url
        followers_url = self.followers_url
        following_url = self.following_url
        gists_url = self.gists_url
        hub_url = self.hub_url
        issue_search_url = self.issue_search_url
        issues_url = self.issues_url
        keys_url = self.keys_url
        label_search_url = self.label_search_url
        notifications_url = self.notifications_url
        organization_url = self.organization_url
        organization_repositories_url = self.organization_repositories_url
        organization_teams_url = self.organization_teams_url
        public_gists_url = self.public_gists_url
        rate_limit_url = self.rate_limit_url
        repository_url = self.repository_url
        repository_search_url = self.repository_search_url
        current_user_repositories_url = self.current_user_repositories_url
        starred_url = self.starred_url
        starred_gists_url = self.starred_gists_url
        user_url = self.user_url
        user_organizations_url = self.user_organizations_url
        user_repositories_url = self.user_repositories_url
        user_search_url = self.user_search_url
        topic_search_url = self.topic_search_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "current_user_url": current_user_url,
                "current_user_authorizations_html_url": current_user_authorizations_html_url,
                "authorizations_url": authorizations_url,
                "code_search_url": code_search_url,
                "commit_search_url": commit_search_url,
                "emails_url": emails_url,
                "emojis_url": emojis_url,
                "events_url": events_url,
                "feeds_url": feeds_url,
                "followers_url": followers_url,
                "following_url": following_url,
                "gists_url": gists_url,
                "hub_url": hub_url,
                "issue_search_url": issue_search_url,
                "issues_url": issues_url,
                "keys_url": keys_url,
                "label_search_url": label_search_url,
                "notifications_url": notifications_url,
                "organization_url": organization_url,
                "organization_repositories_url": organization_repositories_url,
                "organization_teams_url": organization_teams_url,
                "public_gists_url": public_gists_url,
                "rate_limit_url": rate_limit_url,
                "repository_url": repository_url,
                "repository_search_url": repository_search_url,
                "current_user_repositories_url": current_user_repositories_url,
                "starred_url": starred_url,
                "starred_gists_url": starred_gists_url,
                "user_url": user_url,
                "user_organizations_url": user_organizations_url,
                "user_repositories_url": user_repositories_url,
                "user_search_url": user_search_url,
            }
        )
        if topic_search_url is not UNSET:
            field_dict["topic_search_url"] = topic_search_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        current_user_url = d.pop("current_user_url")

        current_user_authorizations_html_url = d.pop("current_user_authorizations_html_url")

        authorizations_url = d.pop("authorizations_url")

        code_search_url = d.pop("code_search_url")

        commit_search_url = d.pop("commit_search_url")

        emails_url = d.pop("emails_url")

        emojis_url = d.pop("emojis_url")

        events_url = d.pop("events_url")

        feeds_url = d.pop("feeds_url")

        followers_url = d.pop("followers_url")

        following_url = d.pop("following_url")

        gists_url = d.pop("gists_url")

        hub_url = d.pop("hub_url")

        issue_search_url = d.pop("issue_search_url")

        issues_url = d.pop("issues_url")

        keys_url = d.pop("keys_url")

        label_search_url = d.pop("label_search_url")

        notifications_url = d.pop("notifications_url")

        organization_url = d.pop("organization_url")

        organization_repositories_url = d.pop("organization_repositories_url")

        organization_teams_url = d.pop("organization_teams_url")

        public_gists_url = d.pop("public_gists_url")

        rate_limit_url = d.pop("rate_limit_url")

        repository_url = d.pop("repository_url")

        repository_search_url = d.pop("repository_search_url")

        current_user_repositories_url = d.pop("current_user_repositories_url")

        starred_url = d.pop("starred_url")

        starred_gists_url = d.pop("starred_gists_url")

        user_url = d.pop("user_url")

        user_organizations_url = d.pop("user_organizations_url")

        user_repositories_url = d.pop("user_repositories_url")

        user_search_url = d.pop("user_search_url")

        topic_search_url = d.pop("topic_search_url", UNSET)

        root = cls(
            current_user_url=current_user_url,
            current_user_authorizations_html_url=current_user_authorizations_html_url,
            authorizations_url=authorizations_url,
            code_search_url=code_search_url,
            commit_search_url=commit_search_url,
            emails_url=emails_url,
            emojis_url=emojis_url,
            events_url=events_url,
            feeds_url=feeds_url,
            followers_url=followers_url,
            following_url=following_url,
            gists_url=gists_url,
            hub_url=hub_url,
            issue_search_url=issue_search_url,
            issues_url=issues_url,
            keys_url=keys_url,
            label_search_url=label_search_url,
            notifications_url=notifications_url,
            organization_url=organization_url,
            organization_repositories_url=organization_repositories_url,
            organization_teams_url=organization_teams_url,
            public_gists_url=public_gists_url,
            rate_limit_url=rate_limit_url,
            repository_url=repository_url,
            repository_search_url=repository_search_url,
            current_user_repositories_url=current_user_repositories_url,
            starred_url=starred_url,
            starred_gists_url=starred_gists_url,
            user_url=user_url,
            user_organizations_url=user_organizations_url,
            user_repositories_url=user_repositories_url,
            user_search_url=user_search_url,
            topic_search_url=topic_search_url,
        )

        root.additional_properties = d
        return root

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
