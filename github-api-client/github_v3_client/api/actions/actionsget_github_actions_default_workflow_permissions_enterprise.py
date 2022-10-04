from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.actions_get_default_workflow_permissions import ActionsGetDefaultWorkflowPermissions
from ...types import Response


def _get_kwargs(
    enterprise: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/enterprises/{enterprise}/actions/permissions/workflow".format(client.base_url, enterprise=enterprise)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[ActionsGetDefaultWorkflowPermissions]:
    if response.status_code == 200:
        response_200 = ActionsGetDefaultWorkflowPermissions.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ActionsGetDefaultWorkflowPermissions]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    enterprise: str,
    *,
    client: Client,
) -> Response[ActionsGetDefaultWorkflowPermissions]:
    """Get default workflow permissions for an enterprise

     Gets the default workflow permissions granted to the `GITHUB_TOKEN` when running workflows in an
    enterprise,
    as well as whether GitHub Actions can submit approving pull request reviews. For more information,
    see
    \"[Enforcing a policy for workflow permissions in your
    enterprise](https://docs.github.com/enterprise-cloud@latest/admin/policies/enforcing-policies-for-
    your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise#enforcing-a-policy-for-
    workflow-permissions-in-your-enterprise).\"

    You must authenticate using an access token with the `admin:enterprise` scope to use this endpoint.
    GitHub Apps must have the `enterprise_administration:write` permission to use this endpoint.

    Args:
        enterprise (str):

    Returns:
        Response[ActionsGetDefaultWorkflowPermissions]
    """

    kwargs = _get_kwargs(
        enterprise=enterprise,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    enterprise: str,
    *,
    client: Client,
) -> Optional[ActionsGetDefaultWorkflowPermissions]:
    """Get default workflow permissions for an enterprise

     Gets the default workflow permissions granted to the `GITHUB_TOKEN` when running workflows in an
    enterprise,
    as well as whether GitHub Actions can submit approving pull request reviews. For more information,
    see
    \"[Enforcing a policy for workflow permissions in your
    enterprise](https://docs.github.com/enterprise-cloud@latest/admin/policies/enforcing-policies-for-
    your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise#enforcing-a-policy-for-
    workflow-permissions-in-your-enterprise).\"

    You must authenticate using an access token with the `admin:enterprise` scope to use this endpoint.
    GitHub Apps must have the `enterprise_administration:write` permission to use this endpoint.

    Args:
        enterprise (str):

    Returns:
        Response[ActionsGetDefaultWorkflowPermissions]
    """

    return sync_detailed(
        enterprise=enterprise,
        client=client,
    ).parsed


async def asyncio_detailed(
    enterprise: str,
    *,
    client: Client,
) -> Response[ActionsGetDefaultWorkflowPermissions]:
    """Get default workflow permissions for an enterprise

     Gets the default workflow permissions granted to the `GITHUB_TOKEN` when running workflows in an
    enterprise,
    as well as whether GitHub Actions can submit approving pull request reviews. For more information,
    see
    \"[Enforcing a policy for workflow permissions in your
    enterprise](https://docs.github.com/enterprise-cloud@latest/admin/policies/enforcing-policies-for-
    your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise#enforcing-a-policy-for-
    workflow-permissions-in-your-enterprise).\"

    You must authenticate using an access token with the `admin:enterprise` scope to use this endpoint.
    GitHub Apps must have the `enterprise_administration:write` permission to use this endpoint.

    Args:
        enterprise (str):

    Returns:
        Response[ActionsGetDefaultWorkflowPermissions]
    """

    kwargs = _get_kwargs(
        enterprise=enterprise,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    enterprise: str,
    *,
    client: Client,
) -> Optional[ActionsGetDefaultWorkflowPermissions]:
    """Get default workflow permissions for an enterprise

     Gets the default workflow permissions granted to the `GITHUB_TOKEN` when running workflows in an
    enterprise,
    as well as whether GitHub Actions can submit approving pull request reviews. For more information,
    see
    \"[Enforcing a policy for workflow permissions in your
    enterprise](https://docs.github.com/enterprise-cloud@latest/admin/policies/enforcing-policies-for-
    your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise#enforcing-a-policy-for-
    workflow-permissions-in-your-enterprise).\"

    You must authenticate using an access token with the `admin:enterprise` scope to use this endpoint.
    GitHub Apps must have the `enterprise_administration:write` permission to use this endpoint.

    Args:
        enterprise (str):

    Returns:
        Response[ActionsGetDefaultWorkflowPermissions]
    """

    return (
        await asyncio_detailed(
            enterprise=enterprise,
            client=client,
        )
    ).parsed
