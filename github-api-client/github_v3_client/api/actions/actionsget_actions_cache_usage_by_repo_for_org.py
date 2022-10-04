from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.actionsget_actions_cache_usage_by_repo_for_org_response_200 import (
    ActionsgetActionsCacheUsageByRepoForOrgResponse200,
)
from ...types import UNSET, Response


def _get_kwargs(
    org: str,
    *,
    client: Client,
    per_page: int = 30,
    page: int = 1,
) -> Dict[str, Any]:
    url = "{}/orgs/{org}/actions/cache/usage-by-repository".format(client.base_url, org=org)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["per_page"] = per_page

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[ActionsgetActionsCacheUsageByRepoForOrgResponse200]:
    if response.status_code == 200:
        response_200 = ActionsgetActionsCacheUsageByRepoForOrgResponse200.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ActionsgetActionsCacheUsageByRepoForOrgResponse200]:
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
    per_page: int = 30,
    page: int = 1,
) -> Response[ActionsgetActionsCacheUsageByRepoForOrgResponse200]:
    """List repositories with GitHub Actions cache usage for an organization

     Lists repositories and their GitHub Actions cache usage for an organization.
    The data fetched using this API is refreshed approximately every 5 minutes, so values returned from
    this endpoint may take at least 5 minutes to get updated.
    You must authenticate using an access token with the `read:org` scope to use this endpoint. GitHub
    Apps must have the `organization_admistration:read` permission to use this endpoint.

    Args:
        org (str):
        per_page (int):  Default: 30.
        page (int):  Default: 1.

    Returns:
        Response[ActionsgetActionsCacheUsageByRepoForOrgResponse200]
    """

    kwargs = _get_kwargs(
        org=org,
        client=client,
        per_page=per_page,
        page=page,
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
    per_page: int = 30,
    page: int = 1,
) -> Optional[ActionsgetActionsCacheUsageByRepoForOrgResponse200]:
    """List repositories with GitHub Actions cache usage for an organization

     Lists repositories and their GitHub Actions cache usage for an organization.
    The data fetched using this API is refreshed approximately every 5 minutes, so values returned from
    this endpoint may take at least 5 minutes to get updated.
    You must authenticate using an access token with the `read:org` scope to use this endpoint. GitHub
    Apps must have the `organization_admistration:read` permission to use this endpoint.

    Args:
        org (str):
        per_page (int):  Default: 30.
        page (int):  Default: 1.

    Returns:
        Response[ActionsgetActionsCacheUsageByRepoForOrgResponse200]
    """

    return sync_detailed(
        org=org,
        client=client,
        per_page=per_page,
        page=page,
    ).parsed


async def asyncio_detailed(
    org: str,
    *,
    client: Client,
    per_page: int = 30,
    page: int = 1,
) -> Response[ActionsgetActionsCacheUsageByRepoForOrgResponse200]:
    """List repositories with GitHub Actions cache usage for an organization

     Lists repositories and their GitHub Actions cache usage for an organization.
    The data fetched using this API is refreshed approximately every 5 minutes, so values returned from
    this endpoint may take at least 5 minutes to get updated.
    You must authenticate using an access token with the `read:org` scope to use this endpoint. GitHub
    Apps must have the `organization_admistration:read` permission to use this endpoint.

    Args:
        org (str):
        per_page (int):  Default: 30.
        page (int):  Default: 1.

    Returns:
        Response[ActionsgetActionsCacheUsageByRepoForOrgResponse200]
    """

    kwargs = _get_kwargs(
        org=org,
        client=client,
        per_page=per_page,
        page=page,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    org: str,
    *,
    client: Client,
    per_page: int = 30,
    page: int = 1,
) -> Optional[ActionsgetActionsCacheUsageByRepoForOrgResponse200]:
    """List repositories with GitHub Actions cache usage for an organization

     Lists repositories and their GitHub Actions cache usage for an organization.
    The data fetched using this API is refreshed approximately every 5 minutes, so values returned from
    this endpoint may take at least 5 minutes to get updated.
    You must authenticate using an access token with the `read:org` scope to use this endpoint. GitHub
    Apps must have the `organization_admistration:read` permission to use this endpoint.

    Args:
        org (str):
        per_page (int):  Default: 30.
        page (int):  Default: 1.

    Returns:
        Response[ActionsgetActionsCacheUsageByRepoForOrgResponse200]
    """

    return (
        await asyncio_detailed(
            org=org,
            client=client,
            per_page=per_page,
            page=page,
        )
    ).parsed
