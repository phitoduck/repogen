from typing import Any, Dict

import httpx

from ...client import Client
from ...models.selected_actions import SelectedActions
from ...types import Response


def _get_kwargs(
    owner: str,
    repo: str,
    *,
    client: Client,
    json_body: SelectedActions,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/actions/permissions/selected-actions".format(client.base_url, owner=owner, repo=repo)

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
    json_body: SelectedActions,
) -> Response[Any]:
    """Set allowed actions and reusable workflows for a repository

     Sets the actions and reusable workflows that are allowed in a repository. To use this endpoint, the
    repository permission policy for `allowed_actions` must be configured to `selected`. For more
    information, see \"[Set GitHub Actions permissions for a repository](#set-github-actions-
    permissions-for-a-repository).\"

    If the repository belongs to an organization or enterprise that has `selected` actions and reusable
    workflows set at the organization or enterprise levels, then you cannot override any of the allowed
    actions and reusable workflows settings.

    To use the `patterns_allowed` setting for private repositories, the repository must belong to an
    enterprise. If the repository does not belong to an enterprise, then the `patterns_allowed` setting
    only applies to public repositories.

    You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps
    must have the `administration` repository permission to use this API.

    Args:
        owner (str):
        repo (str):
        json_body (SelectedActions):

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
    json_body: SelectedActions,
) -> Response[Any]:
    """Set allowed actions and reusable workflows for a repository

     Sets the actions and reusable workflows that are allowed in a repository. To use this endpoint, the
    repository permission policy for `allowed_actions` must be configured to `selected`. For more
    information, see \"[Set GitHub Actions permissions for a repository](#set-github-actions-
    permissions-for-a-repository).\"

    If the repository belongs to an organization or enterprise that has `selected` actions and reusable
    workflows set at the organization or enterprise levels, then you cannot override any of the allowed
    actions and reusable workflows settings.

    To use the `patterns_allowed` setting for private repositories, the repository must belong to an
    enterprise. If the repository does not belong to an enterprise, then the `patterns_allowed` setting
    only applies to public repositories.

    You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps
    must have the `administration` repository permission to use this API.

    Args:
        owner (str):
        repo (str):
        json_body (SelectedActions):

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
