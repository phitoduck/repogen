from typing import Any, Dict

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    org: str,
    repository_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/orgs/{org}/actions/permissions/repositories/{repository_id}".format(
        client.base_url, org=org, repository_id=repository_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
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
    repository_id: int,
    *,
    client: Client,
) -> Response[Any]:
    """Enable a selected repository for GitHub Actions in an organization

     Adds a repository to the list of selected repositories that are enabled for GitHub Actions in an
    organization. To use this endpoint, the organization permission policy for `enabled_repositories`
    must be must be configured to `selected`. For more information, see \"[Set GitHub Actions
    permissions for an organization](#set-github-actions-permissions-for-an-organization).\"

    You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub
    Apps must have the `administration` organization permission to use this API.

    Args:
        org (str):
        repository_id (int):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        org=org,
        repository_id=repository_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    org: str,
    repository_id: int,
    *,
    client: Client,
) -> Response[Any]:
    """Enable a selected repository for GitHub Actions in an organization

     Adds a repository to the list of selected repositories that are enabled for GitHub Actions in an
    organization. To use this endpoint, the organization permission policy for `enabled_repositories`
    must be must be configured to `selected`. For more information, see \"[Set GitHub Actions
    permissions for an organization](#set-github-actions-permissions-for-an-organization).\"

    You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub
    Apps must have the `administration` organization permission to use this API.

    Args:
        org (str):
        repository_id (int):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        org=org,
        repository_id=repository_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
