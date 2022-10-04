from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.actions_get_default_workflow_permissions import ActionsGetDefaultWorkflowPermissions
from ...types import Response


def _get_kwargs(
    org: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/orgs/{org}/actions/permissions/workflow".format(client.base_url, org=org)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[ActionsGetDefaultWorkflowPermissions]:
    if response.status_code == 200:
        response_200 = ActionsGetDefaultWorkflowPermissions.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ActionsGetDefaultWorkflowPermissions]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    org: str,
    *,
    client: Client,
) -> Response[ActionsGetDefaultWorkflowPermissions]:
    """Get default workflow permissions for an organization

     Gets the default workflow permissions granted to the `GITHUB_TOKEN` when running workflows in an
    organization,
    as well as whether GitHub Actions can submit approving pull request reviews. For more information,
    see
    \"[Setting the permissions of the GITHUB_TOKEN for your
    organization](https://docs.github.com/organizations/managing-organization-settings/disabling-or-
    limiting-github-actions-for-your-organization#setting-the-permissions-of-the-github_token-for-your-
    organization).\"

    You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub
    Apps must have the `administration` organization permission to use this API.

    Args:
        org (str):

    Returns:
        Response[ActionsGetDefaultWorkflowPermissions]
    """

    kwargs = _get_kwargs(
        org=org,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    org: str,
    *,
    client: Client,
) -> Optional[ActionsGetDefaultWorkflowPermissions]:
    """Get default workflow permissions for an organization

     Gets the default workflow permissions granted to the `GITHUB_TOKEN` when running workflows in an
    organization,
    as well as whether GitHub Actions can submit approving pull request reviews. For more information,
    see
    \"[Setting the permissions of the GITHUB_TOKEN for your
    organization](https://docs.github.com/organizations/managing-organization-settings/disabling-or-
    limiting-github-actions-for-your-organization#setting-the-permissions-of-the-github_token-for-your-
    organization).\"

    You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub
    Apps must have the `administration` organization permission to use this API.

    Args:
        org (str):

    Returns:
        Response[ActionsGetDefaultWorkflowPermissions]
    """

    return sync_detailed(
        org=org,
        client=client,
    ).parsed


async def asyncio_detailed(
    org: str,
    *,
    client: Client,
) -> Response[ActionsGetDefaultWorkflowPermissions]:
    """Get default workflow permissions for an organization

     Gets the default workflow permissions granted to the `GITHUB_TOKEN` when running workflows in an
    organization,
    as well as whether GitHub Actions can submit approving pull request reviews. For more information,
    see
    \"[Setting the permissions of the GITHUB_TOKEN for your
    organization](https://docs.github.com/organizations/managing-organization-settings/disabling-or-
    limiting-github-actions-for-your-organization#setting-the-permissions-of-the-github_token-for-your-
    organization).\"

    You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub
    Apps must have the `administration` organization permission to use this API.

    Args:
        org (str):

    Returns:
        Response[ActionsGetDefaultWorkflowPermissions]
    """

    kwargs = _get_kwargs(
        org=org,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    org: str,
    *,
    client: Client,
) -> Optional[ActionsGetDefaultWorkflowPermissions]:
    """Get default workflow permissions for an organization

     Gets the default workflow permissions granted to the `GITHUB_TOKEN` when running workflows in an
    organization,
    as well as whether GitHub Actions can submit approving pull request reviews. For more information,
    see
    \"[Setting the permissions of the GITHUB_TOKEN for your
    organization](https://docs.github.com/organizations/managing-organization-settings/disabling-or-
    limiting-github-actions-for-your-organization#setting-the-permissions-of-the-github_token-for-your-
    organization).\"

    You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub
    Apps must have the `administration` organization permission to use this API.

    Args:
        org (str):

    Returns:
        Response[ActionsGetDefaultWorkflowPermissions]
    """

    return (
        await asyncio_detailed(
            org=org,
            client=client,
        )
    ).parsed
