from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.actions_cache_usage_by_repository import ActionsCacheUsageByRepository
from ...types import Response


def _get_kwargs(
    owner: str,
    repo: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/actions/cache/usage".format(client.base_url, owner=owner, repo=repo)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[ActionsCacheUsageByRepository]:
    if response.status_code == 200:
        response_200 = ActionsCacheUsageByRepository.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ActionsCacheUsageByRepository]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    owner: str,
    repo: str,
    *,
    client: Client,
) -> Response[ActionsCacheUsageByRepository]:
    """Get GitHub Actions cache usage for a repository

     Gets GitHub Actions cache usage for a repository.
    The data fetched using this API is refreshed approximately every 5 minutes, so values returned from
    this endpoint may take at least 5 minutes to get updated.
    Anyone with read access to the repository can use this endpoint. If the repository is private, you
    must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission
    to use this endpoint.

    Args:
        owner (str):
        repo (str):

    Returns:
        Response[ActionsCacheUsageByRepository]
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


def sync(
    owner: str,
    repo: str,
    *,
    client: Client,
) -> Optional[ActionsCacheUsageByRepository]:
    """Get GitHub Actions cache usage for a repository

     Gets GitHub Actions cache usage for a repository.
    The data fetched using this API is refreshed approximately every 5 minutes, so values returned from
    this endpoint may take at least 5 minutes to get updated.
    Anyone with read access to the repository can use this endpoint. If the repository is private, you
    must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission
    to use this endpoint.

    Args:
        owner (str):
        repo (str):

    Returns:
        Response[ActionsCacheUsageByRepository]
    """

    return sync_detailed(
        owner=owner,
        repo=repo,
        client=client,
    ).parsed


async def asyncio_detailed(
    owner: str,
    repo: str,
    *,
    client: Client,
) -> Response[ActionsCacheUsageByRepository]:
    """Get GitHub Actions cache usage for a repository

     Gets GitHub Actions cache usage for a repository.
    The data fetched using this API is refreshed approximately every 5 minutes, so values returned from
    this endpoint may take at least 5 minutes to get updated.
    Anyone with read access to the repository can use this endpoint. If the repository is private, you
    must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission
    to use this endpoint.

    Args:
        owner (str):
        repo (str):

    Returns:
        Response[ActionsCacheUsageByRepository]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    owner: str,
    repo: str,
    *,
    client: Client,
) -> Optional[ActionsCacheUsageByRepository]:
    """Get GitHub Actions cache usage for a repository

     Gets GitHub Actions cache usage for a repository.
    The data fetched using this API is refreshed approximately every 5 minutes, so values returned from
    this endpoint may take at least 5 minutes to get updated.
    Anyone with read access to the repository can use this endpoint. If the repository is private, you
    must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission
    to use this endpoint.

    Args:
        owner (str):
        repo (str):

    Returns:
        Response[ActionsCacheUsageByRepository]
    """

    return (
        await asyncio_detailed(
            owner=owner,
            repo=repo,
            client=client,
        )
    ).parsed
