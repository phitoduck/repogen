from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.artifact import Artifact
from ...types import Response


def _get_kwargs(
    owner: str,
    repo: str,
    artifact_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/actions/artifacts/{artifact_id}".format(
        client.base_url, owner=owner, repo=repo, artifact_id=artifact_id
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


def _parse_response(*, response: httpx.Response) -> Optional[Artifact]:
    if response.status_code == 200:
        response_200 = Artifact.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Artifact]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    owner: str,
    repo: str,
    artifact_id: int,
    *,
    client: Client,
) -> Response[Artifact]:
    """Get an artifact

     Gets a specific artifact for a workflow run. Anyone with read access to the repository can use this
    endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub
    Apps must have the `actions:read` permission to use this endpoint.

    Args:
        owner (str):
        repo (str):
        artifact_id (int):

    Returns:
        Response[Artifact]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        artifact_id=artifact_id,
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
    artifact_id: int,
    *,
    client: Client,
) -> Optional[Artifact]:
    """Get an artifact

     Gets a specific artifact for a workflow run. Anyone with read access to the repository can use this
    endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub
    Apps must have the `actions:read` permission to use this endpoint.

    Args:
        owner (str):
        repo (str):
        artifact_id (int):

    Returns:
        Response[Artifact]
    """

    return sync_detailed(
        owner=owner,
        repo=repo,
        artifact_id=artifact_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    owner: str,
    repo: str,
    artifact_id: int,
    *,
    client: Client,
) -> Response[Artifact]:
    """Get an artifact

     Gets a specific artifact for a workflow run. Anyone with read access to the repository can use this
    endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub
    Apps must have the `actions:read` permission to use this endpoint.

    Args:
        owner (str):
        repo (str):
        artifact_id (int):

    Returns:
        Response[Artifact]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        artifact_id=artifact_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    owner: str,
    repo: str,
    artifact_id: int,
    *,
    client: Client,
) -> Optional[Artifact]:
    """Get an artifact

     Gets a specific artifact for a workflow run. Anyone with read access to the repository can use this
    endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub
    Apps must have the `actions:read` permission to use this endpoint.

    Args:
        owner (str):
        repo (str):
        artifact_id (int):

    Returns:
        Response[Artifact]
    """

    return (
        await asyncio_detailed(
            owner=owner,
            repo=repo,
            artifact_id=artifact_id,
            client=client,
        )
    ).parsed
