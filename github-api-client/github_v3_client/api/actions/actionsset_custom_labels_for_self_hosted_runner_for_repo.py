from typing import Any, Dict

import httpx

from ...client import Client
from ...models.actionsset_custom_labels_for_self_hosted_runner_for_repo_json_body import (
    ActionssetCustomLabelsForSelfHostedRunnerForRepoJsonBody,
)
from ...types import Response


def _get_kwargs(
    owner: str,
    repo: str,
    runner_id: int,
    *,
    client: Client,
    json_body: ActionssetCustomLabelsForSelfHostedRunnerForRepoJsonBody,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/actions/runners/{runner_id}/labels".format(
        client.base_url, owner=owner, repo=repo, runner_id=runner_id
    )

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
    runner_id: int,
    *,
    client: Client,
    json_body: ActionssetCustomLabelsForSelfHostedRunnerForRepoJsonBody,
) -> Response[Any]:
    """Set custom labels for a self-hosted runner for a repository

     Remove all previous custom labels and set the new custom labels for a specific
    self-hosted runner configured in a repository.

    You must authenticate using an access token with the `repo` scope to use this
    endpoint.

    Args:
        owner (str):
        repo (str):
        runner_id (int):
        json_body (ActionssetCustomLabelsForSelfHostedRunnerForRepoJsonBody):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        runner_id=runner_id,
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
    runner_id: int,
    *,
    client: Client,
    json_body: ActionssetCustomLabelsForSelfHostedRunnerForRepoJsonBody,
) -> Response[Any]:
    """Set custom labels for a self-hosted runner for a repository

     Remove all previous custom labels and set the new custom labels for a specific
    self-hosted runner configured in a repository.

    You must authenticate using an access token with the `repo` scope to use this
    endpoint.

    Args:
        owner (str):
        repo (str):
        runner_id (int):
        json_body (ActionssetCustomLabelsForSelfHostedRunnerForRepoJsonBody):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        runner_id=runner_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
