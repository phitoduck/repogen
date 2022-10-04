from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.actions_organization_permissions import ActionsOrganizationPermissions
from ...types import Response


def _get_kwargs(
    org: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/orgs/{org}/actions/permissions".format(client.base_url, org=org)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[ActionsOrganizationPermissions]:
    if response.status_code == 200:
        response_200 = ActionsOrganizationPermissions.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ActionsOrganizationPermissions]:
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
) -> Response[ActionsOrganizationPermissions]:
    """Get GitHub Actions permissions for an organization

     Gets the GitHub Actions permissions policy for repositories and allowed actions and reusable
    workflows in an organization.

    You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub
    Apps must have the `administration` organization permission to use this API.

    Args:
        org (str):

    Returns:
        Response[ActionsOrganizationPermissions]
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
) -> Optional[ActionsOrganizationPermissions]:
    """Get GitHub Actions permissions for an organization

     Gets the GitHub Actions permissions policy for repositories and allowed actions and reusable
    workflows in an organization.

    You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub
    Apps must have the `administration` organization permission to use this API.

    Args:
        org (str):

    Returns:
        Response[ActionsOrganizationPermissions]
    """

    return sync_detailed(
        org=org,
        client=client,
    ).parsed


async def asyncio_detailed(
    org: str,
    *,
    client: Client,
) -> Response[ActionsOrganizationPermissions]:
    """Get GitHub Actions permissions for an organization

     Gets the GitHub Actions permissions policy for repositories and allowed actions and reusable
    workflows in an organization.

    You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub
    Apps must have the `administration` organization permission to use this API.

    Args:
        org (str):

    Returns:
        Response[ActionsOrganizationPermissions]
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
) -> Optional[ActionsOrganizationPermissions]:
    """Get GitHub Actions permissions for an organization

     Gets the GitHub Actions permissions policy for repositories and allowed actions and reusable
    workflows in an organization.

    You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub
    Apps must have the `administration` organization permission to use this API.

    Args:
        org (str):

    Returns:
        Response[ActionsOrganizationPermissions]
    """

    return (
        await asyncio_detailed(
            org=org,
            client=client,
        )
    ).parsed
