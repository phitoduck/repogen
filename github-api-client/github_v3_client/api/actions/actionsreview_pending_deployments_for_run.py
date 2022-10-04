from typing import Any, Dict

import httpx

from ...client import Client
from ...models.actionsreview_pending_deployments_for_run_json_body import ActionsreviewPendingDeploymentsForRunJsonBody
from ...types import Response


def _get_kwargs(
    owner: str,
    repo: str,
    run_id: int,
    *,
    client: Client,
    json_body: ActionsreviewPendingDeploymentsForRunJsonBody,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/actions/runs/{run_id}/pending_deployments".format(
        client.base_url, owner=owner, repo=repo, run_id=run_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
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
    run_id: int,
    *,
    client: Client,
    json_body: ActionsreviewPendingDeploymentsForRunJsonBody,
) -> Response[Any]:
    """Review pending deployments for a workflow run

     Approve or reject pending deployments that are waiting on approval by a required reviewer.

    Required reviewers with read access to the repository contents and deployments can use this
    endpoint. Required reviewers must authenticate using an access token with the `repo` scope to use
    this endpoint.

    Args:
        owner (str):
        repo (str):
        run_id (int):
        json_body (ActionsreviewPendingDeploymentsForRunJsonBody):

    Returns:
        Response[Any]
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


async def asyncio_detailed(
    owner: str,
    repo: str,
    run_id: int,
    *,
    client: Client,
    json_body: ActionsreviewPendingDeploymentsForRunJsonBody,
) -> Response[Any]:
    """Review pending deployments for a workflow run

     Approve or reject pending deployments that are waiting on approval by a required reviewer.

    Required reviewers with read access to the repository contents and deployments can use this
    endpoint. Required reviewers must authenticate using an access token with the `repo` scope to use
    this endpoint.

    Args:
        owner (str):
        repo (str):
        run_id (int):
        json_body (ActionsreviewPendingDeploymentsForRunJsonBody):

    Returns:
        Response[Any]
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
