from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.actions_public_key import ActionsPublicKey
from ...types import Response


def _get_kwargs(
    owner: str,
    repo: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/actions/secrets/public-key".format(client.base_url, owner=owner, repo=repo)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[ActionsPublicKey]:
    if response.status_code == 200:
        response_200 = ActionsPublicKey.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ActionsPublicKey]:
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
) -> Response[ActionsPublicKey]:
    """Get a repository public key

     Gets your public key, which you need to encrypt secrets. You need to encrypt a secret before you can
    create or update secrets. Anyone with read access to the repository can use this endpoint. If the
    repository is private you must use an access token with the `repo` scope. GitHub Apps must have the
    `secrets` repository permission to use this endpoint.

    Args:
        owner (str):
        repo (str):

    Returns:
        Response[ActionsPublicKey]
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
) -> Optional[ActionsPublicKey]:
    """Get a repository public key

     Gets your public key, which you need to encrypt secrets. You need to encrypt a secret before you can
    create or update secrets. Anyone with read access to the repository can use this endpoint. If the
    repository is private you must use an access token with the `repo` scope. GitHub Apps must have the
    `secrets` repository permission to use this endpoint.

    Args:
        owner (str):
        repo (str):

    Returns:
        Response[ActionsPublicKey]
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
) -> Response[ActionsPublicKey]:
    """Get a repository public key

     Gets your public key, which you need to encrypt secrets. You need to encrypt a secret before you can
    create or update secrets. Anyone with read access to the repository can use this endpoint. If the
    repository is private you must use an access token with the `repo` scope. GitHub Apps must have the
    `secrets` repository permission to use this endpoint.

    Args:
        owner (str):
        repo (str):

    Returns:
        Response[ActionsPublicKey]
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
) -> Optional[ActionsPublicKey]:
    """Get a repository public key

     Gets your public key, which you need to encrypt secrets. You need to encrypt a secret before you can
    create or update secrets. Anyone with read access to the repository can use this endpoint. If the
    repository is private you must use an access token with the `repo` scope. GitHub Apps must have the
    `secrets` repository permission to use this endpoint.

    Args:
        owner (str):
        repo (str):

    Returns:
        Response[ActionsPublicKey]
    """

    return (
        await asyncio_detailed(
            owner=owner,
            repo=repo,
            client=client,
        )
    ).parsed
