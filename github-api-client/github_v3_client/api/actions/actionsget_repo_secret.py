from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.actions_secret import ActionsSecret
from ...types import Response


def _get_kwargs(
    owner: str,
    repo: str,
    secret_name: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/actions/secrets/{secret_name}".format(
        client.base_url, owner=owner, repo=repo, secret_name=secret_name
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


def _parse_response(*, response: httpx.Response) -> Optional[ActionsSecret]:
    if response.status_code == 200:
        response_200 = ActionsSecret.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ActionsSecret]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    owner: str,
    repo: str,
    secret_name: str,
    *,
    client: Client,
) -> Response[ActionsSecret]:
    """Get a repository secret

     Gets a single repository secret without revealing its encrypted value. You must authenticate using
    an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `secrets`
    repository permission to use this endpoint.

    Args:
        owner (str):
        repo (str):
        secret_name (str):

    Returns:
        Response[ActionsSecret]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        secret_name=secret_name,
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
    secret_name: str,
    *,
    client: Client,
) -> Optional[ActionsSecret]:
    """Get a repository secret

     Gets a single repository secret without revealing its encrypted value. You must authenticate using
    an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `secrets`
    repository permission to use this endpoint.

    Args:
        owner (str):
        repo (str):
        secret_name (str):

    Returns:
        Response[ActionsSecret]
    """

    return sync_detailed(
        owner=owner,
        repo=repo,
        secret_name=secret_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    owner: str,
    repo: str,
    secret_name: str,
    *,
    client: Client,
) -> Response[ActionsSecret]:
    """Get a repository secret

     Gets a single repository secret without revealing its encrypted value. You must authenticate using
    an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `secrets`
    repository permission to use this endpoint.

    Args:
        owner (str):
        repo (str):
        secret_name (str):

    Returns:
        Response[ActionsSecret]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        secret_name=secret_name,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    owner: str,
    repo: str,
    secret_name: str,
    *,
    client: Client,
) -> Optional[ActionsSecret]:
    """Get a repository secret

     Gets a single repository secret without revealing its encrypted value. You must authenticate using
    an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `secrets`
    repository permission to use this endpoint.

    Args:
        owner (str):
        repo (str):
        secret_name (str):

    Returns:
        Response[ActionsSecret]
    """

    return (
        await asyncio_detailed(
            owner=owner,
            repo=repo,
            secret_name=secret_name,
            client=client,
        )
    ).parsed
