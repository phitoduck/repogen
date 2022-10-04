from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.actions_workflow_access_to_repository import ActionsWorkflowAccessToRepository
from ...types import Response


def _get_kwargs(
    owner: str,
    repo: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/actions/permissions/access".format(client.base_url, owner=owner, repo=repo)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[ActionsWorkflowAccessToRepository]:
    if response.status_code == 200:
        response_200 = ActionsWorkflowAccessToRepository.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ActionsWorkflowAccessToRepository]:
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
) -> Response[ActionsWorkflowAccessToRepository]:
    """Get the level of access for workflows outside of the repository

     Gets the level of access that workflows outside of the repository have to actions and reusable
    workflows in the repository.
    This endpoint only applies to internal repositories. For more information, see \"[Managing GitHub
    Actions settings for a repository](https://docs.github.com/repositories/managing-your-repositorys-
    settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-
    repository#allowing-access-to-components-in-an-internal-repository).\"

    You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps
    must have the
    repository `administration` permission to use this endpoint.

    Args:
        owner (str):
        repo (str):

    Returns:
        Response[ActionsWorkflowAccessToRepository]
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
) -> Optional[ActionsWorkflowAccessToRepository]:
    """Get the level of access for workflows outside of the repository

     Gets the level of access that workflows outside of the repository have to actions and reusable
    workflows in the repository.
    This endpoint only applies to internal repositories. For more information, see \"[Managing GitHub
    Actions settings for a repository](https://docs.github.com/repositories/managing-your-repositorys-
    settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-
    repository#allowing-access-to-components-in-an-internal-repository).\"

    You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps
    must have the
    repository `administration` permission to use this endpoint.

    Args:
        owner (str):
        repo (str):

    Returns:
        Response[ActionsWorkflowAccessToRepository]
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
) -> Response[ActionsWorkflowAccessToRepository]:
    """Get the level of access for workflows outside of the repository

     Gets the level of access that workflows outside of the repository have to actions and reusable
    workflows in the repository.
    This endpoint only applies to internal repositories. For more information, see \"[Managing GitHub
    Actions settings for a repository](https://docs.github.com/repositories/managing-your-repositorys-
    settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-
    repository#allowing-access-to-components-in-an-internal-repository).\"

    You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps
    must have the
    repository `administration` permission to use this endpoint.

    Args:
        owner (str):
        repo (str):

    Returns:
        Response[ActionsWorkflowAccessToRepository]
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
) -> Optional[ActionsWorkflowAccessToRepository]:
    """Get the level of access for workflows outside of the repository

     Gets the level of access that workflows outside of the repository have to actions and reusable
    workflows in the repository.
    This endpoint only applies to internal repositories. For more information, see \"[Managing GitHub
    Actions settings for a repository](https://docs.github.com/repositories/managing-your-repositorys-
    settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-
    repository#allowing-access-to-components-in-an-internal-repository).\"

    You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps
    must have the
    repository `administration` permission to use this endpoint.

    Args:
        owner (str):
        repo (str):

    Returns:
        Response[ActionsWorkflowAccessToRepository]
    """

    return (
        await asyncio_detailed(
            owner=owner,
            repo=repo,
            client=client,
        )
    ).parsed
