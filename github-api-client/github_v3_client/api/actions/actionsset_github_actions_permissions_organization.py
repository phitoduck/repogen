from typing import Any, Dict

import httpx

from ...client import Client
from ...models.actionsset_github_actions_permissions_organization_json_body import (
    ActionssetGithubActionsPermissionsOrganizationJsonBody,
)
from ...types import Response


def _get_kwargs(
    org: str,
    *,
    client: Client,
    json_body: ActionssetGithubActionsPermissionsOrganizationJsonBody,
) -> Dict[str, Any]:
    url = "{}/orgs/{org}/actions/permissions".format(client.base_url, org=org)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    org: str,
    *,
    client: Client,
    json_body: ActionssetGithubActionsPermissionsOrganizationJsonBody,
) -> Response[Any]:
    """Set GitHub Actions permissions for an organization

     Sets the GitHub Actions permissions policy for repositories and allowed actions and reusable
    workflows in an organization.

    If the organization belongs to an enterprise that has set restrictive permissions at the enterprise
    level, such as `allowed_actions` to `selected` actions and reusable workflows, then you cannot
    override them for the organization.

    You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub
    Apps must have the `administration` organization permission to use this API.

    Args:
        org (str):
        json_body (ActionssetGithubActionsPermissionsOrganizationJsonBody):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        org=org,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    org: str,
    *,
    client: Client,
    json_body: ActionssetGithubActionsPermissionsOrganizationJsonBody,
) -> Response[Any]:
    """Set GitHub Actions permissions for an organization

     Sets the GitHub Actions permissions policy for repositories and allowed actions and reusable
    workflows in an organization.

    If the organization belongs to an enterprise that has set restrictive permissions at the enterprise
    level, such as `allowed_actions` to `selected` actions and reusable workflows, then you cannot
    override them for the organization.

    You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub
    Apps must have the `administration` organization permission to use this API.

    Args:
        org (str):
        json_body (ActionssetGithubActionsPermissionsOrganizationJsonBody):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        org=org,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
