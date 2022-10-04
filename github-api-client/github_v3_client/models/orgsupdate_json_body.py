from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.orgsupdate_json_body_default_repository_permission import OrgsupdateJsonBodyDefaultRepositoryPermission
from ..models.orgsupdate_json_body_members_allowed_repository_creation_type import (
    OrgsupdateJsonBodyMembersAllowedRepositoryCreationType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrgsupdateJsonBody")


@attr.s(auto_attribs=True)
class OrgsupdateJsonBody:
    """
    Attributes:
        billing_email (Union[Unset, str]): Billing email address. This address is not publicized.
        company (Union[Unset, str]): The company name.
        email (Union[Unset, str]): The publicly visible email address.
        twitter_username (Union[Unset, str]): The Twitter username of the company.
        location (Union[Unset, str]): The location.
        name (Union[Unset, str]): The shorthand name of the company.
        description (Union[Unset, str]): The description of the company.
        has_organization_projects (Union[Unset, bool]): Whether an organization can use organization projects.
        has_repository_projects (Union[Unset, bool]): Whether repositories that belong to the organization can use
            repository projects.
        default_repository_permission (Union[Unset, OrgsupdateJsonBodyDefaultRepositoryPermission]): Default permission
            level members have for organization repositories. Default: OrgsupdateJsonBodyDefaultRepositoryPermission.READ.
        members_can_create_repositories (Union[Unset, bool]): Whether of non-admin organization members can create
            repositories. **Note:** A parameter can override this parameter. See `members_allowed_repository_creation_type`
            in this table for details. Default: True.
        members_can_create_internal_repositories (Union[Unset, bool]): Whether organization members can create internal
            repositories, which are visible to all enterprise members. You can only allow members to create internal
            repositories if your organization is associated with an enterprise account using GitHub Enterprise Cloud or
            GitHub Enterprise Server 2.20+. For more information, see "[Restricting repository creation in your
            organization](https://docs.github.com/github/setting-up-and-managing-organizations-and-teams/restricting-
            repository-creation-in-your-organization)" in the GitHub Help documentation.
        members_can_create_private_repositories (Union[Unset, bool]): Whether organization members can create private
            repositories, which are visible to organization members with permission. For more information, see "[Restricting
            repository creation in your organization](https://docs.github.com/github/setting-up-and-managing-organizations-
            and-teams/restricting-repository-creation-in-your-organization)" in the GitHub Help documentation.
        members_can_create_public_repositories (Union[Unset, bool]): Whether organization members can create public
            repositories, which are visible to anyone. For more information, see "[Restricting repository creation in your
            organization](https://docs.github.com/github/setting-up-and-managing-organizations-and-teams/restricting-
            repository-creation-in-your-organization)" in the GitHub Help documentation.
        members_allowed_repository_creation_type (Union[Unset, OrgsupdateJsonBodyMembersAllowedRepositoryCreationType]):
            Specifies which types of repositories non-admin organization members can create. `private` is only available to
            repositories that are part of an organization on GitHub Enterprise Cloud.
            **Note:** This parameter is deprecated and will be removed in the future. Its return value ignores internal
            repositories. Using this parameter overrides values set in `members_can_create_repositories`. See the parameter
            deprecation notice in the operation description for details.
        members_can_create_pages (Union[Unset, bool]): Whether organization members can create GitHub Pages sites.
            Existing published sites will not be impacted. Default: True.
        members_can_create_public_pages (Union[Unset, bool]): Whether organization members can create public GitHub
            Pages sites. Existing published sites will not be impacted. Default: True.
        members_can_create_private_pages (Union[Unset, bool]): Whether organization members can create private GitHub
            Pages sites. Existing published sites will not be impacted. Default: True.
        members_can_fork_private_repositories (Union[Unset, bool]): Whether organization members can fork private
            organization repositories.
        web_commit_signoff_required (Union[Unset, bool]): Whether contributors to organization repositories are required
            to sign off on commits they make through GitHub's web interface.
        blog (Union[Unset, str]):  Example: "http://github.blog".
        advanced_security_enabled_for_new_repositories (Union[Unset, bool]): Whether GitHub Advanced Security is
            automatically enabled for new repositories.

            To use this parameter, you must have admin permissions for the repository or be an owner or security manager for
            the organization that owns the repository. For more information, see "[Managing security managers in your
            organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-
            roles/managing-security-managers-in-your-organization)."

            You can check which security and analysis features are currently enabled by using a `GET /orgs/{org}` request.
        dependabot_alerts_enabled_for_new_repositories (Union[Unset, bool]): Whether Dependabot alerts is automatically
            enabled for new repositories.

            To use this parameter, you must have admin permissions for the repository or be an owner or security manager for
            the organization that owns the repository. For more information, see "[Managing security managers in your
            organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-
            roles/managing-security-managers-in-your-organization)."

            You can check which security and analysis features are currently enabled by using a `GET /orgs/{org}` request.
        dependabot_security_updates_enabled_for_new_repositories (Union[Unset, bool]): Whether Dependabot security
            updates is automatically enabled for new repositories.

            To use this parameter, you must have admin permissions for the repository or be an owner or security manager for
            the organization that owns the repository. For more information, see "[Managing security managers in your
            organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-
            roles/managing-security-managers-in-your-organization)."

            You can check which security and analysis features are currently enabled by using a `GET /orgs/{org}` request.
        dependency_graph_enabled_for_new_repositories (Union[Unset, bool]): Whether dependency graph is automatically
            enabled for new repositories.

            To use this parameter, you must have admin permissions for the repository or be an owner or security manager for
            the organization that owns the repository. For more information, see "[Managing security managers in your
            organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-
            roles/managing-security-managers-in-your-organization)."

            You can check which security and analysis features are currently enabled by using a `GET /orgs/{org}` request.
        secret_scanning_enabled_for_new_repositories (Union[Unset, bool]): Whether secret scanning is automatically
            enabled for new repositories.

            To use this parameter, you must have admin permissions for the repository or be an owner or security manager for
            the organization that owns the repository. For more information, see "[Managing security managers in your
            organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-
            roles/managing-security-managers-in-your-organization)."

            You can check which security and analysis features are currently enabled by using a `GET /orgs/{org}` request.
        secret_scanning_push_protection_enabled_for_new_repositories (Union[Unset, bool]): Whether secret scanning push
            protection is automatically enabled for new repositories.

            To use this parameter, you must have admin permissions for the repository or be an owner or security manager for
            the organization that owns the repository. For more information, see "[Managing security managers in your
            organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-
            roles/managing-security-managers-in-your-organization)."

            You can check which security and analysis features are currently enabled by using a `GET /orgs/{org}` request.
    """

    billing_email: Union[Unset, str] = UNSET
    company: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    twitter_username: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    has_organization_projects: Union[Unset, bool] = UNSET
    has_repository_projects: Union[Unset, bool] = UNSET
    default_repository_permission: Union[
        Unset, OrgsupdateJsonBodyDefaultRepositoryPermission
    ] = OrgsupdateJsonBodyDefaultRepositoryPermission.READ
    members_can_create_repositories: Union[Unset, bool] = True
    members_can_create_internal_repositories: Union[Unset, bool] = UNSET
    members_can_create_private_repositories: Union[Unset, bool] = UNSET
    members_can_create_public_repositories: Union[Unset, bool] = UNSET
    members_allowed_repository_creation_type: Union[
        Unset, OrgsupdateJsonBodyMembersAllowedRepositoryCreationType
    ] = UNSET
    members_can_create_pages: Union[Unset, bool] = True
    members_can_create_public_pages: Union[Unset, bool] = True
    members_can_create_private_pages: Union[Unset, bool] = True
    members_can_fork_private_repositories: Union[Unset, bool] = False
    web_commit_signoff_required: Union[Unset, bool] = False
    blog: Union[Unset, str] = UNSET
    advanced_security_enabled_for_new_repositories: Union[Unset, bool] = UNSET
    dependabot_alerts_enabled_for_new_repositories: Union[Unset, bool] = UNSET
    dependabot_security_updates_enabled_for_new_repositories: Union[Unset, bool] = UNSET
    dependency_graph_enabled_for_new_repositories: Union[Unset, bool] = UNSET
    secret_scanning_enabled_for_new_repositories: Union[Unset, bool] = UNSET
    secret_scanning_push_protection_enabled_for_new_repositories: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        billing_email = self.billing_email
        company = self.company
        email = self.email
        twitter_username = self.twitter_username
        location = self.location
        name = self.name
        description = self.description
        has_organization_projects = self.has_organization_projects
        has_repository_projects = self.has_repository_projects
        default_repository_permission: Union[Unset, str] = UNSET
        if not isinstance(self.default_repository_permission, Unset):
            default_repository_permission = self.default_repository_permission.value

        members_can_create_repositories = self.members_can_create_repositories
        members_can_create_internal_repositories = self.members_can_create_internal_repositories
        members_can_create_private_repositories = self.members_can_create_private_repositories
        members_can_create_public_repositories = self.members_can_create_public_repositories
        members_allowed_repository_creation_type: Union[Unset, str] = UNSET
        if not isinstance(self.members_allowed_repository_creation_type, Unset):
            members_allowed_repository_creation_type = self.members_allowed_repository_creation_type.value

        members_can_create_pages = self.members_can_create_pages
        members_can_create_public_pages = self.members_can_create_public_pages
        members_can_create_private_pages = self.members_can_create_private_pages
        members_can_fork_private_repositories = self.members_can_fork_private_repositories
        web_commit_signoff_required = self.web_commit_signoff_required
        blog = self.blog
        advanced_security_enabled_for_new_repositories = self.advanced_security_enabled_for_new_repositories
        dependabot_alerts_enabled_for_new_repositories = self.dependabot_alerts_enabled_for_new_repositories
        dependabot_security_updates_enabled_for_new_repositories = (
            self.dependabot_security_updates_enabled_for_new_repositories
        )
        dependency_graph_enabled_for_new_repositories = self.dependency_graph_enabled_for_new_repositories
        secret_scanning_enabled_for_new_repositories = self.secret_scanning_enabled_for_new_repositories
        secret_scanning_push_protection_enabled_for_new_repositories = (
            self.secret_scanning_push_protection_enabled_for_new_repositories
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if billing_email is not UNSET:
            field_dict["billing_email"] = billing_email
        if company is not UNSET:
            field_dict["company"] = company
        if email is not UNSET:
            field_dict["email"] = email
        if twitter_username is not UNSET:
            field_dict["twitter_username"] = twitter_username
        if location is not UNSET:
            field_dict["location"] = location
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if has_organization_projects is not UNSET:
            field_dict["has_organization_projects"] = has_organization_projects
        if has_repository_projects is not UNSET:
            field_dict["has_repository_projects"] = has_repository_projects
        if default_repository_permission is not UNSET:
            field_dict["default_repository_permission"] = default_repository_permission
        if members_can_create_repositories is not UNSET:
            field_dict["members_can_create_repositories"] = members_can_create_repositories
        if members_can_create_internal_repositories is not UNSET:
            field_dict["members_can_create_internal_repositories"] = members_can_create_internal_repositories
        if members_can_create_private_repositories is not UNSET:
            field_dict["members_can_create_private_repositories"] = members_can_create_private_repositories
        if members_can_create_public_repositories is not UNSET:
            field_dict["members_can_create_public_repositories"] = members_can_create_public_repositories
        if members_allowed_repository_creation_type is not UNSET:
            field_dict["members_allowed_repository_creation_type"] = members_allowed_repository_creation_type
        if members_can_create_pages is not UNSET:
            field_dict["members_can_create_pages"] = members_can_create_pages
        if members_can_create_public_pages is not UNSET:
            field_dict["members_can_create_public_pages"] = members_can_create_public_pages
        if members_can_create_private_pages is not UNSET:
            field_dict["members_can_create_private_pages"] = members_can_create_private_pages
        if members_can_fork_private_repositories is not UNSET:
            field_dict["members_can_fork_private_repositories"] = members_can_fork_private_repositories
        if web_commit_signoff_required is not UNSET:
            field_dict["web_commit_signoff_required"] = web_commit_signoff_required
        if blog is not UNSET:
            field_dict["blog"] = blog
        if advanced_security_enabled_for_new_repositories is not UNSET:
            field_dict[
                "advanced_security_enabled_for_new_repositories"
            ] = advanced_security_enabled_for_new_repositories
        if dependabot_alerts_enabled_for_new_repositories is not UNSET:
            field_dict[
                "dependabot_alerts_enabled_for_new_repositories"
            ] = dependabot_alerts_enabled_for_new_repositories
        if dependabot_security_updates_enabled_for_new_repositories is not UNSET:
            field_dict[
                "dependabot_security_updates_enabled_for_new_repositories"
            ] = dependabot_security_updates_enabled_for_new_repositories
        if dependency_graph_enabled_for_new_repositories is not UNSET:
            field_dict["dependency_graph_enabled_for_new_repositories"] = dependency_graph_enabled_for_new_repositories
        if secret_scanning_enabled_for_new_repositories is not UNSET:
            field_dict["secret_scanning_enabled_for_new_repositories"] = secret_scanning_enabled_for_new_repositories
        if secret_scanning_push_protection_enabled_for_new_repositories is not UNSET:
            field_dict[
                "secret_scanning_push_protection_enabled_for_new_repositories"
            ] = secret_scanning_push_protection_enabled_for_new_repositories

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        billing_email = d.pop("billing_email", UNSET)

        company = d.pop("company", UNSET)

        email = d.pop("email", UNSET)

        twitter_username = d.pop("twitter_username", UNSET)

        location = d.pop("location", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        has_organization_projects = d.pop("has_organization_projects", UNSET)

        has_repository_projects = d.pop("has_repository_projects", UNSET)

        _default_repository_permission = d.pop("default_repository_permission", UNSET)
        default_repository_permission: Union[Unset, OrgsupdateJsonBodyDefaultRepositoryPermission]
        if isinstance(_default_repository_permission, Unset):
            default_repository_permission = UNSET
        else:
            default_repository_permission = OrgsupdateJsonBodyDefaultRepositoryPermission(
                _default_repository_permission
            )

        members_can_create_repositories = d.pop("members_can_create_repositories", UNSET)

        members_can_create_internal_repositories = d.pop("members_can_create_internal_repositories", UNSET)

        members_can_create_private_repositories = d.pop("members_can_create_private_repositories", UNSET)

        members_can_create_public_repositories = d.pop("members_can_create_public_repositories", UNSET)

        _members_allowed_repository_creation_type = d.pop("members_allowed_repository_creation_type", UNSET)
        members_allowed_repository_creation_type: Union[Unset, OrgsupdateJsonBodyMembersAllowedRepositoryCreationType]
        if isinstance(_members_allowed_repository_creation_type, Unset):
            members_allowed_repository_creation_type = UNSET
        else:
            members_allowed_repository_creation_type = OrgsupdateJsonBodyMembersAllowedRepositoryCreationType(
                _members_allowed_repository_creation_type
            )

        members_can_create_pages = d.pop("members_can_create_pages", UNSET)

        members_can_create_public_pages = d.pop("members_can_create_public_pages", UNSET)

        members_can_create_private_pages = d.pop("members_can_create_private_pages", UNSET)

        members_can_fork_private_repositories = d.pop("members_can_fork_private_repositories", UNSET)

        web_commit_signoff_required = d.pop("web_commit_signoff_required", UNSET)

        blog = d.pop("blog", UNSET)

        advanced_security_enabled_for_new_repositories = d.pop("advanced_security_enabled_for_new_repositories", UNSET)

        dependabot_alerts_enabled_for_new_repositories = d.pop("dependabot_alerts_enabled_for_new_repositories", UNSET)

        dependabot_security_updates_enabled_for_new_repositories = d.pop(
            "dependabot_security_updates_enabled_for_new_repositories", UNSET
        )

        dependency_graph_enabled_for_new_repositories = d.pop("dependency_graph_enabled_for_new_repositories", UNSET)

        secret_scanning_enabled_for_new_repositories = d.pop("secret_scanning_enabled_for_new_repositories", UNSET)

        secret_scanning_push_protection_enabled_for_new_repositories = d.pop(
            "secret_scanning_push_protection_enabled_for_new_repositories", UNSET
        )

        orgsupdate_json_body = cls(
            billing_email=billing_email,
            company=company,
            email=email,
            twitter_username=twitter_username,
            location=location,
            name=name,
            description=description,
            has_organization_projects=has_organization_projects,
            has_repository_projects=has_repository_projects,
            default_repository_permission=default_repository_permission,
            members_can_create_repositories=members_can_create_repositories,
            members_can_create_internal_repositories=members_can_create_internal_repositories,
            members_can_create_private_repositories=members_can_create_private_repositories,
            members_can_create_public_repositories=members_can_create_public_repositories,
            members_allowed_repository_creation_type=members_allowed_repository_creation_type,
            members_can_create_pages=members_can_create_pages,
            members_can_create_public_pages=members_can_create_public_pages,
            members_can_create_private_pages=members_can_create_private_pages,
            members_can_fork_private_repositories=members_can_fork_private_repositories,
            web_commit_signoff_required=web_commit_signoff_required,
            blog=blog,
            advanced_security_enabled_for_new_repositories=advanced_security_enabled_for_new_repositories,
            dependabot_alerts_enabled_for_new_repositories=dependabot_alerts_enabled_for_new_repositories,
            dependabot_security_updates_enabled_for_new_repositories=dependabot_security_updates_enabled_for_new_repositories,
            dependency_graph_enabled_for_new_repositories=dependency_graph_enabled_for_new_repositories,
            secret_scanning_enabled_for_new_repositories=secret_scanning_enabled_for_new_repositories,
            secret_scanning_push_protection_enabled_for_new_repositories=secret_scanning_push_protection_enabled_for_new_repositories,
        )

        orgsupdate_json_body.additional_properties = d
        return orgsupdate_json_body

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
