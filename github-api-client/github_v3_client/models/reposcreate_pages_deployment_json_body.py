from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReposcreatePagesDeploymentJsonBody")


@attr.s(auto_attribs=True)
class ReposcreatePagesDeploymentJsonBody:
    """The object used to create GitHub Pages deployment

    Attributes:
        artifact_url (str): The URL of an artifact that contains the .zip or .tar of static assets to deploy. The
            artifact belongs to the repository.
        pages_build_version (str): A unique string that represents the version of the build for this deployment.
            Default: 'GITHUB_SHA'.
        oidc_token (str): The OIDC token issued by GitHub Actions certifying the origin of the deployment.
        environment (Union[Unset, str]): The target environment for this GitHub Pages deployment. Default: 'github-
            pages'.
    """

    artifact_url: str
    oidc_token: str
    pages_build_version: str = "GITHUB_SHA"
    environment: Union[Unset, str] = "github-pages"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        artifact_url = self.artifact_url
        pages_build_version = self.pages_build_version
        oidc_token = self.oidc_token
        environment = self.environment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "artifact_url": artifact_url,
                "pages_build_version": pages_build_version,
                "oidc_token": oidc_token,
            }
        )
        if environment is not UNSET:
            field_dict["environment"] = environment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        artifact_url = d.pop("artifact_url")

        pages_build_version = d.pop("pages_build_version")

        oidc_token = d.pop("oidc_token")

        environment = d.pop("environment", UNSET)

        reposcreate_pages_deployment_json_body = cls(
            artifact_url=artifact_url,
            pages_build_version=pages_build_version,
            oidc_token=oidc_token,
            environment=environment,
        )

        reposcreate_pages_deployment_json_body.additional_properties = d
        return reposcreate_pages_deployment_json_body

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
