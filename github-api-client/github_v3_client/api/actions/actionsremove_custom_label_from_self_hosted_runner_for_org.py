from typing import Any, Dict

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    org: str,
    runner_id: int,
    name: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/orgs/{org}/actions/runners/{runner_id}/labels/{name}".format(
        client.base_url, org=org, runner_id=runner_id, name=name
    )

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
    name: str,
    *,
    client: Client,
) -> Response[Any]:
    """Remove a custom label from a self-hosted runner for an organization

     Remove a custom label from a self-hosted runner configured
    in an organization. Returns the remaining labels from the runner.

    This endpoint returns a `404 Not Found` status if the custom label is not
    present on the runner.

    You must authenticate using an access token with the `admin:org` scope to use this endpoint.

    Args:
        org (str):
        runner_id (int):
        name (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        org=org,
        runner_id=runner_id,
        name=name,
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
    name: str,
    *,
    client: Client,
) -> Response[Any]:
    """Remove a custom label from a self-hosted runner for an organization

     Remove a custom label from a self-hosted runner configured
    in an organization. Returns the remaining labels from the runner.

    This endpoint returns a `404 Not Found` status if the custom label is not
    present on the runner.

    You must authenticate using an access token with the `admin:org` scope to use this endpoint.

    Args:
        org (str):
        runner_id (int):
        name (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        org=org,
        runner_id=runner_id,
        name=name,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
