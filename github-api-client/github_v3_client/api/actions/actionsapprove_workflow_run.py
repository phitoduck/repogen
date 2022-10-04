from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.empty_object import EmptyObject
from ...types import Response


def _get_kwargs(
    owner: str,
    repo: str,
    run_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/actions/runs/{run_id}/approve".format(
        client.base_url, owner=owner, repo=repo, run_id=run_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, EmptyObject]]:
    if response.status_code == 201:
        response_201 = EmptyObject.from_dict(response.json())

        return response_201
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
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
    run_id: int,
    *,
    client: Client,
) -> Response[Union[Any, EmptyObject]]:
    """Approve a workflow run for a fork pull request

     Approves a workflow run for a pull request from a public fork of a first time contributor. For more
    information, see [\"Approving workflow runs from public
    forks](https://docs.github.com/actions/managing-workflow-runs/approving-workflow-runs-from-public-
    forks).\"

    You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps
    must have the `actions:write` permission to use this endpoint.

    Args:
        owner (str):
        repo (str):
        run_id (int):

    Returns:
        Response[Union[Any, EmptyObject]]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        run_id=run_id,
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
    run_id: int,
    *,
    client: Client,
) -> Optional[Union[Any, EmptyObject]]:
    """Approve a workflow run for a fork pull request

     Approves a workflow run for a pull request from a public fork of a first time contributor. For more
    information, see [\"Approving workflow runs from public
    forks](https://docs.github.com/actions/managing-workflow-runs/approving-workflow-runs-from-public-
    forks).\"

    You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps
    must have the `actions:write` permission to use this endpoint.

    Args:
        owner (str):
        repo (str):
        run_id (int):

    Returns:
        Response[Union[Any, EmptyObject]]
    """

    return sync_detailed(
        owner=owner,
        repo=repo,
        run_id=run_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    owner: str,
    repo: str,
    run_id: int,
    *,
    client: Client,
) -> Response[Union[Any, EmptyObject]]:
    """Approve a workflow run for a fork pull request

     Approves a workflow run for a pull request from a public fork of a first time contributor. For more
    information, see [\"Approving workflow runs from public
    forks](https://docs.github.com/actions/managing-workflow-runs/approving-workflow-runs-from-public-
    forks).\"

    You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps
    must have the `actions:write` permission to use this endpoint.

    Args:
        owner (str):
        repo (str):
        run_id (int):

    Returns:
        Response[Union[Any, EmptyObject]]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        run_id=run_id,
        client=client,
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
) -> Optional[Union[Any, EmptyObject]]:
    """Approve a workflow run for a fork pull request

     Approves a workflow run for a pull request from a public fork of a first time contributor. For more
    information, see [\"Approving workflow runs from public
    forks](https://docs.github.com/actions/managing-workflow-runs/approving-workflow-runs-from-public-
    forks).\"

    You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps
    must have the `actions:write` permission to use this endpoint.

    Args:
        owner (str):
        repo (str):
        run_id (int):

    Returns:
        Response[Union[Any, EmptyObject]]
    """

    return (
        await asyncio_detailed(
            owner=owner,
            repo=repo,
            run_id=run_id,
            client=client,
        )
    ).parsed
