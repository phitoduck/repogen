from typing import Any, Dict

import httpx

from ...client import Client
from ...types import UNSET, Response


def _get_kwargs(
    owner: str,
    repo: str,
    run_id: int,
    attempt_number: int,
    *,
    client: Client,
    exclude_pull_requests: bool = False,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}".format(
        client.base_url, owner=owner, repo=repo, run_id=run_id, attempt_number=attempt_number
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["exclude_pull_requests"] = exclude_pull_requests

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
    run_id: int,
    attempt_number: int,
    *,
    client: Client,
    exclude_pull_requests: bool = False,
) -> Response[Any]:
    """Get a workflow run attempt

     Gets a specific workflow run attempt. Anyone with read access to the repository
    can use this endpoint. If the repository is private you must use an access token
    with the `repo` scope. GitHub Apps must have the `actions:read` permission to
    use this endpoint.

    Args:
        owner (str):
        repo (str):
        run_id (int):
        attempt_number (int):
        exclude_pull_requests (bool):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        run_id=run_id,
        attempt_number=attempt_number,
        client=client,
        exclude_pull_requests=exclude_pull_requests,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    owner: str,
    repo: str,
    run_id: int,
    attempt_number: int,
    *,
    client: Client,
    exclude_pull_requests: bool = False,
) -> Response[Any]:
    """Get a workflow run attempt

     Gets a specific workflow run attempt. Anyone with read access to the repository
    can use this endpoint. If the repository is private you must use an access token
    with the `repo` scope. GitHub Apps must have the `actions:read` permission to
    use this endpoint.

    Args:
        owner (str):
        repo (str):
        run_id (int):
        attempt_number (int):
        exclude_pull_requests (bool):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        run_id=run_id,
        attempt_number=attempt_number,
        client=client,
        exclude_pull_requests=exclude_pull_requests,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
