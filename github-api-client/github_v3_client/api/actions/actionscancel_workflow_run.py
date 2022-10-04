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
    url = "{}/repos/{owner}/{repo}/actions/runs/{run_id}/cancel".format(
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
    if response.status_code == 202:
        response_202 = EmptyObject.from_dict(response.json())

        return response_202
    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409
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
    """Cancel a workflow run

     Cancels a workflow run using its `id`. You must authenticate using an access token with the `repo`
    scope to use this endpoint. GitHub Apps must have the `actions:write` permission to use this
    endpoint.

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
    """Cancel a workflow run

     Cancels a workflow run using its `id`. You must authenticate using an access token with the `repo`
    scope to use this endpoint. GitHub Apps must have the `actions:write` permission to use this
    endpoint.

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
    """Cancel a workflow run

     Cancels a workflow run using its `id`. You must authenticate using an access token with the `repo`
    scope to use this endpoint. GitHub Apps must have the `actions:write` permission to use this
    endpoint.

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
    """Cancel a workflow run

     Cancels a workflow run using its `id`. You must authenticate using an access token with the `repo`
    scope to use this endpoint. GitHub Apps must have the `actions:write` permission to use this
    endpoint.

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
