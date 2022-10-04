from typing import Any, Dict

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    owner: str,
    repo: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/actions/runners/remove-token".format(client.base_url, owner=owner, repo=repo)

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
    owner: str,
    repo: str,
    *,
    client: Client,
) -> Response[Any]:
    """Create a remove token for a repository

     Returns a token that you can pass to remove a self-hosted runner from a repository. The token
    expires after one hour.
    You must authenticate using an access token with the `repo` scope to use this endpoint.

    #### Example using remove token

    To remove your self-hosted runner from a repository, replace TOKEN with the remove token provided by
    this endpoint.

    ```
    ./config.sh remove --token TOKEN
    ```

    Args:
        owner (str):
        repo (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    owner: str,
    repo: str,
    *,
    client: Client,
) -> Response[Any]:
    """Create a remove token for a repository

     Returns a token that you can pass to remove a self-hosted runner from a repository. The token
    expires after one hour.
    You must authenticate using an access token with the `repo` scope to use this endpoint.

    #### Example using remove token

    To remove your self-hosted runner from a repository, replace TOKEN with the remove token provided by
    this endpoint.

    ```
    ./config.sh remove --token TOKEN
    ```

    Args:
        owner (str):
        repo (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
