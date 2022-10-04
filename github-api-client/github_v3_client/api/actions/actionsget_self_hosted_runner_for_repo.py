from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.self_hosted_runners import SelfHostedRunners
from ...types import Response


def _get_kwargs(
    owner: str,
    repo: str,
    runner_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/actions/runners/{runner_id}".format(
        client.base_url, owner=owner, repo=repo, runner_id=runner_id
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


def _parse_response(*, response: httpx.Response) -> Optional[SelfHostedRunners]:
    if response.status_code == 200:
        response_200 = SelfHostedRunners.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[SelfHostedRunners]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    owner: str,
    repo: str,
    runner_id: int,
    *,
    client: Client,
) -> Response[SelfHostedRunners]:
    """Get a self-hosted runner for a repository

     Gets a specific self-hosted runner configured in a repository.

    You must authenticate using an access token with the `repo` scope to use this
    endpoint.

    Args:
        owner (str):
        repo (str):
        runner_id (int):

    Returns:
        Response[SelfHostedRunners]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        runner_id=runner_id,
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
    runner_id: int,
    *,
    client: Client,
) -> Optional[SelfHostedRunners]:
    """Get a self-hosted runner for a repository

     Gets a specific self-hosted runner configured in a repository.

    You must authenticate using an access token with the `repo` scope to use this
    endpoint.

    Args:
        owner (str):
        repo (str):
        runner_id (int):

    Returns:
        Response[SelfHostedRunners]
    """

    return sync_detailed(
        owner=owner,
        repo=repo,
        runner_id=runner_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    owner: str,
    repo: str,
    runner_id: int,
    *,
    client: Client,
) -> Response[SelfHostedRunners]:
    """Get a self-hosted runner for a repository

     Gets a specific self-hosted runner configured in a repository.

    You must authenticate using an access token with the `repo` scope to use this
    endpoint.

    Args:
        owner (str):
        repo (str):
        runner_id (int):

    Returns:
        Response[SelfHostedRunners]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        runner_id=runner_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    owner: str,
    repo: str,
    runner_id: int,
    *,
    client: Client,
) -> Optional[SelfHostedRunners]:
    """Get a self-hosted runner for a repository

     Gets a specific self-hosted runner configured in a repository.

    You must authenticate using an access token with the `repo` scope to use this
    endpoint.

    Args:
        owner (str):
        repo (str):
        runner_id (int):

    Returns:
        Response[SelfHostedRunners]
    """

    return (
        await asyncio_detailed(
            owner=owner,
            repo=repo,
            runner_id=runner_id,
            client=client,
        )
    ).parsed
