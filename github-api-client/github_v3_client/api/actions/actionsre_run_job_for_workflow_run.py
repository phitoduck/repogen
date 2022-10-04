from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.actionsre_run_job_for_workflow_run_json_body import ActionsreRunJobForWorkflowRunJsonBody
from ...models.empty_object import EmptyObject
from ...types import Response


def _get_kwargs(
    owner: str,
    repo: str,
    job_id: int,
    *,
    client: Client,
    json_body: Optional[ActionsreRunJobForWorkflowRunJsonBody],
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/actions/jobs/{job_id}/rerun".format(
        client.base_url, owner=owner, repo=repo, job_id=job_id
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, EmptyObject]]:
    if response.status_code == 201:
        response_201 = EmptyObject.from_dict(response.json())

        return response_201
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, EmptyObject]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    owner: str,
    repo: str,
    job_id: int,
    *,
    client: Client,
    json_body: Optional[ActionsreRunJobForWorkflowRunJsonBody],
) -> Response[Union[Any, EmptyObject]]:
    """Re-run a job from a workflow run

     Re-run a job and its dependent jobs in a workflow run. You must authenticate using an access token
    with the `repo` scope to use this endpoint. GitHub Apps must have the `actions:write` permission to
    use this endpoint.

    Args:
        owner (str):
        repo (str):
        job_id (int):
        json_body (Optional[ActionsreRunJobForWorkflowRunJsonBody]):

    Returns:
        Response[Union[Any, EmptyObject]]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        job_id=job_id,
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
    job_id: int,
    *,
    client: Client,
    json_body: Optional[ActionsreRunJobForWorkflowRunJsonBody],
) -> Optional[Union[Any, EmptyObject]]:
    """Re-run a job from a workflow run

     Re-run a job and its dependent jobs in a workflow run. You must authenticate using an access token
    with the `repo` scope to use this endpoint. GitHub Apps must have the `actions:write` permission to
    use this endpoint.

    Args:
        owner (str):
        repo (str):
        job_id (int):
        json_body (Optional[ActionsreRunJobForWorkflowRunJsonBody]):

    Returns:
        Response[Union[Any, EmptyObject]]
    """

    return sync_detailed(
        owner=owner,
        repo=repo,
        job_id=job_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    owner: str,
    repo: str,
    job_id: int,
    *,
    client: Client,
    json_body: Optional[ActionsreRunJobForWorkflowRunJsonBody],
) -> Response[Union[Any, EmptyObject]]:
    """Re-run a job from a workflow run

     Re-run a job and its dependent jobs in a workflow run. You must authenticate using an access token
    with the `repo` scope to use this endpoint. GitHub Apps must have the `actions:write` permission to
    use this endpoint.

    Args:
        owner (str):
        repo (str):
        job_id (int):
        json_body (Optional[ActionsreRunJobForWorkflowRunJsonBody]):

    Returns:
        Response[Union[Any, EmptyObject]]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        job_id=job_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    owner: str,
    repo: str,
    job_id: int,
    *,
    client: Client,
    json_body: Optional[ActionsreRunJobForWorkflowRunJsonBody],
) -> Optional[Union[Any, EmptyObject]]:
    """Re-run a job from a workflow run

     Re-run a job and its dependent jobs in a workflow run. You must authenticate using an access token
    with the `repo` scope to use this endpoint. GitHub Apps must have the `actions:write` permission to
    use this endpoint.

    Args:
        owner (str):
        repo (str):
        job_id (int):
        json_body (Optional[ActionsreRunJobForWorkflowRunJsonBody]):

    Returns:
        Response[Union[Any, EmptyObject]]
    """

    return (
        await asyncio_detailed(
            owner=owner,
            repo=repo,
            job_id=job_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
