from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.repository_actions_caches import RepositoryActionsCaches
from ...types import UNSET, Response


def _get_kwargs(
    owner: str,
    repo: str,
    *,
    client: Client,
    key: str,
    ref: str,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/actions/caches".format(client.base_url, owner=owner, repo=repo)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["key"] = key

    params["ref"] = ref

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[RepositoryActionsCaches]:
    if response.status_code == 200:
        response_200 = RepositoryActionsCaches.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[RepositoryActionsCaches]:
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
    key: str,
    ref: str,
) -> Response[RepositoryActionsCaches]:
    """Delete GitHub Actions caches for a repository (using a cache key)

     Deletes one or more GitHub Actions caches for a repository, using a complete cache key. By default,
    all caches that match the provided key are deleted, but you can optionally provide a Git ref to
    restrict deletions to caches that match both the provided key and the Git ref.

    You must authenticate using an access token with the `repo` scope to use this endpoint.

    GitHub Apps must have the `actions:write` permission to use this endpoint.

    Args:
        owner (str):
        repo (str):
        key (str):
        ref (str): The full Git reference, formatted as `refs/heads/<branch name>`,
            `refs/pull/<number>/merge`, or `refs/pull/<number>/head`.

    Returns:
        Response[RepositoryActionsCaches]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        client=client,
        key=key,
        ref=ref,
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
    key: str,
    ref: str,
) -> Optional[RepositoryActionsCaches]:
    """Delete GitHub Actions caches for a repository (using a cache key)

     Deletes one or more GitHub Actions caches for a repository, using a complete cache key. By default,
    all caches that match the provided key are deleted, but you can optionally provide a Git ref to
    restrict deletions to caches that match both the provided key and the Git ref.

    You must authenticate using an access token with the `repo` scope to use this endpoint.

    GitHub Apps must have the `actions:write` permission to use this endpoint.

    Args:
        owner (str):
        repo (str):
        key (str):
        ref (str): The full Git reference, formatted as `refs/heads/<branch name>`,
            `refs/pull/<number>/merge`, or `refs/pull/<number>/head`.

    Returns:
        Response[RepositoryActionsCaches]
    """

    return sync_detailed(
        owner=owner,
        repo=repo,
        client=client,
        key=key,
        ref=ref,
    ).parsed


async def asyncio_detailed(
    owner: str,
    repo: str,
    *,
    client: Client,
    key: str,
    ref: str,
) -> Response[RepositoryActionsCaches]:
    """Delete GitHub Actions caches for a repository (using a cache key)

     Deletes one or more GitHub Actions caches for a repository, using a complete cache key. By default,
    all caches that match the provided key are deleted, but you can optionally provide a Git ref to
    restrict deletions to caches that match both the provided key and the Git ref.

    You must authenticate using an access token with the `repo` scope to use this endpoint.

    GitHub Apps must have the `actions:write` permission to use this endpoint.

    Args:
        owner (str):
        repo (str):
        key (str):
        ref (str): The full Git reference, formatted as `refs/heads/<branch name>`,
            `refs/pull/<number>/merge`, or `refs/pull/<number>/head`.

    Returns:
        Response[RepositoryActionsCaches]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        client=client,
        key=key,
        ref=ref,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    owner: str,
    repo: str,
    *,
    client: Client,
    key: str,
    ref: str,
) -> Optional[RepositoryActionsCaches]:
    """Delete GitHub Actions caches for a repository (using a cache key)

     Deletes one or more GitHub Actions caches for a repository, using a complete cache key. By default,
    all caches that match the provided key are deleted, but you can optionally provide a Git ref to
    restrict deletions to caches that match both the provided key and the Git ref.

    You must authenticate using an access token with the `repo` scope to use this endpoint.

    GitHub Apps must have the `actions:write` permission to use this endpoint.

    Args:
        owner (str):
        repo (str):
        key (str):
        ref (str): The full Git reference, formatted as `refs/heads/<branch name>`,
            `refs/pull/<number>/merge`, or `refs/pull/<number>/head`.

    Returns:
        Response[RepositoryActionsCaches]
    """

    return (
        await asyncio_detailed(
            owner=owner,
            repo=repo,
            client=client,
            key=key,
            ref=ref,
        )
    ).parsed
