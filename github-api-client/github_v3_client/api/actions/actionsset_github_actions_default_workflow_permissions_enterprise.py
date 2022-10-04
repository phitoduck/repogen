from typing import Any, Dict

import httpx

from ...client import Client
from ...models.actions_set_default_workflow_permissions import ActionsSetDefaultWorkflowPermissions
from ...types import Response


def _get_kwargs(
    enterprise: str,
    *,
    client: Client,
    json_body: ActionsSetDefaultWorkflowPermissions,
) -> Dict[str, Any]:
    url = "{}/enterprises/{enterprise}/actions/permissions/workflow".format(client.base_url, enterprise=enterprise)

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
    enterprise: str,
    *,
    client: Client,
    json_body: ActionsSetDefaultWorkflowPermissions,
) -> Response[Any]:
    """Set default workflow permissions for an enterprise

     Sets the default workflow permissions granted to the `GITHUB_TOKEN` when running workflows in an
    enterprise, and sets
    whether GitHub Actions can submit approving pull request reviews. For more information, see
    \"[Enforcing a policy for workflow permissions in your
    enterprise](https://docs.github.com/enterprise-cloud@latest/admin/policies/enforcing-policies-for-
    your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise#enforcing-a-policy-for-
    workflow-permissions-in-your-enterprise).\"

    You must authenticate using an access token with the `admin:enterprise` scope to use this endpoint.
    GitHub Apps must have the `enterprise_administration:write` permission to use this endpoint.

    Args:
        enterprise (str):
        json_body (ActionsSetDefaultWorkflowPermissions):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        enterprise=enterprise,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    enterprise: str,
    *,
    client: Client,
    json_body: ActionsSetDefaultWorkflowPermissions,
) -> Response[Any]:
    """Set default workflow permissions for an enterprise

     Sets the default workflow permissions granted to the `GITHUB_TOKEN` when running workflows in an
    enterprise, and sets
    whether GitHub Actions can submit approving pull request reviews. For more information, see
    \"[Enforcing a policy for workflow permissions in your
    enterprise](https://docs.github.com/enterprise-cloud@latest/admin/policies/enforcing-policies-for-
    your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise#enforcing-a-policy-for-
    workflow-permissions-in-your-enterprise).\"

    You must authenticate using an access token with the `admin:enterprise` scope to use this endpoint.
    GitHub Apps must have the `enterprise_administration:write` permission to use this endpoint.

    Args:
        enterprise (str):
        json_body (ActionsSetDefaultWorkflowPermissions):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        enterprise=enterprise,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
