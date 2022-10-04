from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.actionslist_workflow_run_artifacts_response_200 import ActionslistWorkflowRunArtifactsResponse200
from ...types import UNSET, Response


def _get_kwargs(
    owner: str,
    repo: str,
    run_id: int,
    *,
    client: Client,
    per_page: int = 30,
    page: int = 1,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/actions/runs/{run_id}/artifacts".format(
        client.base_url, owner=owner, repo=repo, run_id=run_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["per_page"] = per_page

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[ActionslistWorkflowRunArtifactsResponse200]:
    if response.status_code == 200:
        response_200 = ActionslistWorkflowRunArtifactsResponse200.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ActionslistWorkflowRunArtifactsResponse200]:
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
    per_page: int = 30,
    page: int = 1,
) -> Response[ActionslistWorkflowRunArtifactsResponse200]:
    """List workflow run artifacts

     Lists artifacts for a workflow run. Anyone with read access to the repository can use this endpoint.
    If the repository is private you must use an access token with the `repo` scope. GitHub Apps must
    have the `actions:read` permission to use this endpoint.

    Args:
        owner (str):
        repo (str):
        run_id (int):
        per_page (int):  Default: 30.
        page (int):  Default: 1.

    Returns:
        Response[ActionslistWorkflowRunArtifactsResponse200]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        run_id=run_id,
        client=client,
        per_page=per_page,
        page=page,
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
    per_page: int = 30,
    page: int = 1,
) -> Optional[ActionslistWorkflowRunArtifactsResponse200]:
    """List workflow run artifacts

     Lists artifacts for a workflow run. Anyone with read access to the repository can use this endpoint.
    If the repository is private you must use an access token with the `repo` scope. GitHub Apps must
    have the `actions:read` permission to use this endpoint.

    Args:
        owner (str):
        repo (str):
        run_id (int):
        per_page (int):  Default: 30.
        page (int):  Default: 1.

    Returns:
        Response[ActionslistWorkflowRunArtifactsResponse200]
    """

    return sync_detailed(
        owner=owner,
        repo=repo,
        run_id=run_id,
        client=client,
        per_page=per_page,
        page=page,
    ).parsed


async def asyncio_detailed(
    owner: str,
    repo: str,
    run_id: int,
    *,
    client: Client,
    per_page: int = 30,
    page: int = 1,
) -> Response[ActionslistWorkflowRunArtifactsResponse200]:
    """List workflow run artifacts

     Lists artifacts for a workflow run. Anyone with read access to the repository can use this endpoint.
    If the repository is private you must use an access token with the `repo` scope. GitHub Apps must
    have the `actions:read` permission to use this endpoint.

    Args:
        owner (str):
        repo (str):
        run_id (int):
        per_page (int):  Default: 30.
        page (int):  Default: 1.

    Returns:
        Response[ActionslistWorkflowRunArtifactsResponse200]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        run_id=run_id,
        client=client,
        per_page=per_page,
        page=page,
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
    per_page: int = 30,
    page: int = 1,
) -> Optional[ActionslistWorkflowRunArtifactsResponse200]:
    """List workflow run artifacts

     Lists artifacts for a workflow run. Anyone with read access to the repository can use this endpoint.
    If the repository is private you must use an access token with the `repo` scope. GitHub Apps must
    have the `actions:read` permission to use this endpoint.

    Args:
        owner (str):
        repo (str):
        run_id (int):
        per_page (int):  Default: 30.
        page (int):  Default: 1.

    Returns:
        Response[ActionslistWorkflowRunArtifactsResponse200]
    """

    return (
        await asyncio_detailed(
            owner=owner,
            repo=repo,
            run_id=run_id,
            client=client,
            per_page=per_page,
            page=page,
        )
    ).parsed
