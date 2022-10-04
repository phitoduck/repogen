from typing import Any, Dict

import httpx

from ...client import Client
from ...models.actionsset_github_actions_permissions_repository_json_body import (
    ActionssetGithubActionsPermissionsRepositoryJsonBody,
)
from ...types import Response


def _get_kwargs(
    owner: str,
    repo: str,
    *,
    client: Client,
    json_body: ActionssetGithubActionsPermissionsRepositoryJsonBody,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/actions/permissions".format(client.base_url, owner=owner, repo=repo)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
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
    json_body: ActionssetGithubActionsPermissionsRepositoryJsonBody,
) -> Response[Any]:
    """Set GitHub Actions permissions for a repository

     Sets the GitHub Actions permissions policy for enabling GitHub Actions and allowed actions and
    reusable workflows in the repository.

    If the repository belongs to an organization or enterprise that has set restrictive permissions at
    the organization or enterprise levels, such as `allowed_actions` to `selected` actions and reusable
    workflows, then you cannot override them for the repository.

    You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps
    must have the `administration` repository permission to use this API.

    Args:
        owner (str):
        repo (str):
        json_body (ActionssetGithubActionsPermissionsRepositoryJsonBody):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        client=client,
        json_body=json_body,
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
    json_body: ActionssetGithubActionsPermissionsRepositoryJsonBody,
) -> Response[Any]:
    """Set GitHub Actions permissions for a repository

     Sets the GitHub Actions permissions policy for enabling GitHub Actions and allowed actions and
    reusable workflows in the repository.

    If the repository belongs to an organization or enterprise that has set restrictive permissions at
    the organization or enterprise levels, such as `allowed_actions` to `selected` actions and reusable
    workflows, then you cannot override them for the repository.

    You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps
    must have the `administration` repository permission to use this API.

    Args:
        owner (str):
        repo (str):
        json_body (ActionssetGithubActionsPermissionsRepositoryJsonBody):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
