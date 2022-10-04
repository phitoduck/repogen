from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.selected_actions import SelectedActions
from ...types import Response


def _get_kwargs(
    owner: str,
    repo: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/actions/permissions/selected-actions".format(client.base_url, owner=owner, repo=repo)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[SelectedActions]:
    if response.status_code == 200:
        response_200 = SelectedActions.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[SelectedActions]:
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
) -> Response[SelectedActions]:
    """Get allowed actions and reusable workflows for a repository

     Gets the settings for selected actions and reusable workflows that are allowed in a repository. To
    use this endpoint, the repository policy for `allowed_actions` must be configured to `selected`. For
    more information, see \"[Set GitHub Actions permissions for a repository](#set-github-actions-
    permissions-for-a-repository).\"

    You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps
    must have the `administration` repository permission to use this API.

    Args:
        owner (str):
        repo (str):

    Returns:
        Response[SelectedActions]
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
) -> Optional[SelectedActions]:
    """Get allowed actions and reusable workflows for a repository

     Gets the settings for selected actions and reusable workflows that are allowed in a repository. To
    use this endpoint, the repository policy for `allowed_actions` must be configured to `selected`. For
    more information, see \"[Set GitHub Actions permissions for a repository](#set-github-actions-
    permissions-for-a-repository).\"

    You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps
    must have the `administration` repository permission to use this API.

    Args:
        owner (str):
        repo (str):

    Returns:
        Response[SelectedActions]
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
) -> Response[SelectedActions]:
    """Get allowed actions and reusable workflows for a repository

     Gets the settings for selected actions and reusable workflows that are allowed in a repository. To
    use this endpoint, the repository policy for `allowed_actions` must be configured to `selected`. For
    more information, see \"[Set GitHub Actions permissions for a repository](#set-github-actions-
    permissions-for-a-repository).\"

    You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps
    must have the `administration` repository permission to use this API.

    Args:
        owner (str):
        repo (str):

    Returns:
        Response[SelectedActions]
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
) -> Optional[SelectedActions]:
    """Get allowed actions and reusable workflows for a repository

     Gets the settings for selected actions and reusable workflows that are allowed in a repository. To
    use this endpoint, the repository policy for `allowed_actions` must be configured to `selected`. For
    more information, see \"[Set GitHub Actions permissions for a repository](#set-github-actions-
    permissions-for-a-repository).\"

    You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps
    must have the `administration` repository permission to use this API.

    Args:
        owner (str):
        repo (str):

    Returns:
        Response[SelectedActions]
    """

    return (
        await asyncio_detailed(
            owner=owner,
            repo=repo,
            client=client,
        )
    ).parsed
