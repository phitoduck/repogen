from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    owner: str,
    repo: str,
    workflow_id: Union[int, str],
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable".format(
        client.base_url, owner=owner, repo=repo, workflow_id=workflow_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
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
    workflow_id: Union[int, str],
    *,
    client: Client,
) -> Response[Any]:
    """Disable a workflow

     Disables a workflow and sets the `state` of the workflow to `disabled_manually`. You can replace
    `workflow_id` with the workflow file name. For example, you could use `main.yaml`.

    You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps
    must have the `actions:write` permission to use this endpoint.

    Args:
        owner (str):
        repo (str):
        workflow_id (Union[int, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        workflow_id=workflow_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    owner: str,
    repo: str,
    workflow_id: Union[int, str],
    *,
    client: Client,
) -> Response[Any]:
    """Disable a workflow

     Disables a workflow and sets the `state` of the workflow to `disabled_manually`. You can replace
    `workflow_id` with the workflow file name. For example, you could use `main.yaml`.

    You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps
    must have the `actions:write` permission to use this endpoint.

    Args:
        owner (str):
        repo (str):
        workflow_id (Union[int, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        workflow_id=workflow_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
