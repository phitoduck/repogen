from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.server_statistics_item_ghe_stats_comments import ServerStatisticsItemGheStatsComments
from ..models.server_statistics_item_ghe_stats_gists import ServerStatisticsItemGheStatsGists
from ..models.server_statistics_item_ghe_stats_hooks import ServerStatisticsItemGheStatsHooks
from ..models.server_statistics_item_ghe_stats_issues import ServerStatisticsItemGheStatsIssues
from ..models.server_statistics_item_ghe_stats_milestones import ServerStatisticsItemGheStatsMilestones
from ..models.server_statistics_item_ghe_stats_orgs import ServerStatisticsItemGheStatsOrgs
from ..models.server_statistics_item_ghe_stats_pages import ServerStatisticsItemGheStatsPages
from ..models.server_statistics_item_ghe_stats_pulls import ServerStatisticsItemGheStatsPulls
from ..models.server_statistics_item_ghe_stats_repos import ServerStatisticsItemGheStatsRepos
from ..models.server_statistics_item_ghe_stats_users import ServerStatisticsItemGheStatsUsers
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerStatisticsItemGheStats")


@attr.s(auto_attribs=True)
class ServerStatisticsItemGheStats:
    """
    Attributes:
        comments (Union[Unset, ServerStatisticsItemGheStatsComments]):
        gists (Union[Unset, ServerStatisticsItemGheStatsGists]):
        hooks (Union[Unset, ServerStatisticsItemGheStatsHooks]):
        issues (Union[Unset, ServerStatisticsItemGheStatsIssues]):
        milestones (Union[Unset, ServerStatisticsItemGheStatsMilestones]):
        orgs (Union[Unset, ServerStatisticsItemGheStatsOrgs]):
        pages (Union[Unset, ServerStatisticsItemGheStatsPages]):
        pulls (Union[Unset, ServerStatisticsItemGheStatsPulls]):
        repos (Union[Unset, ServerStatisticsItemGheStatsRepos]):
        users (Union[Unset, ServerStatisticsItemGheStatsUsers]):
    """

    comments: Union[Unset, ServerStatisticsItemGheStatsComments] = UNSET
    gists: Union[Unset, ServerStatisticsItemGheStatsGists] = UNSET
    hooks: Union[Unset, ServerStatisticsItemGheStatsHooks] = UNSET
    issues: Union[Unset, ServerStatisticsItemGheStatsIssues] = UNSET
    milestones: Union[Unset, ServerStatisticsItemGheStatsMilestones] = UNSET
    orgs: Union[Unset, ServerStatisticsItemGheStatsOrgs] = UNSET
    pages: Union[Unset, ServerStatisticsItemGheStatsPages] = UNSET
    pulls: Union[Unset, ServerStatisticsItemGheStatsPulls] = UNSET
    repos: Union[Unset, ServerStatisticsItemGheStatsRepos] = UNSET
    users: Union[Unset, ServerStatisticsItemGheStatsUsers] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        comments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.comments, Unset):
            comments = self.comments.to_dict()

        gists: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.gists, Unset):
            gists = self.gists.to_dict()

        hooks: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.hooks, Unset):
            hooks = self.hooks.to_dict()

        issues: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.issues, Unset):
            issues = self.issues.to_dict()

        milestones: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.milestones, Unset):
            milestones = self.milestones.to_dict()

        orgs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.orgs, Unset):
            orgs = self.orgs.to_dict()

        pages: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pages, Unset):
            pages = self.pages.to_dict()

        pulls: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pulls, Unset):
            pulls = self.pulls.to_dict()

        repos: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.repos, Unset):
            repos = self.repos.to_dict()

        users: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.users, Unset):
            users = self.users.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comments is not UNSET:
            field_dict["comments"] = comments
        if gists is not UNSET:
            field_dict["gists"] = gists
        if hooks is not UNSET:
            field_dict["hooks"] = hooks
        if issues is not UNSET:
            field_dict["issues"] = issues
        if milestones is not UNSET:
            field_dict["milestones"] = milestones
        if orgs is not UNSET:
            field_dict["orgs"] = orgs
        if pages is not UNSET:
            field_dict["pages"] = pages
        if pulls is not UNSET:
            field_dict["pulls"] = pulls
        if repos is not UNSET:
            field_dict["repos"] = repos
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _comments = d.pop("comments", UNSET)
        comments: Union[Unset, ServerStatisticsItemGheStatsComments]
        if isinstance(_comments, Unset):
            comments = UNSET
        else:
            comments = ServerStatisticsItemGheStatsComments.from_dict(_comments)

        _gists = d.pop("gists", UNSET)
        gists: Union[Unset, ServerStatisticsItemGheStatsGists]
        if isinstance(_gists, Unset):
            gists = UNSET
        else:
            gists = ServerStatisticsItemGheStatsGists.from_dict(_gists)

        _hooks = d.pop("hooks", UNSET)
        hooks: Union[Unset, ServerStatisticsItemGheStatsHooks]
        if isinstance(_hooks, Unset):
            hooks = UNSET
        else:
            hooks = ServerStatisticsItemGheStatsHooks.from_dict(_hooks)

        _issues = d.pop("issues", UNSET)
        issues: Union[Unset, ServerStatisticsItemGheStatsIssues]
        if isinstance(_issues, Unset):
            issues = UNSET
        else:
            issues = ServerStatisticsItemGheStatsIssues.from_dict(_issues)

        _milestones = d.pop("milestones", UNSET)
        milestones: Union[Unset, ServerStatisticsItemGheStatsMilestones]
        if isinstance(_milestones, Unset):
            milestones = UNSET
        else:
            milestones = ServerStatisticsItemGheStatsMilestones.from_dict(_milestones)

        _orgs = d.pop("orgs", UNSET)
        orgs: Union[Unset, ServerStatisticsItemGheStatsOrgs]
        if isinstance(_orgs, Unset):
            orgs = UNSET
        else:
            orgs = ServerStatisticsItemGheStatsOrgs.from_dict(_orgs)

        _pages = d.pop("pages", UNSET)
        pages: Union[Unset, ServerStatisticsItemGheStatsPages]
        if isinstance(_pages, Unset):
            pages = UNSET
        else:
            pages = ServerStatisticsItemGheStatsPages.from_dict(_pages)

        _pulls = d.pop("pulls", UNSET)
        pulls: Union[Unset, ServerStatisticsItemGheStatsPulls]
        if isinstance(_pulls, Unset):
            pulls = UNSET
        else:
            pulls = ServerStatisticsItemGheStatsPulls.from_dict(_pulls)

        _repos = d.pop("repos", UNSET)
        repos: Union[Unset, ServerStatisticsItemGheStatsRepos]
        if isinstance(_repos, Unset):
            repos = UNSET
        else:
            repos = ServerStatisticsItemGheStatsRepos.from_dict(_repos)

        _users = d.pop("users", UNSET)
        users: Union[Unset, ServerStatisticsItemGheStatsUsers]
        if isinstance(_users, Unset):
            users = UNSET
        else:
            users = ServerStatisticsItemGheStatsUsers.from_dict(_users)

        server_statistics_item_ghe_stats = cls(
            comments=comments,
            gists=gists,
            hooks=hooks,
            issues=issues,
            milestones=milestones,
            orgs=orgs,
            pages=pages,
            pulls=pulls,
            repos=repos,
            users=users,
        )

        server_statistics_item_ghe_stats.additional_properties = d
        return server_statistics_item_ghe_stats

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
