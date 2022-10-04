from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.actionsget_actions_cache_list_direction import ActionsgetActionsCacheListDirection
from ...models.actionsget_actions_cache_list_sort import ActionsgetActionsCacheListSort
from ...models.repository_actions_caches import RepositoryActionsCaches
from ...types import UNSET, Response


def _get_kwargs(
    owner: str,
    repo: str,
    *,
    client: Client,
    per_page: int = 30,
    page: int = 1,
    ref: str,
    key: str,
    sort: ActionsgetActionsCacheListSort = ActionsgetActionsCacheListSort.LAST_ACCESSED_AT,
    direction: ActionsgetActionsCacheListDirection = ActionsgetActionsCacheListDirection.DESC,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/actions/caches".format(client.base_url, owner=owner, repo=repo)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["per_page"] = per_page

    params["page"] = page

    params["ref"] = ref

    params["key"] = key

    json_sort = sort.value

    params["sort"] = json_sort

    json_direction = direction.value

    params["direction"] = json_direction

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
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
    per_page: int = 30,
    page: int = 1,
    ref: str,
    key: str,
    sort: ActionsgetActionsCacheListSort = ActionsgetActionsCacheListSort.LAST_ACCESSED_AT,
    direction: ActionsgetActionsCacheListDirection = ActionsgetActionsCacheListDirection.DESC,
) -> Response[RepositoryActionsCaches]:
    """List GitHub Actions caches for a repository

     Lists the GitHub Actions caches for a repository.
    You must authenticate using an access token with the `repo` scope to use this endpoint.
    GitHub Apps must have the `actions:read` permission to use this endpoint.

    Args:
        owner (str):
        repo (str):
        per_page (int):  Default: 30.
        page (int):  Default: 1.
        ref (str): The full Git reference, formatted as `refs/heads/<branch name>`,
            `refs/pull/<number>/merge`, or `refs/pull/<number>/head`.
        key (str):
        sort (ActionsgetActionsCacheListSort):  Default:
            ActionsgetActionsCacheListSort.LAST_ACCESSED_AT.
        direction (ActionsgetActionsCacheListDirection):  Default:
            ActionsgetActionsCacheListDirection.DESC.

    Returns:
        Response[RepositoryActionsCaches]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        client=client,
        per_page=per_page,
        page=page,
        ref=ref,
        key=key,
        sort=sort,
        direction=direction,
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
    per_page: int = 30,
    page: int = 1,
    ref: str,
    key: str,
    sort: ActionsgetActionsCacheListSort = ActionsgetActionsCacheListSort.LAST_ACCESSED_AT,
    direction: ActionsgetActionsCacheListDirection = ActionsgetActionsCacheListDirection.DESC,
) -> Optional[RepositoryActionsCaches]:
    """List GitHub Actions caches for a repository

     Lists the GitHub Actions caches for a repository.
    You must authenticate using an access token with the `repo` scope to use this endpoint.
    GitHub Apps must have the `actions:read` permission to use this endpoint.

    Args:
        owner (str):
        repo (str):
        per_page (int):  Default: 30.
        page (int):  Default: 1.
        ref (str): The full Git reference, formatted as `refs/heads/<branch name>`,
            `refs/pull/<number>/merge`, or `refs/pull/<number>/head`.
        key (str):
        sort (ActionsgetActionsCacheListSort):  Default:
            ActionsgetActionsCacheListSort.LAST_ACCESSED_AT.
        direction (ActionsgetActionsCacheListDirection):  Default:
            ActionsgetActionsCacheListDirection.DESC.

    Returns:
        Response[RepositoryActionsCaches]
    """

    return sync_detailed(
        owner=owner,
        repo=repo,
        client=client,
        per_page=per_page,
        page=page,
        ref=ref,
        key=key,
        sort=sort,
        direction=direction,
    ).parsed


async def asyncio_detailed(
    owner: str,
    repo: str,
    *,
    client: Client,
    per_page: int = 30,
    page: int = 1,
    ref: str,
    key: str,
    sort: ActionsgetActionsCacheListSort = ActionsgetActionsCacheListSort.LAST_ACCESSED_AT,
    direction: ActionsgetActionsCacheListDirection = ActionsgetActionsCacheListDirection.DESC,
) -> Response[RepositoryActionsCaches]:
    """List GitHub Actions caches for a repository

     Lists the GitHub Actions caches for a repository.
    You must authenticate using an access token with the `repo` scope to use this endpoint.
    GitHub Apps must have the `actions:read` permission to use this endpoint.

    Args:
        owner (str):
        repo (str):
        per_page (int):  Default: 30.
        page (int):  Default: 1.
        ref (str): The full Git reference, formatted as `refs/heads/<branch name>`,
            `refs/pull/<number>/merge`, or `refs/pull/<number>/head`.
        key (str):
        sort (ActionsgetActionsCacheListSort):  Default:
            ActionsgetActionsCacheListSort.LAST_ACCESSED_AT.
        direction (ActionsgetActionsCacheListDirection):  Default:
            ActionsgetActionsCacheListDirection.DESC.

    Returns:
        Response[RepositoryActionsCaches]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        client=client,
        per_page=per_page,
        page=page,
        ref=ref,
        key=key,
        sort=sort,
        direction=direction,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    owner: str,
    repo: str,
    *,
    client: Client,
    per_page: int = 30,
    page: int = 1,
    ref: str,
    key: str,
    sort: ActionsgetActionsCacheListSort = ActionsgetActionsCacheListSort.LAST_ACCESSED_AT,
    direction: ActionsgetActionsCacheListDirection = ActionsgetActionsCacheListDirection.DESC,
) -> Optional[RepositoryActionsCaches]:
    """List GitHub Actions caches for a repository

     Lists the GitHub Actions caches for a repository.
    You must authenticate using an access token with the `repo` scope to use this endpoint.
    GitHub Apps must have the `actions:read` permission to use this endpoint.

    Args:
        owner (str):
        repo (str):
        per_page (int):  Default: 30.
        page (int):  Default: 1.
        ref (str): The full Git reference, formatted as `refs/heads/<branch name>`,
            `refs/pull/<number>/merge`, or `refs/pull/<number>/head`.
        key (str):
        sort (ActionsgetActionsCacheListSort):  Default:
            ActionsgetActionsCacheListSort.LAST_ACCESSED_AT.
        direction (ActionsgetActionsCacheListDirection):  Default:
            ActionsgetActionsCacheListDirection.DESC.

    Returns:
        Response[RepositoryActionsCaches]
    """

    return (
        await asyncio_detailed(
            owner=owner,
            repo=repo,
            client=client,
            per_page=per_page,
            page=page,
            ref=ref,
            key=key,
            sort=sort,
            direction=direction,
        )
    ).parsed
