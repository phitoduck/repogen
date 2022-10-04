from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.actionslist_self_hosted_runner_groups_for_org_response_200 import (
    ActionslistSelfHostedRunnerGroupsForOrgResponse200,
)
from ...types import UNSET, Response


def _get_kwargs(
    org: str,
    *,
    client: Client,
    per_page: int = 30,
    page: int = 1,
    visible_to_repository: str,
) -> Dict[str, Any]:
    url = "{}/orgs/{org}/actions/runner-groups".format(client.base_url, org=org)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["per_page"] = per_page

    params["page"] = page

    params["visible_to_repository"] = visible_to_repository

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[ActionslistSelfHostedRunnerGroupsForOrgResponse200]:
    if response.status_code == 200:
        response_200 = ActionslistSelfHostedRunnerGroupsForOrgResponse200.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ActionslistSelfHostedRunnerGroupsForOrgResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    org: str,
    *,
    client: Client,
    per_page: int = 30,
    page: int = 1,
    visible_to_repository: str,
) -> Response[ActionslistSelfHostedRunnerGroupsForOrgResponse200]:
    """List self-hosted runner groups for an organization

     The self-hosted runner groups REST API is available with GitHub Enterprise Cloud. For more
    information, see \"[GitHub's products](https://docs.github.com/github/getting-started-with-
    github/githubs-products).\"

    Lists all self-hosted runner groups configured in an organization and inherited from an enterprise.

    You must authenticate using an access token with the `admin:org` scope to use this endpoint.

    Args:
        org (str):
        per_page (int):  Default: 30.
        page (int):  Default: 1.
        visible_to_repository (str):

    Returns:
        Response[ActionslistSelfHostedRunnerGroupsForOrgResponse200]
    """

    kwargs = _get_kwargs(
        org=org,
        client=client,
        per_page=per_page,
        page=page,
        visible_to_repository=visible_to_repository,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    org: str,
    *,
    client: Client,
    per_page: int = 30,
    page: int = 1,
    visible_to_repository: str,
) -> Optional[ActionslistSelfHostedRunnerGroupsForOrgResponse200]:
    """List self-hosted runner groups for an organization

     The self-hosted runner groups REST API is available with GitHub Enterprise Cloud. For more
    information, see \"[GitHub's products](https://docs.github.com/github/getting-started-with-
    github/githubs-products).\"

    Lists all self-hosted runner groups configured in an organization and inherited from an enterprise.

    You must authenticate using an access token with the `admin:org` scope to use this endpoint.

    Args:
        org (str):
        per_page (int):  Default: 30.
        page (int):  Default: 1.
        visible_to_repository (str):

    Returns:
        Response[ActionslistSelfHostedRunnerGroupsForOrgResponse200]
    """

    return sync_detailed(
        org=org,
        client=client,
        per_page=per_page,
        page=page,
        visible_to_repository=visible_to_repository,
    ).parsed


async def asyncio_detailed(
    org: str,
    *,
    client: Client,
    per_page: int = 30,
    page: int = 1,
    visible_to_repository: str,
) -> Response[ActionslistSelfHostedRunnerGroupsForOrgResponse200]:
    """List self-hosted runner groups for an organization

     The self-hosted runner groups REST API is available with GitHub Enterprise Cloud. For more
    information, see \"[GitHub's products](https://docs.github.com/github/getting-started-with-
    github/githubs-products).\"

    Lists all self-hosted runner groups configured in an organization and inherited from an enterprise.

    You must authenticate using an access token with the `admin:org` scope to use this endpoint.

    Args:
        org (str):
        per_page (int):  Default: 30.
        page (int):  Default: 1.
        visible_to_repository (str):

    Returns:
        Response[ActionslistSelfHostedRunnerGroupsForOrgResponse200]
    """

    kwargs = _get_kwargs(
        org=org,
        client=client,
        per_page=per_page,
        page=page,
        visible_to_repository=visible_to_repository,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    org: str,
    *,
    client: Client,
    per_page: int = 30,
    page: int = 1,
    visible_to_repository: str,
) -> Optional[ActionslistSelfHostedRunnerGroupsForOrgResponse200]:
    """List self-hosted runner groups for an organization

     The self-hosted runner groups REST API is available with GitHub Enterprise Cloud. For more
    information, see \"[GitHub's products](https://docs.github.com/github/getting-started-with-
    github/githubs-products).\"

    Lists all self-hosted runner groups configured in an organization and inherited from an enterprise.

    You must authenticate using an access token with the `admin:org` scope to use this endpoint.

    Args:
        org (str):
        per_page (int):  Default: 30.
        page (int):  Default: 1.
        visible_to_repository (str):

    Returns:
        Response[ActionslistSelfHostedRunnerGroupsForOrgResponse200]
    """

    return (
        await asyncio_detailed(
            org=org,
            client=client,
            per_page=per_page,
            page=page,
            visible_to_repository=visible_to_repository,
        )
    ).parsed
