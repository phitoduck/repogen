from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.actions_secret import ActionsSecret
from ...types import Response


def _get_kwargs(
    repository_id: int,
    environment_name: str,
    secret_name: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/repositories/{repository_id}/environments/{environment_name}/secrets/{secret_name}".format(
        client.base_url, repository_id=repository_id, environment_name=environment_name, secret_name=secret_name
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
    repository_id: int,
    environment_name: str,
    secret_name: str,
    *,
    client: Client,
) -> Response[ActionsSecret]:
    """Get an environment secret

     Gets a single environment secret without revealing its encrypted value. You must authenticate using
    an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `secrets`
    repository permission to use this endpoint.

    Args:
        repository_id (int):
        environment_name (str):
        secret_name (str):

    Returns:
        Response[ActionsSecret]
    """

    kwargs = _get_kwargs(
        repository_id=repository_id,
        environment_name=environment_name,
        secret_name=secret_name,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    repository_id: int,
    environment_name: str,
    secret_name: str,
    *,
    client: Client,
) -> Optional[ActionsSecret]:
    """Get an environment secret

     Gets a single environment secret without revealing its encrypted value. You must authenticate using
    an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `secrets`
    repository permission to use this endpoint.

    Args:
        repository_id (int):
        environment_name (str):
        secret_name (str):

    Returns:
        Response[ActionsSecret]
    """

    return sync_detailed(
        repository_id=repository_id,
        environment_name=environment_name,
        secret_name=secret_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    repository_id: int,
    environment_name: str,
    secret_name: str,
    *,
    client: Client,
) -> Response[ActionsSecret]:
    """Get an environment secret

     Gets a single environment secret without revealing its encrypted value. You must authenticate using
    an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `secrets`
    repository permission to use this endpoint.

    Args:
        repository_id (int):
        environment_name (str):
        secret_name (str):

    Returns:
        Response[ActionsSecret]
    """

    kwargs = _get_kwargs(
        repository_id=repository_id,
        environment_name=environment_name,
        secret_name=secret_name,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    repository_id: int,
    environment_name: str,
    secret_name: str,
    *,
    client: Client,
) -> Optional[ActionsSecret]:
    """Get an environment secret

     Gets a single environment secret without revealing its encrypted value. You must authenticate using
    an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `secrets`
    repository permission to use this endpoint.

    Args:
        repository_id (int):
        environment_name (str):
        secret_name (str):

    Returns:
        Response[ActionsSecret]
    """

    return (
        await asyncio_detailed(
            repository_id=repository_id,
            environment_name=environment_name,
            secret_name=secret_name,
            client=client,
        )
    ).parsed
