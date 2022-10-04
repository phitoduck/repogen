from typing import Any, Dict

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    owner: str,
    repo: str,
    cache_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/actions/caches/{cache_id}".format(
        client.base_url, owner=owner, repo=repo, cache_id=cache_id
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
    owner: str,
    repo: str,
    cache_id: int,
    *,
    client: Client,
) -> Response[Any]:
    """Delete a GitHub Actions cache for a repository (using a cache ID)

     Deletes a GitHub Actions cache for a repository, using a cache ID.

    You must authenticate using an access token with the `repo` scope to use this endpoint.

    GitHub Apps must have the `actions:write` permission to use this endpoint.

    Args:
        owner (str):
        repo (str):
        cache_id (int):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        cache_id=cache_id,
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
    cache_id: int,
    *,
    client: Client,
) -> Response[Any]:
    """Delete a GitHub Actions cache for a repository (using a cache ID)

     Deletes a GitHub Actions cache for a repository, using a cache ID.

    You must authenticate using an access token with the `repo` scope to use this endpoint.

    GitHub Apps must have the `actions:write` permission to use this endpoint.

    Args:
        owner (str):
        repo (str):
        cache_id (int):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        cache_id=cache_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
