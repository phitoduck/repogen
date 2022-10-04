from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.actions_get_default_workflow_permissions import ActionsGetDefaultWorkflowPermissions
from ...types import Response


def _get_kwargs(
    owner: str,
    repo: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/actions/permissions/workflow".format(client.base_url, owner=owner, repo=repo)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[ActionsGetDefaultWorkflowPermissions]:
    if response.status_code == 200:
        response_200 = ActionsGetDefaultWorkflowPermissions.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ActionsGetDefaultWorkflowPermissions]:
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
) -> Response[ActionsGetDefaultWorkflowPermissions]:
    """Get default workflow permissions for a repository

     Gets the default workflow permissions granted to the `GITHUB_TOKEN` when running workflows in a
    repository,
    as well as if GitHub Actions can submit approving pull request reviews.
    For more information, see \"[Setting the permissions of the GITHUB_TOKEN for your
    repository](https://docs.github.com/repositories/managing-your-repositorys-settings-and-
    features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-
    repository#setting-the-permissions-of-the-github_token-for-your-repository).\"

    You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps
    must have the repository `administration` permission to use this API.

    Args:
        owner (str):
        repo (str):

    Returns:
        Response[ActionsGetDefaultWorkflowPermissions]
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
) -> Optional[ActionsGetDefaultWorkflowPermissions]:
    """Get default workflow permissions for a repository

     Gets the default workflow permissions granted to the `GITHUB_TOKEN` when running workflows in a
    repository,
    as well as if GitHub Actions can submit approving pull request reviews.
    For more information, see \"[Setting the permissions of the GITHUB_TOKEN for your
    repository](https://docs.github.com/repositories/managing-your-repositorys-settings-and-
    features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-
    repository#setting-the-permissions-of-the-github_token-for-your-repository).\"

    You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps
    must have the repository `administration` permission to use this API.

    Args:
        owner (str):
        repo (str):

    Returns:
        Response[ActionsGetDefaultWorkflowPermissions]
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
) -> Response[ActionsGetDefaultWorkflowPermissions]:
    """Get default workflow permissions for a repository

     Gets the default workflow permissions granted to the `GITHUB_TOKEN` when running workflows in a
    repository,
    as well as if GitHub Actions can submit approving pull request reviews.
    For more information, see \"[Setting the permissions of the GITHUB_TOKEN for your
    repository](https://docs.github.com/repositories/managing-your-repositorys-settings-and-
    features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-
    repository#setting-the-permissions-of-the-github_token-for-your-repository).\"

    You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps
    must have the repository `administration` permission to use this API.

    Args:
        owner (str):
        repo (str):

    Returns:
        Response[ActionsGetDefaultWorkflowPermissions]
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
) -> Optional[ActionsGetDefaultWorkflowPermissions]:
    """Get default workflow permissions for a repository

     Gets the default workflow permissions granted to the `GITHUB_TOKEN` when running workflows in a
    repository,
    as well as if GitHub Actions can submit approving pull request reviews.
    For more information, see \"[Setting the permissions of the GITHUB_TOKEN for your
    repository](https://docs.github.com/repositories/managing-your-repositorys-settings-and-
    features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-
    repository#setting-the-permissions-of-the-github_token-for-your-repository).\"

    You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps
    must have the repository `administration` permission to use this API.

    Args:
        owner (str):
        repo (str):

    Returns:
        Response[ActionsGetDefaultWorkflowPermissions]
    """

    return (
        await asyncio_detailed(
            owner=owner,
            repo=repo,
            client=client,
        )
    ).parsed
