from typing import Any, Dict, List, Optional

import httpx

from ...client import Client
from ...models.runner_application import RunnerApplication
from ...types import Response


def _get_kwargs(
    owner: str,
    repo: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/actions/runners/downloads".format(client.base_url, owner=owner, repo=repo)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[RunnerApplication]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RunnerApplication.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[RunnerApplication]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    owner: str,
    repo: str,
    *,
    client: Client,
) -> Response[List[RunnerApplication]]:
    """List runner applications for a repository

     Lists binaries for the runner application that you can download and run.

    You must authenticate using an access token with the `repo` scope to use this endpoint.

    Args:
        owner (str):
        repo (str):

    Returns:
        Response[List[RunnerApplication]]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
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
    *,
    client: Client,
) -> Optional[List[RunnerApplication]]:
    """List runner applications for a repository

     Lists binaries for the runner application that you can download and run.

    You must authenticate using an access token with the `repo` scope to use this endpoint.

    Args:
        owner (str):
        repo (str):

    Returns:
        Response[List[RunnerApplication]]
    """

    return sync_detailed(
        owner=owner,
        repo=repo,
        client=client,
    ).parsed


async def asyncio_detailed(
    owner: str,
    repo: str,
    *,
    client: Client,
) -> Response[List[RunnerApplication]]:
    """List runner applications for a repository

     Lists binaries for the runner application that you can download and run.

    You must authenticate using an access token with the `repo` scope to use this endpoint.

    Args:
        owner (str):
        repo (str):

    Returns:
        Response[List[RunnerApplication]]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    owner: str,
    repo: str,
    *,
    client: Client,
) -> Optional[List[RunnerApplication]]:
    """List runner applications for a repository

     Lists binaries for the runner application that you can download and run.

    You must authenticate using an access token with the `repo` scope to use this endpoint.

    Args:
        owner (str):
        repo (str):

    Returns:
        Response[List[RunnerApplication]]
    """

    return (
        await asyncio_detailed(
            owner=owner,
            repo=repo,
            client=client,
        )
    ).parsed
