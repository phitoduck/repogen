from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.actionscreate_self_hosted_runner_group_for_org_json_body import (
    ActionscreateSelfHostedRunnerGroupForOrgJsonBody,
)
from ...models.runner_groups_org import RunnerGroupsOrg
from ...types import Response


def _get_kwargs(
    org: str,
    *,
    client: Client,
    json_body: ActionscreateSelfHostedRunnerGroupForOrgJsonBody,
) -> Dict[str, Any]:
    url = "{}/orgs/{org}/actions/runner-groups".format(client.base_url, org=org)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[RunnerGroupsOrg]:
    if response.status_code == 201:
        response_201 = RunnerGroupsOrg.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[RunnerGroupsOrg]:
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
    json_body: ActionscreateSelfHostedRunnerGroupForOrgJsonBody,
) -> Response[RunnerGroupsOrg]:
    """Create a self-hosted runner group for an organization

     The self-hosted runner groups REST API is available with GitHub Enterprise Cloud and GitHub
    Enterprise Server. For more information, see \"[GitHub's
    products](https://docs.github.com/github/getting-started-with-github/githubs-products).\"

    Creates a new self-hosted runner group for an organization.

    You must authenticate using an access token with the `admin:org` scope to use this endpoint.

    Args:
        org (str):
        json_body (ActionscreateSelfHostedRunnerGroupForOrgJsonBody):

    Returns:
        Response[RunnerGroupsOrg]
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


def sync(
    org: str,
    *,
    client: Client,
    json_body: ActionscreateSelfHostedRunnerGroupForOrgJsonBody,
) -> Optional[RunnerGroupsOrg]:
    """Create a self-hosted runner group for an organization

     The self-hosted runner groups REST API is available with GitHub Enterprise Cloud and GitHub
    Enterprise Server. For more information, see \"[GitHub's
    products](https://docs.github.com/github/getting-started-with-github/githubs-products).\"

    Creates a new self-hosted runner group for an organization.

    You must authenticate using an access token with the `admin:org` scope to use this endpoint.

    Args:
        org (str):
        json_body (ActionscreateSelfHostedRunnerGroupForOrgJsonBody):

    Returns:
        Response[RunnerGroupsOrg]
    """

    return sync_detailed(
        org=org,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    org: str,
    *,
    client: Client,
    json_body: ActionscreateSelfHostedRunnerGroupForOrgJsonBody,
) -> Response[RunnerGroupsOrg]:
    """Create a self-hosted runner group for an organization

     The self-hosted runner groups REST API is available with GitHub Enterprise Cloud and GitHub
    Enterprise Server. For more information, see \"[GitHub's
    products](https://docs.github.com/github/getting-started-with-github/githubs-products).\"

    Creates a new self-hosted runner group for an organization.

    You must authenticate using an access token with the `admin:org` scope to use this endpoint.

    Args:
        org (str):
        json_body (ActionscreateSelfHostedRunnerGroupForOrgJsonBody):

    Returns:
        Response[RunnerGroupsOrg]
    """

    kwargs = _get_kwargs(
        org=org,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    org: str,
    *,
    client: Client,
    json_body: ActionscreateSelfHostedRunnerGroupForOrgJsonBody,
) -> Optional[RunnerGroupsOrg]:
    """Create a self-hosted runner group for an organization

     The self-hosted runner groups REST API is available with GitHub Enterprise Cloud and GitHub
    Enterprise Server. For more information, see \"[GitHub's
    products](https://docs.github.com/github/getting-started-with-github/githubs-products).\"

    Creates a new self-hosted runner group for an organization.

    You must authenticate using an access token with the `admin:org` scope to use this endpoint.

    Args:
        org (str):
        json_body (ActionscreateSelfHostedRunnerGroupForOrgJsonBody):

    Returns:
        Response[RunnerGroupsOrg]
    """

    return (
        await asyncio_detailed(
            org=org,
            client=client,
            json_body=json_body,
        )
    ).parsed
