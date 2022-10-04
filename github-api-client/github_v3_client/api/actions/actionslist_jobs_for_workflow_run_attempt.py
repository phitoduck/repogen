from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.actionslist_jobs_for_workflow_run_attempt_response_200 import (
    ActionslistJobsForWorkflowRunAttemptResponse200,
)
from ...types import UNSET, Response


def _get_kwargs(
    owner: str,
    repo: str,
    run_id: int,
    attempt_number: int,
    *,
    client: Client,
    per_page: int = 30,
    page: int = 1,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}/jobs".format(
        client.base_url, owner=owner, repo=repo, run_id=run_id, attempt_number=attempt_number
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


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[ActionslistJobsForWorkflowRunAttemptResponse200, Any]]:
    if response.status_code == 200:
        response_200 = ActionslistJobsForWorkflowRunAttemptResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[ActionslistJobsForWorkflowRunAttemptResponse200, Any]]:
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
    attempt_number: int,
    *,
    client: Client,
    per_page: int = 30,
    page: int = 1,
) -> Response[Union[ActionslistJobsForWorkflowRunAttemptResponse200, Any]]:
    """List jobs for a workflow run attempt

     Lists jobs for a specific workflow run attempt. Anyone with read access to the repository can use
    this endpoint. If the repository is private you must use an access token with the `repo` scope.
    GitHub Apps must have the `actions:read` permission to use this endpoint. You can use parameters to
    narrow the list of results. For more information about using parameters, see
    [Parameters](https://docs.github.com/rest/overview/resources-in-the-rest-api#parameters).

    Args:
        owner (str):
        repo (str):
        run_id (int):
        attempt_number (int):
        per_page (int):  Default: 30.
        page (int):  Default: 1.

    Returns:
        Response[Union[ActionslistJobsForWorkflowRunAttemptResponse200, Any]]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        run_id=run_id,
        attempt_number=attempt_number,
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
    attempt_number: int,
    *,
    client: Client,
    per_page: int = 30,
    page: int = 1,
) -> Optional[Union[ActionslistJobsForWorkflowRunAttemptResponse200, Any]]:
    """List jobs for a workflow run attempt

     Lists jobs for a specific workflow run attempt. Anyone with read access to the repository can use
    this endpoint. If the repository is private you must use an access token with the `repo` scope.
    GitHub Apps must have the `actions:read` permission to use this endpoint. You can use parameters to
    narrow the list of results. For more information about using parameters, see
    [Parameters](https://docs.github.com/rest/overview/resources-in-the-rest-api#parameters).

    Args:
        owner (str):
        repo (str):
        run_id (int):
        attempt_number (int):
        per_page (int):  Default: 30.
        page (int):  Default: 1.

    Returns:
        Response[Union[ActionslistJobsForWorkflowRunAttemptResponse200, Any]]
    """

    return sync_detailed(
        owner=owner,
        repo=repo,
        run_id=run_id,
        attempt_number=attempt_number,
        client=client,
        per_page=per_page,
        page=page,
    ).parsed


async def asyncio_detailed(
    owner: str,
    repo: str,
    run_id: int,
    attempt_number: int,
    *,
    client: Client,
    per_page: int = 30,
    page: int = 1,
) -> Response[Union[ActionslistJobsForWorkflowRunAttemptResponse200, Any]]:
    """List jobs for a workflow run attempt

     Lists jobs for a specific workflow run attempt. Anyone with read access to the repository can use
    this endpoint. If the repository is private you must use an access token with the `repo` scope.
    GitHub Apps must have the `actions:read` permission to use this endpoint. You can use parameters to
    narrow the list of results. For more information about using parameters, see
    [Parameters](https://docs.github.com/rest/overview/resources-in-the-rest-api#parameters).

    Args:
        owner (str):
        repo (str):
        run_id (int):
        attempt_number (int):
        per_page (int):  Default: 30.
        page (int):  Default: 1.

    Returns:
        Response[Union[ActionslistJobsForWorkflowRunAttemptResponse200, Any]]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        run_id=run_id,
        attempt_number=attempt_number,
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
    attempt_number: int,
    *,
    client: Client,
    per_page: int = 30,
    page: int = 1,
) -> Optional[Union[ActionslistJobsForWorkflowRunAttemptResponse200, Any]]:
    """List jobs for a workflow run attempt

     Lists jobs for a specific workflow run attempt. Anyone with read access to the repository can use
    this endpoint. If the repository is private you must use an access token with the `repo` scope.
    GitHub Apps must have the `actions:read` permission to use this endpoint. You can use parameters to
    narrow the list of results. For more information about using parameters, see
    [Parameters](https://docs.github.com/rest/overview/resources-in-the-rest-api#parameters).

    Args:
        owner (str):
        repo (str):
        run_id (int):
        attempt_number (int):
        per_page (int):  Default: 30.
        page (int):  Default: 1.

    Returns:
        Response[Union[ActionslistJobsForWorkflowRunAttemptResponse200, Any]]
    """

    return (
        await asyncio_detailed(
            owner=owner,
            repo=repo,
            run_id=run_id,
            attempt_number=attempt_number,
            client=client,
            per_page=per_page,
            page=page,
        )
    ).parsed
