from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.actions_secret_for_an_organization import ActionsSecretForAnOrganization
from ...types import Response


def _get_kwargs(
    org: str,
    secret_name: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/orgs/{org}/actions/secrets/{secret_name}".format(client.base_url, org=org, secret_name=secret_name)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[ActionsSecretForAnOrganization]:
    if response.status_code == 200:
        response_200 = ActionsSecretForAnOrganization.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ActionsSecretForAnOrganization]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    org: str,
    secret_name: str,
    *,
    client: Client,
) -> Response[ActionsSecretForAnOrganization]:
    """Get an organization secret

     Gets a single organization secret without revealing its encrypted value. You must authenticate using
    an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `secrets`
    organization permission to use this endpoint.

    Args:
        org (str):
        secret_name (str):

    Returns:
        Response[ActionsSecretForAnOrganization]
    """

    kwargs = _get_kwargs(
        org=org,
        secret_name=secret_name,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    org: str,
    secret_name: str,
    *,
    client: Client,
) -> Optional[ActionsSecretForAnOrganization]:
    """Get an organization secret

     Gets a single organization secret without revealing its encrypted value. You must authenticate using
    an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `secrets`
    organization permission to use this endpoint.

    Args:
        org (str):
        secret_name (str):

    Returns:
        Response[ActionsSecretForAnOrganization]
    """

    return sync_detailed(
        org=org,
        secret_name=secret_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    org: str,
    secret_name: str,
    *,
    client: Client,
) -> Response[ActionsSecretForAnOrganization]:
    """Get an organization secret

     Gets a single organization secret without revealing its encrypted value. You must authenticate using
    an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `secrets`
    organization permission to use this endpoint.

    Args:
        org (str):
        secret_name (str):

    Returns:
        Response[ActionsSecretForAnOrganization]
    """

    kwargs = _get_kwargs(
        org=org,
        secret_name=secret_name,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    org: str,
    secret_name: str,
    *,
    client: Client,
) -> Optional[ActionsSecretForAnOrganization]:
    """Get an organization secret

     Gets a single organization secret without revealing its encrypted value. You must authenticate using
    an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `secrets`
    organization permission to use this endpoint.

    Args:
        org (str):
        secret_name (str):

    Returns:
        Response[ActionsSecretForAnOrganization]
    """

    return (
        await asyncio_detailed(
            org=org,
            secret_name=secret_name,
            client=client,
        )
    ).parsed
