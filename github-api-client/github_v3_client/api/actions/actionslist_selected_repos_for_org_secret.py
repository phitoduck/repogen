from typing import Any, Dict

import httpx

from ...client import Client
from ...types import UNSET, Response


def _get_kwargs(
    org: str,
    secret_name: str,
    *,
    client: Client,
    page: int = 1,
    per_page: int = 30,
) -> Dict[str, Any]:
    url = "{}/orgs/{org}/actions/secrets/{secret_name}/repositories".format(
        client.base_url, org=org, secret_name=secret_name
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    org: str,
    secret_name: str,
    *,
    client: Client,
    page: int = 1,
    per_page: int = 30,
) -> Response[Any]:
    """List selected repositories for an organization secret

     Lists all repositories that have been selected when the `visibility` for repository access to a
    secret is set to `selected`. You must authenticate using an access token with the `admin:org` scope
    to use this endpoint. GitHub Apps must have the `secrets` organization permission to use this
    endpoint.

    Args:
        org (str):
        secret_name (str):
        page (int):  Default: 1.
        per_page (int):  Default: 30.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        org=org,
        secret_name=secret_name,
        client=client,
        page=page,
        per_page=per_page,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    org: str,
    secret_name: str,
    *,
    client: Client,
    page: int = 1,
    per_page: int = 30,
) -> Response[Any]:
    """List selected repositories for an organization secret

     Lists all repositories that have been selected when the `visibility` for repository access to a
    secret is set to `selected`. You must authenticate using an access token with the `admin:org` scope
    to use this endpoint. GitHub Apps must have the `secrets` organization permission to use this
    endpoint.

    Args:
        org (str):
        secret_name (str):
        page (int):  Default: 1.
        per_page (int):  Default: 30.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        org=org,
        secret_name=secret_name,
        client=client,
        page=page,
        per_page=per_page,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
