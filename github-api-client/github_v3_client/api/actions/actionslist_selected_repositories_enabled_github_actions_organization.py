from typing import Any, Dict

import httpx

from ...client import Client
from ...types import UNSET, Response


def _get_kwargs(
    org: str,
    *,
    client: Client,
    per_page: int = 30,
    page: int = 1,
) -> Dict[str, Any]:
    url = "{}/orgs/{org}/actions/permissions/repositories".format(client.base_url, org=org)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["per_page"] = per_page

    params["page"] = page

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
    *,
    client: Client,
    per_page: int = 30,
    page: int = 1,
) -> Response[Any]:
    """List selected repositories enabled for GitHub Actions in an organization

     Lists the selected repositories that are enabled for GitHub Actions in an organization. To use this
    endpoint, the organization permission policy for `enabled_repositories` must be configured to
    `selected`. For more information, see \"[Set GitHub Actions permissions for an organization](#set-
    github-actions-permissions-for-an-organization).\"

    You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub
    Apps must have the `administration` organization permission to use this API.

    Args:
        org (str):
        per_page (int):  Default: 30.
        page (int):  Default: 1.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        org=org,
        client=client,
        per_page=per_page,
        page=page,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    org: str,
    *,
    client: Client,
    per_page: int = 30,
    page: int = 1,
) -> Response[Any]:
    """List selected repositories enabled for GitHub Actions in an organization

     Lists the selected repositories that are enabled for GitHub Actions in an organization. To use this
    endpoint, the organization permission policy for `enabled_repositories` must be configured to
    `selected`. For more information, see \"[Set GitHub Actions permissions for an organization](#set-
    github-actions-permissions-for-an-organization).\"

    You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub
    Apps must have the `administration` organization permission to use this API.

    Args:
        org (str):
        per_page (int):  Default: 30.
        page (int):  Default: 1.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        org=org,
        client=client,
        per_page=per_page,
        page=page,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
