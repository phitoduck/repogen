from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.workflow_usage import WorkflowUsage
from ...types import Response


def _get_kwargs(
    owner: str,
    repo: str,
    workflow_id: Union[int, str],
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/actions/workflows/{workflow_id}/timing".format(
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


def _parse_response(*, response: httpx.Response) -> Optional[WorkflowUsage]:
    if response.status_code == 200:
        response_200 = WorkflowUsage.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[WorkflowUsage]:
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
) -> Response[WorkflowUsage]:
    """Get workflow usage

     Gets the number of billable minutes used by a specific workflow during the current billing cycle.
    Billable minutes only apply to workflows in private repositories that use GitHub-hosted runners.
    Usage is listed for each GitHub-hosted runner operating system in milliseconds. Any job re-runs are
    also included in the usage. The usage does not include the multiplier for macOS and Windows runners
    and is not rounded up to the nearest whole minute. For more information, see \"[Managing billing for
    GitHub Actions](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-
    github/managing-billing-for-github-actions)\".

    You can replace `workflow_id` with the workflow file name. For example, you could use `main.yaml`.
    Anyone with read access to the repository can use this endpoint. If the repository is private you
    must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission
    to use this endpoint.

    Args:
        owner (str):
        repo (str):
        workflow_id (Union[int, str]):

    Returns:
        Response[WorkflowUsage]
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
) -> Optional[WorkflowUsage]:
    """Get workflow usage

     Gets the number of billable minutes used by a specific workflow during the current billing cycle.
    Billable minutes only apply to workflows in private repositories that use GitHub-hosted runners.
    Usage is listed for each GitHub-hosted runner operating system in milliseconds. Any job re-runs are
    also included in the usage. The usage does not include the multiplier for macOS and Windows runners
    and is not rounded up to the nearest whole minute. For more information, see \"[Managing billing for
    GitHub Actions](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-
    github/managing-billing-for-github-actions)\".

    You can replace `workflow_id` with the workflow file name. For example, you could use `main.yaml`.
    Anyone with read access to the repository can use this endpoint. If the repository is private you
    must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission
    to use this endpoint.

    Args:
        owner (str):
        repo (str):
        workflow_id (Union[int, str]):

    Returns:
        Response[WorkflowUsage]
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
) -> Response[WorkflowUsage]:
    """Get workflow usage

     Gets the number of billable minutes used by a specific workflow during the current billing cycle.
    Billable minutes only apply to workflows in private repositories that use GitHub-hosted runners.
    Usage is listed for each GitHub-hosted runner operating system in milliseconds. Any job re-runs are
    also included in the usage. The usage does not include the multiplier for macOS and Windows runners
    and is not rounded up to the nearest whole minute. For more information, see \"[Managing billing for
    GitHub Actions](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-
    github/managing-billing-for-github-actions)\".

    You can replace `workflow_id` with the workflow file name. For example, you could use `main.yaml`.
    Anyone with read access to the repository can use this endpoint. If the repository is private you
    must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission
    to use this endpoint.

    Args:
        owner (str):
        repo (str):
        workflow_id (Union[int, str]):

    Returns:
        Response[WorkflowUsage]
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
) -> Optional[WorkflowUsage]:
    """Get workflow usage

     Gets the number of billable minutes used by a specific workflow during the current billing cycle.
    Billable minutes only apply to workflows in private repositories that use GitHub-hosted runners.
    Usage is listed for each GitHub-hosted runner operating system in milliseconds. Any job re-runs are
    also included in the usage. The usage does not include the multiplier for macOS and Windows runners
    and is not rounded up to the nearest whole minute. For more information, see \"[Managing billing for
    GitHub Actions](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-
    github/managing-billing-for-github-actions)\".

    You can replace `workflow_id` with the workflow file name. For example, you could use `main.yaml`.
    Anyone with read access to the repository can use this endpoint. If the repository is private you
    must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission
    to use this endpoint.

    Args:
        owner (str):
        repo (str):
        workflow_id (Union[int, str]):

    Returns:
        Response[WorkflowUsage]
    """

    return (
        await asyncio_detailed(
            owner=owner,
            repo=repo,
            workflow_id=workflow_id,
            client=client,
        )
    ).parsed
