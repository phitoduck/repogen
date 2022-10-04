from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.actions_cache_usage_org_enterprise import ActionsCacheUsageOrgEnterprise
from ...types import Response


def _get_kwargs(
    enterprise: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/enterprises/{enterprise}/actions/cache/usage".format(client.base_url, enterprise=enterprise)

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
    enterprise: str,
    *,
    client: Client,
) -> Response[ActionsCacheUsageOrgEnterprise]:
    """Get GitHub Actions cache usage for an enterprise

     Gets the total GitHub Actions cache usage for an enterprise.
    The data fetched using this API is refreshed approximately every 5 minutes, so values returned from
    this endpoint may take at least 5 minutes to get updated.
    You must authenticate using an access token with the `admin:enterprise` scope to use this endpoint.

    Args:
        enterprise (str):

    Returns:
        Response[ActionsCacheUsageOrgEnterprise]
    """

    kwargs = _get_kwargs(
        enterprise=enterprise,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    enterprise: str,
    *,
    client: Client,
) -> Optional[ActionsCacheUsageOrgEnterprise]:
    """Get GitHub Actions cache usage for an enterprise

     Gets the total GitHub Actions cache usage for an enterprise.
    The data fetched using this API is refreshed approximately every 5 minutes, so values returned from
    this endpoint may take at least 5 minutes to get updated.
    You must authenticate using an access token with the `admin:enterprise` scope to use this endpoint.

    Args:
        enterprise (str):

    Returns:
        Response[ActionsCacheUsageOrgEnterprise]
    """

    return sync_detailed(
        enterprise=enterprise,
        client=client,
    ).parsed


async def asyncio_detailed(
    enterprise: str,
    *,
    client: Client,
) -> Response[ActionsCacheUsageOrgEnterprise]:
    """Get GitHub Actions cache usage for an enterprise

     Gets the total GitHub Actions cache usage for an enterprise.
    The data fetched using this API is refreshed approximately every 5 minutes, so values returned from
    this endpoint may take at least 5 minutes to get updated.
    You must authenticate using an access token with the `admin:enterprise` scope to use this endpoint.

    Args:
        enterprise (str):

    Returns:
        Response[ActionsCacheUsageOrgEnterprise]
    """

    kwargs = _get_kwargs(
        enterprise=enterprise,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    enterprise: str,
    *,
    client: Client,
) -> Optional[ActionsCacheUsageOrgEnterprise]:
    """Get GitHub Actions cache usage for an enterprise

     Gets the total GitHub Actions cache usage for an enterprise.
    The data fetched using this API is refreshed approximately every 5 minutes, so values returned from
    this endpoint may take at least 5 minutes to get updated.
    You must authenticate using an access token with the `admin:enterprise` scope to use this endpoint.

    Args:
        enterprise (str):

    Returns:
        Response[ActionsCacheUsageOrgEnterprise]
    """

    return (
        await asyncio_detailed(
            enterprise=enterprise,
            client=client,
        )
    ).parsed
