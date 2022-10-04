from typing import Any, Dict

import httpx

from ...client import Client
from ...models.actions_set_default_workflow_permissions import ActionsSetDefaultWorkflowPermissions
from ...types import Response


def _get_kwargs(
    org: str,
    *,
    client: Client,
    json_body: ActionsSetDefaultWorkflowPermissions,
) -> Dict[str, Any]:
    url = "{}/orgs/{org}/actions/permissions/workflow".format(client.base_url, org=org)

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
    *,
    client: Client,
    json_body: ActionsSetDefaultWorkflowPermissions,
) -> Response[Any]:
    """Set default workflow permissions for an organization

     Sets the default workflow permissions granted to the `GITHUB_TOKEN` when running workflows in an
    organization, and sets if GitHub Actions
    can submit approving pull request reviews. For more information, see
    \"[Setting the permissions of the GITHUB_TOKEN for your
    organization](https://docs.github.com/organizations/managing-organization-settings/disabling-or-
    limiting-github-actions-for-your-organization#setting-the-permissions-of-the-github_token-for-your-
    organization).\"

    You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub
    Apps must have the `administration` organization permission to use this API.

    Args:
        org (str):
        json_body (ActionsSetDefaultWorkflowPermissions):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        org=org,
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
    *,
    client: Client,
    json_body: ActionsSetDefaultWorkflowPermissions,
) -> Response[Any]:
    """Set default workflow permissions for an organization

     Sets the default workflow permissions granted to the `GITHUB_TOKEN` when running workflows in an
    organization, and sets if GitHub Actions
    can submit approving pull request reviews. For more information, see
    \"[Setting the permissions of the GITHUB_TOKEN for your
    organization](https://docs.github.com/organizations/managing-organization-settings/disabling-or-
    limiting-github-actions-for-your-organization#setting-the-permissions-of-the-github_token-for-your-
    organization).\"

    You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub
    Apps must have the `administration` organization permission to use this API.

    Args:
        org (str):
        json_body (ActionsSetDefaultWorkflowPermissions):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        org=org,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
