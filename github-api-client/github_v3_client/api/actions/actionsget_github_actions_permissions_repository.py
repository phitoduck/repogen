from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.actions_repository_permissions import ActionsRepositoryPermissions
from ...types import Response


def _get_kwargs(
    owner: str,
    repo: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/actions/permissions".format(client.base_url, owner=owner, repo=repo)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[ActionsRepositoryPermissions]:
    if response.status_code == 200:
        response_200 = ActionsRepositoryPermissions.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ActionsRepositoryPermissions]:
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
) -> Response[ActionsRepositoryPermissions]:
    """Get GitHub Actions permissions for a repository

     Gets the GitHub Actions permissions policy for a repository, including whether GitHub Actions is
    enabled and the actions and reusable workflows allowed to run in the repository.

    You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps
    must have the `administration` repository permission to use this API.

    Args:
        owner (str):
        repo (str):

    Returns:
        Response[ActionsRepositoryPermissions]
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
) -> Optional[ActionsRepositoryPermissions]:
    """Get GitHub Actions permissions for a repository

     Gets the GitHub Actions permissions policy for a repository, including whether GitHub Actions is
    enabled and the actions and reusable workflows allowed to run in the repository.

    You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps
    must have the `administration` repository permission to use this API.

    Args:
        owner (str):
        repo (str):

    Returns:
        Response[ActionsRepositoryPermissions]
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
) -> Response[ActionsRepositoryPermissions]:
    """Get GitHub Actions permissions for a repository

     Gets the GitHub Actions permissions policy for a repository, including whether GitHub Actions is
    enabled and the actions and reusable workflows allowed to run in the repository.

    You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps
    must have the `administration` repository permission to use this API.

    Args:
        owner (str):
        repo (str):

    Returns:
        Response[ActionsRepositoryPermissions]
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
) -> Optional[ActionsRepositoryPermissions]:
    """Get GitHub Actions permissions for a repository

     Gets the GitHub Actions permissions policy for a repository, including whether GitHub Actions is
    enabled and the actions and reusable workflows allowed to run in the repository.

    You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps
    must have the `administration` repository permission to use this API.

    Args:
        owner (str):
        repo (str):

    Returns:
        Response[ActionsRepositoryPermissions]
    """

    return (
        await asyncio_detailed(
            owner=owner,
            repo=repo,
            client=client,
        )
    ).parsed
