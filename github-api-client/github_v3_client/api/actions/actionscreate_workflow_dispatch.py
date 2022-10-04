from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...models.actionscreate_workflow_dispatch_json_body import ActionscreateWorkflowDispatchJsonBody
from ...types import Response


def _get_kwargs(
    owner: str,
    repo: str,
    workflow_id: Union[int, str],
    *,
    client: Client,
    json_body: ActionscreateWorkflowDispatchJsonBody,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches".format(
        client.base_url, owner=owner, repo=repo, workflow_id=workflow_id
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
    workflow_id: Union[int, str],
    *,
    client: Client,
    json_body: ActionscreateWorkflowDispatchJsonBody,
) -> Response[Any]:
    """Create a workflow dispatch event

     You can use this endpoint to manually trigger a GitHub Actions workflow run. You can replace
    `workflow_id` with the workflow file name. For example, you could use `main.yaml`.

    You must configure your GitHub Actions workflow to run when the [`workflow_dispatch`
    webhook](/developers/webhooks-and-events/webhook-events-and-payloads#workflow_dispatch) event
    occurs. The `inputs` are configured in the workflow file. For more information about how to
    configure the `workflow_dispatch` event in the workflow file, see \"[Events that trigger
    workflows](/actions/reference/events-that-trigger-workflows#workflow_dispatch).\"

    You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps
    must have the `actions:write` permission to use this endpoint. For more information, see \"[Creating
    a personal access token for the command line](https://docs.github.com/articles/creating-a-personal-
    access-token-for-the-command-line).\"

    Args:
        owner (str):
        repo (str):
        workflow_id (Union[int, str]):
        json_body (ActionscreateWorkflowDispatchJsonBody):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        workflow_id=workflow_id,
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
    workflow_id: Union[int, str],
    *,
    client: Client,
    json_body: ActionscreateWorkflowDispatchJsonBody,
) -> Response[Any]:
    """Create a workflow dispatch event

     You can use this endpoint to manually trigger a GitHub Actions workflow run. You can replace
    `workflow_id` with the workflow file name. For example, you could use `main.yaml`.

    You must configure your GitHub Actions workflow to run when the [`workflow_dispatch`
    webhook](/developers/webhooks-and-events/webhook-events-and-payloads#workflow_dispatch) event
    occurs. The `inputs` are configured in the workflow file. For more information about how to
    configure the `workflow_dispatch` event in the workflow file, see \"[Events that trigger
    workflows](/actions/reference/events-that-trigger-workflows#workflow_dispatch).\"

    You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps
    must have the `actions:write` permission to use this endpoint. For more information, see \"[Creating
    a personal access token for the command line](https://docs.github.com/articles/creating-a-personal-
    access-token-for-the-command-line).\"

    Args:
        owner (str):
        repo (str):
        workflow_id (Union[int, str]):
        json_body (ActionscreateWorkflowDispatchJsonBody):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        workflow_id=workflow_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
