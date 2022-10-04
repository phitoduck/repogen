from typing import Any, Dict

import httpx

from ...client import Client
from ...models.actionsset_selected_repos_for_org_secret_json_body import ActionssetSelectedReposForOrgSecretJsonBody
from ...types import Response


def _get_kwargs(
    org: str,
    secret_name: str,
    *,
    client: Client,
    json_body: ActionssetSelectedReposForOrgSecretJsonBody,
) -> Dict[str, Any]:
    url = "{}/orgs/{org}/actions/secrets/{secret_name}/repositories".format(
        client.base_url, org=org, secret_name=secret_name
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
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
    json_body: ActionssetSelectedReposForOrgSecretJsonBody,
) -> Response[Any]:
    """Set selected repositories for an organization secret

     Replaces all repositories for an organization secret when the `visibility` for repository access is
    set to `selected`. The visibility is set when you [Create or update an organization
    secret](https://docs.github.com/rest/reference/actions#create-or-update-an-organization-secret). You
    must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps
    must have the `secrets` organization permission to use this endpoint.

    Args:
        org (str):
        secret_name (str):
        json_body (ActionssetSelectedReposForOrgSecretJsonBody):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        org=org,
        secret_name=secret_name,
        client=client,
        json_body=json_body,
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
    json_body: ActionssetSelectedReposForOrgSecretJsonBody,
) -> Response[Any]:
    """Set selected repositories for an organization secret

     Replaces all repositories for an organization secret when the `visibility` for repository access is
    set to `selected`. The visibility is set when you [Create or update an organization
    secret](https://docs.github.com/rest/reference/actions#create-or-update-an-organization-secret). You
    must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps
    must have the `secrets` organization permission to use this endpoint.

    Args:
        org (str):
        secret_name (str):
        json_body (ActionssetSelectedReposForOrgSecretJsonBody):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        org=org,
        secret_name=secret_name,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
