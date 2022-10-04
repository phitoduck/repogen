from typing import Any, Dict

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    org: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/orgs/{org}/actions/runners/remove-token".format(client.base_url, org=org)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
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
    *,
    client: Client,
) -> Response[Any]:
    """Create a remove token for an organization

     Returns a token that you can pass to the `config` script to remove a self-hosted runner from an
    organization. The token expires after one hour.

    You must authenticate using an access token with the `admin:org` scope to use this endpoint.

    #### Example using remove token

    To remove your self-hosted runner from an organization, replace `TOKEN` with the remove token
    provided by this
    endpoint.

    ```
    ./config.sh remove --token TOKEN
    ```

    Args:
        org (str):

    Returns:
        Response[Any]
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


async def asyncio_detailed(
    org: str,
    *,
    client: Client,
) -> Response[Any]:
    """Create a remove token for an organization

     Returns a token that you can pass to the `config` script to remove a self-hosted runner from an
    organization. The token expires after one hour.

    You must authenticate using an access token with the `admin:org` scope to use this endpoint.

    #### Example using remove token

    To remove your self-hosted runner from an organization, replace `TOKEN` with the remove token
    provided by this
    endpoint.

    ```
    ./config.sh remove --token TOKEN
    ```

    Args:
        org (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        org=org,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
