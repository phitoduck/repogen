from typing import Any, Dict

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    org: str,
    runner_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/orgs/{org}/actions/runners/{runner_id}".format(client.base_url, org=org, runner_id=runner_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
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
    runner_id: int,
    *,
    client: Client,
) -> Response[Any]:
    """Delete a self-hosted runner from an organization

     Forces the removal of a self-hosted runner from an organization. You can use this endpoint to
    completely remove the runner when the machine you were using no longer exists.

    You must authenticate using an access token with the `admin:org` scope to use this endpoint.

    Args:
        org (str):
        runner_id (int):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        org=org,
        runner_id=runner_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    org: str,
    runner_id: int,
    *,
    client: Client,
) -> Response[Any]:
    """Delete a self-hosted runner from an organization

     Forces the removal of a self-hosted runner from an organization. You can use this endpoint to
    completely remove the runner when the machine you were using no longer exists.

    You must authenticate using an access token with the `admin:org` scope to use this endpoint.

    Args:
        org (str):
        runner_id (int):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        org=org,
        runner_id=runner_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
