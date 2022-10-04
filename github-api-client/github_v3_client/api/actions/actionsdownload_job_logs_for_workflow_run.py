from typing import Any, Dict

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    owner: str,
    repo: str,
    job_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/actions/jobs/{job_id}/logs".format(
        client.base_url, owner=owner, repo=repo, job_id=job_id
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
    job_id: int,
    *,
    client: Client,
) -> Response[Any]:
    """Download job logs for a workflow run

     Gets a redirect URL to download a plain text file of logs for a workflow job. This link expires
    after 1 minute. Look
    for `Location:` in the response header to find the URL for the download. Anyone with read access to
    the repository can
    use this endpoint. If the repository is private you must use an access token with the `repo` scope.
    GitHub Apps must
    have the `actions:read` permission to use this endpoint.

    Args:
        owner (str):
        repo (str):
        job_id (int):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        job_id=job_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    owner: str,
    repo: str,
    job_id: int,
    *,
    client: Client,
) -> Response[Any]:
    """Download job logs for a workflow run

     Gets a redirect URL to download a plain text file of logs for a workflow job. This link expires
    after 1 minute. Look
    for `Location:` in the response header to find the URL for the download. Anyone with read access to
    the repository can
    use this endpoint. If the repository is private you must use an access token with the `repo` scope.
    GitHub Apps must
    have the `actions:read` permission to use this endpoint.

    Args:
        owner (str):
        repo (str):
        job_id (int):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        job_id=job_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
