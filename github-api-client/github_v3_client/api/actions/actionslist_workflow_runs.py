import datetime
from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...models.actionslist_workflow_runs_status import ActionslistWorkflowRunsStatus
from ...types import UNSET, Response


def _get_kwargs(
    owner: str,
    repo: str,
    workflow_id: Union[int, str],
    *,
    client: Client,
    actor: str,
    branch: str,
    event: str,
    status: ActionslistWorkflowRunsStatus,
    per_page: int = 30,
    page: int = 1,
    created: datetime.datetime,
    exclude_pull_requests: bool = False,
    check_suite_id: int,
    head_sha: str,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs".format(
        client.base_url, owner=owner, repo=repo, workflow_id=workflow_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["actor"] = actor

    params["branch"] = branch

    params["event"] = event

    json_status = status.value

    params["status"] = json_status

    params["per_page"] = per_page

    params["page"] = page

    json_created = created.isoformat()

    params["created"] = json_created

    params["exclude_pull_requests"] = exclude_pull_requests

    params["check_suite_id"] = check_suite_id

    params["head_sha"] = head_sha

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
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
    actor: str,
    branch: str,
    event: str,
    status: ActionslistWorkflowRunsStatus,
    per_page: int = 30,
    page: int = 1,
    created: datetime.datetime,
    exclude_pull_requests: bool = False,
    check_suite_id: int,
    head_sha: str,
) -> Response[Any]:
    """List workflow runs for a workflow

     List all workflow runs for a workflow. You can replace `workflow_id` with the workflow file name.
    For example, you could use `main.yaml`. You can use parameters to narrow the list of results. For
    more information about using parameters, see
    [Parameters](https://docs.github.com/rest/overview/resources-in-the-rest-api#parameters).

    Anyone with read access to the repository can use this endpoint. If the repository is private you
    must use an access token with the `repo` scope.

    Args:
        owner (str):
        repo (str):
        workflow_id (Union[int, str]):
        actor (str):
        branch (str):
        event (str):
        status (ActionslistWorkflowRunsStatus):
        per_page (int):  Default: 30.
        page (int):  Default: 1.
        created (datetime.datetime):
        exclude_pull_requests (bool):
        check_suite_id (int):
        head_sha (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        workflow_id=workflow_id,
        client=client,
        actor=actor,
        branch=branch,
        event=event,
        status=status,
        per_page=per_page,
        page=page,
        created=created,
        exclude_pull_requests=exclude_pull_requests,
        check_suite_id=check_suite_id,
        head_sha=head_sha,
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
    actor: str,
    branch: str,
    event: str,
    status: ActionslistWorkflowRunsStatus,
    per_page: int = 30,
    page: int = 1,
    created: datetime.datetime,
    exclude_pull_requests: bool = False,
    check_suite_id: int,
    head_sha: str,
) -> Response[Any]:
    """List workflow runs for a workflow

     List all workflow runs for a workflow. You can replace `workflow_id` with the workflow file name.
    For example, you could use `main.yaml`. You can use parameters to narrow the list of results. For
    more information about using parameters, see
    [Parameters](https://docs.github.com/rest/overview/resources-in-the-rest-api#parameters).

    Anyone with read access to the repository can use this endpoint. If the repository is private you
    must use an access token with the `repo` scope.

    Args:
        owner (str):
        repo (str):
        workflow_id (Union[int, str]):
        actor (str):
        branch (str):
        event (str):
        status (ActionslistWorkflowRunsStatus):
        per_page (int):  Default: 30.
        page (int):  Default: 1.
        created (datetime.datetime):
        exclude_pull_requests (bool):
        check_suite_id (int):
        head_sha (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        workflow_id=workflow_id,
        client=client,
        actor=actor,
        branch=branch,
        event=event,
        status=status,
        per_page=per_page,
        page=page,
        created=created,
        exclude_pull_requests=exclude_pull_requests,
        check_suite_id=check_suite_id,
        head_sha=head_sha,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
