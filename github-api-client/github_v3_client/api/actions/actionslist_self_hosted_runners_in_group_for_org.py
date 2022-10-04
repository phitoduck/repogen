from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.actionslist_self_hosted_runners_in_group_for_org_response_200 import (
    ActionslistSelfHostedRunnersInGroupForOrgResponse200,
)
from ...types import UNSET, Response


def _get_kwargs(
    org: str,
    runner_group_id: int,
    *,
    client: Client,
    per_page: int = 30,
    page: int = 1,
) -> Dict[str, Any]:
    url = "{}/orgs/{org}/actions/runner-groups/{runner_group_id}/runners".format(
        client.base_url, org=org, runner_group_id=runner_group_id
    )

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


def _parse_response(*, response: httpx.Response) -> Optional[ActionslistSelfHostedRunnersInGroupForOrgResponse200]:
    if response.status_code == 200:
        response_200 = ActionslistSelfHostedRunnersInGroupForOrgResponse200.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ActionslistSelfHostedRunnersInGroupForOrgResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    org: str,
    runner_group_id: int,
    *,
    client: Client,
    per_page: int = 30,
    page: int = 1,
) -> Response[ActionslistSelfHostedRunnersInGroupForOrgResponse200]:
    """List self-hosted runners in a group for an organization

     The self-hosted runner groups REST API is available with GitHub Enterprise Cloud. For more
    information, see \"[GitHub's products](https://docs.github.com/github/getting-started-with-
    github/githubs-products).\"

    Lists self-hosted runners that are in a specific organization group.

    You must authenticate using an access token with the `admin:org` scope to use this endpoint.

    Args:
        org (str):
        runner_group_id (int):
        per_page (int):  Default: 30.
        page (int):  Default: 1.

    Returns:
        Response[ActionslistSelfHostedRunnersInGroupForOrgResponse200]
    """

    kwargs = _get_kwargs(
        org=org,
        runner_group_id=runner_group_id,
        client=client,
        per_page=per_page,
        page=page,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    org: str,
    runner_group_id: int,
    *,
    client: Client,
    per_page: int = 30,
    page: int = 1,
) -> Optional[ActionslistSelfHostedRunnersInGroupForOrgResponse200]:
    """List self-hosted runners in a group for an organization

     The self-hosted runner groups REST API is available with GitHub Enterprise Cloud. For more
    information, see \"[GitHub's products](https://docs.github.com/github/getting-started-with-
    github/githubs-products).\"

    Lists self-hosted runners that are in a specific organization group.

    You must authenticate using an access token with the `admin:org` scope to use this endpoint.

    Args:
        org (str):
        runner_group_id (int):
        per_page (int):  Default: 30.
        page (int):  Default: 1.

    Returns:
        Response[ActionslistSelfHostedRunnersInGroupForOrgResponse200]
    """

    return sync_detailed(
        org=org,
        runner_group_id=runner_group_id,
        client=client,
        per_page=per_page,
        page=page,
    ).parsed


async def asyncio_detailed(
    org: str,
    runner_group_id: int,
    *,
    client: Client,
    per_page: int = 30,
    page: int = 1,
) -> Response[ActionslistSelfHostedRunnersInGroupForOrgResponse200]:
    """List self-hosted runners in a group for an organization

     The self-hosted runner groups REST API is available with GitHub Enterprise Cloud. For more
    information, see \"[GitHub's products](https://docs.github.com/github/getting-started-with-
    github/githubs-products).\"

    Lists self-hosted runners that are in a specific organization group.

    You must authenticate using an access token with the `admin:org` scope to use this endpoint.

    Args:
        org (str):
        runner_group_id (int):
        per_page (int):  Default: 30.
        page (int):  Default: 1.

    Returns:
        Response[ActionslistSelfHostedRunnersInGroupForOrgResponse200]
    """

    kwargs = _get_kwargs(
        org=org,
        runner_group_id=runner_group_id,
        client=client,
        per_page=per_page,
        page=page,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    org: str,
    runner_group_id: int,
    *,
    client: Client,
    per_page: int = 30,
    page: int = 1,
) -> Optional[ActionslistSelfHostedRunnersInGroupForOrgResponse200]:
    """List self-hosted runners in a group for an organization

     The self-hosted runner groups REST API is available with GitHub Enterprise Cloud. For more
    information, see \"[GitHub's products](https://docs.github.com/github/getting-started-with-
    github/githubs-products).\"

    Lists self-hosted runners that are in a specific organization group.

    You must authenticate using an access token with the `admin:org` scope to use this endpoint.

    Args:
        org (str):
        runner_group_id (int):
        per_page (int):  Default: 30.
        page (int):  Default: 1.

    Returns:
        Response[ActionslistSelfHostedRunnersInGroupForOrgResponse200]
    """

    return (
        await asyncio_detailed(
            org=org,
            runner_group_id=runner_group_id,
            client=client,
            per_page=per_page,
            page=page,
        )
    ).parsed
