from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.workflow import Workflow
from ...types import Response


def _get_kwargs(
    owner: str,
    repo: str,
    workflow_id: Union[int, str],
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/actions/workflows/{workflow_id}".format(
        client.base_url, owner=owner, repo=repo, workflow_id=workflow_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Workflow]:
    if response.status_code == 200:
        response_200 = Workflow.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Workflow]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    owner: str,
    repo: str,
    workflow_id: Union[int, str],
    *,
    client: Client,
) -> Response[Workflow]:
    """Get a workflow

     Gets a specific workflow. You can replace `workflow_id` with the workflow file name. For example,
    you could use `main.yaml`. Anyone with read access to the repository can use this endpoint. If the
    repository is private you must use an access token with the `repo` scope. GitHub Apps must have the
    `actions:read` permission to use this endpoint.

    Args:
        owner (str):
        repo (str):
        workflow_id (Union[int, str]):

    Returns:
        Response[Workflow]
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


def sync(
    owner: str,
    repo: str,
    workflow_id: Union[int, str],
    *,
    client: Client,
) -> Optional[Workflow]:
    """Get a workflow

     Gets a specific workflow. You can replace `workflow_id` with the workflow file name. For example,
    you could use `main.yaml`. Anyone with read access to the repository can use this endpoint. If the
    repository is private you must use an access token with the `repo` scope. GitHub Apps must have the
    `actions:read` permission to use this endpoint.

    Args:
        owner (str):
        repo (str):
        workflow_id (Union[int, str]):

    Returns:
        Response[Workflow]
    """

    return sync_detailed(
        owner=owner,
        repo=repo,
        workflow_id=workflow_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    owner: str,
    repo: str,
    workflow_id: Union[int, str],
    *,
    client: Client,
) -> Response[Workflow]:
    """Get a workflow

     Gets a specific workflow. You can replace `workflow_id` with the workflow file name. For example,
    you could use `main.yaml`. Anyone with read access to the repository can use this endpoint. If the
    repository is private you must use an access token with the `repo` scope. GitHub Apps must have the
    `actions:read` permission to use this endpoint.

    Args:
        owner (str):
        repo (str):
        workflow_id (Union[int, str]):

    Returns:
        Response[Workflow]
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


async def asyncio(
    owner: str,
    repo: str,
    workflow_id: Union[int, str],
    *,
    client: Client,
) -> Optional[Workflow]:
    """Get a workflow

     Gets a specific workflow. You can replace `workflow_id` with the workflow file name. For example,
    you could use `main.yaml`. Anyone with read access to the repository can use this endpoint. If the
    repository is private you must use an access token with the `repo` scope. GitHub Apps must have the
    `actions:read` permission to use this endpoint.

    Args:
        owner (str):
        repo (str):
        workflow_id (Union[int, str]):

    Returns:
        Response[Workflow]
    """

    return (
        await asyncio_detailed(
            owner=owner,
            repo=repo,
            workflow_id=workflow_id,
            client=client,
        )
    ).parsed
