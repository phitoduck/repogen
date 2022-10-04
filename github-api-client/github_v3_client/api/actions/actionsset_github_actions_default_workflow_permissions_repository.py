from typing import Any, Dict

import httpx

from ...client import Client
from ...models.actions_set_default_workflow_permissions import ActionsSetDefaultWorkflowPermissions
from ...types import Response


def _get_kwargs(
    owner: str,
    repo: str,
    *,
    client: Client,
    json_body: ActionsSetDefaultWorkflowPermissions,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/actions/permissions/workflow".format(client.base_url, owner=owner, repo=repo)

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
    json_body: ActionsSetDefaultWorkflowPermissions,
) -> Response[Any]:
    """Set default workflow permissions for a repository

     Sets the default workflow permissions granted to the `GITHUB_TOKEN` when running workflows in a
    repository, and sets if GitHub Actions
    can submit approving pull request reviews.
    For more information, see \"[Setting the permissions of the GITHUB_TOKEN for your
    repository](https://docs.github.com/repositories/managing-your-repositorys-settings-and-
    features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-
    repository#setting-the-permissions-of-the-github_token-for-your-repository).\"

    You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps
    must have the repository `administration` permission to use this API.

    Args:
        owner (str):
        repo (str):
        json_body (ActionsSetDefaultWorkflowPermissions):

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
    json_body: ActionsSetDefaultWorkflowPermissions,
) -> Response[Any]:
    """Set default workflow permissions for a repository

     Sets the default workflow permissions granted to the `GITHUB_TOKEN` when running workflows in a
    repository, and sets if GitHub Actions
    can submit approving pull request reviews.
    For more information, see \"[Setting the permissions of the GITHUB_TOKEN for your
    repository](https://docs.github.com/repositories/managing-your-repositorys-settings-and-
    features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-
    repository#setting-the-permissions-of-the-github_token-for-your-repository).\"

    You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps
    must have the repository `administration` permission to use this API.

    Args:
        owner (str):
        repo (str):
        json_body (ActionsSetDefaultWorkflowPermissions):

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
