from typing import Any, Dict

import httpx

from ...client import Client
from ...models.selected_actions import SelectedActions
from ...types import Response


def _get_kwargs(
    org: str,
    *,
    client: Client,
    json_body: SelectedActions,
) -> Dict[str, Any]:
    url = "{}/orgs/{org}/actions/permissions/selected-actions".format(client.base_url, org=org)

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
    json_body: SelectedActions,
) -> Response[Any]:
    """Set allowed actions and reusable workflows for an organization

     Sets the actions and reusable workflows that are allowed in an organization. To use this endpoint,
    the organization permission policy for `allowed_actions` must be configured to `selected`. For more
    information, see \"[Set GitHub Actions permissions for an organization](#set-github-actions-
    permissions-for-an-organization).\"

    If the organization belongs to an enterprise that has `selected` actions and reusable workflows set
    at the enterprise level, then you cannot override any of the enterprise's allowed actions and
    reusable workflows settings.

    To use the `patterns_allowed` setting for private repositories, the organization must belong to an
    enterprise. If the organization does not belong to an enterprise, then the `patterns_allowed`
    setting only applies to public repositories in the organization.

    You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub
    Apps must have the `administration` organization permission to use this API.

    Args:
        org (str):
        json_body (SelectedActions):

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
    json_body: SelectedActions,
) -> Response[Any]:
    """Set allowed actions and reusable workflows for an organization

     Sets the actions and reusable workflows that are allowed in an organization. To use this endpoint,
    the organization permission policy for `allowed_actions` must be configured to `selected`. For more
    information, see \"[Set GitHub Actions permissions for an organization](#set-github-actions-
    permissions-for-an-organization).\"

    If the organization belongs to an enterprise that has `selected` actions and reusable workflows set
    at the enterprise level, then you cannot override any of the enterprise's allowed actions and
    reusable workflows settings.

    To use the `patterns_allowed` setting for private repositories, the organization must belong to an
    enterprise. If the organization does not belong to an enterprise, then the `patterns_allowed`
    setting only applies to public repositories in the organization.

    You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub
    Apps must have the `administration` organization permission to use this API.

    Args:
        org (str):
        json_body (SelectedActions):

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
