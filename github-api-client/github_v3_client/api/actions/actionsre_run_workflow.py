from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.actionsre_run_workflow_json_body import ActionsreRunWorkflowJsonBody
from ...models.empty_object import EmptyObject
from ...types import Response


def _get_kwargs(
    owner: str,
    repo: str,
    run_id: int,
    *,
    client: Client,
    json_body: Optional[ActionsreRunWorkflowJsonBody],
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/actions/runs/{run_id}/rerun".format(
        client.base_url, owner=owner, repo=repo, run_id=run_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict() if json_body else None

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[EmptyObject]:
    if response.status_code == 201:
        response_201 = EmptyObject.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[EmptyObject]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    owner: str,
    repo: str,
    run_id: int,
    *,
    client: Client,
    json_body: Optional[ActionsreRunWorkflowJsonBody],
) -> Response[EmptyObject]:
    """Re-run a workflow

     Re-runs your workflow run using its `id`. You must authenticate using an access token with the
    `repo` scope to use this endpoint. GitHub Apps must have the `actions:write` permission to use this
    endpoint.

    Args:
        owner (str):
        repo (str):
        run_id (int):
        json_body (Optional[ActionsreRunWorkflowJsonBody]):

    Returns:
        Response[EmptyObject]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        run_id=run_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    owner: str,
    repo: str,
    run_id: int,
    *,
    client: Client,
    json_body: Optional[ActionsreRunWorkflowJsonBody],
) -> Optional[EmptyObject]:
    """Re-run a workflow

     Re-runs your workflow run using its `id`. You must authenticate using an access token with the
    `repo` scope to use this endpoint. GitHub Apps must have the `actions:write` permission to use this
    endpoint.

    Args:
        owner (str):
        repo (str):
        run_id (int):
        json_body (Optional[ActionsreRunWorkflowJsonBody]):

    Returns:
        Response[EmptyObject]
    """

    return sync_detailed(
        owner=owner,
        repo=repo,
        run_id=run_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    owner: str,
    repo: str,
    run_id: int,
    *,
    client: Client,
    json_body: Optional[ActionsreRunWorkflowJsonBody],
) -> Response[EmptyObject]:
    """Re-run a workflow

     Re-runs your workflow run using its `id`. You must authenticate using an access token with the
    `repo` scope to use this endpoint. GitHub Apps must have the `actions:write` permission to use this
    endpoint.

    Args:
        owner (str):
        repo (str):
        run_id (int):
        json_body (Optional[ActionsreRunWorkflowJsonBody]):

    Returns:
        Response[EmptyObject]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        run_id=run_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    owner: str,
    repo: str,
    run_id: int,
    *,
    client: Client,
    json_body: Optional[ActionsreRunWorkflowJsonBody],
) -> Optional[EmptyObject]:
    """Re-run a workflow

     Re-runs your workflow run using its `id`. You must authenticate using an access token with the
    `repo` scope to use this endpoint. GitHub Apps must have the `actions:write` permission to use this
    endpoint.

    Args:
        owner (str):
        repo (str):
        run_id (int):
        json_body (Optional[ActionsreRunWorkflowJsonBody]):

    Returns:
        Response[EmptyObject]
    """

    return (
        await asyncio_detailed(
            owner=owner,
            repo=repo,
            run_id=run_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
