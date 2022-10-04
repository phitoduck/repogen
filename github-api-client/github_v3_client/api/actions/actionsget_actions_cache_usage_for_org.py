from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.actions_cache_usage_org_enterprise import ActionsCacheUsageOrgEnterprise
from ...types import Response


def _get_kwargs(
    org: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/orgs/{org}/actions/cache/usage".format(client.base_url, org=org)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[ActionsCacheUsageOrgEnterprise]:
    if response.status_code == 200:
        response_200 = ActionsCacheUsageOrgEnterprise.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ActionsCacheUsageOrgEnterprise]:
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
) -> Response[ActionsCacheUsageOrgEnterprise]:
    """Get GitHub Actions cache usage for an organization

     Gets the total GitHub Actions cache usage for an organization.
    The data fetched using this API is refreshed approximately every 5 minutes, so values returned from
    this endpoint may take at least 5 minutes to get updated.
    You must authenticate using an access token with the `read:org` scope to use this endpoint. GitHub
    Apps must have the `organization_admistration:read` permission to use this endpoint.

    Args:
        org (str):

    Returns:
        Response[ActionsCacheUsageOrgEnterprise]
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
) -> Optional[ActionsCacheUsageOrgEnterprise]:
    """Get GitHub Actions cache usage for an organization

     Gets the total GitHub Actions cache usage for an organization.
    The data fetched using this API is refreshed approximately every 5 minutes, so values returned from
    this endpoint may take at least 5 minutes to get updated.
    You must authenticate using an access token with the `read:org` scope to use this endpoint. GitHub
    Apps must have the `organization_admistration:read` permission to use this endpoint.

    Args:
        org (str):

    Returns:
        Response[ActionsCacheUsageOrgEnterprise]
    """

    return sync_detailed(
        org=org,
        client=client,
    ).parsed


async def asyncio_detailed(
    org: str,
    *,
    client: Client,
) -> Response[ActionsCacheUsageOrgEnterprise]:
    """Get GitHub Actions cache usage for an organization

     Gets the total GitHub Actions cache usage for an organization.
    The data fetched using this API is refreshed approximately every 5 minutes, so values returned from
    this endpoint may take at least 5 minutes to get updated.
    You must authenticate using an access token with the `read:org` scope to use this endpoint. GitHub
    Apps must have the `organization_admistration:read` permission to use this endpoint.

    Args:
        org (str):

    Returns:
        Response[ActionsCacheUsageOrgEnterprise]
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
) -> Optional[ActionsCacheUsageOrgEnterprise]:
    """Get GitHub Actions cache usage for an organization

     Gets the total GitHub Actions cache usage for an organization.
    The data fetched using this API is refreshed approximately every 5 minutes, so values returned from
    this endpoint may take at least 5 minutes to get updated.
    You must authenticate using an access token with the `read:org` scope to use this endpoint. GitHub
    Apps must have the `organization_admistration:read` permission to use this endpoint.

    Args:
        org (str):

    Returns:
        Response[ActionsCacheUsageOrgEnterprise]
    """

    return (
        await asyncio_detailed(
            org=org,
            client=client,
        )
    ).parsed
