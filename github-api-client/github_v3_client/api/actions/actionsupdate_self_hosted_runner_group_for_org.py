from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.actionsupdate_self_hosted_runner_group_for_org_json_body import (
    ActionsupdateSelfHostedRunnerGroupForOrgJsonBody,
)
from ...models.runner_groups_org import RunnerGroupsOrg
from ...types import Response


def _get_kwargs(
    org: str,
    runner_group_id: int,
    *,
    client: Client,
    json_body: ActionsupdateSelfHostedRunnerGroupForOrgJsonBody,
) -> Dict[str, Any]:
    url = "{}/orgs/{org}/actions/runner-groups/{runner_group_id}".format(
        client.base_url, org=org, runner_group_id=runner_group_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[RunnerGroupsOrg]:
    if response.status_code == 200:
        response_200 = RunnerGroupsOrg.from_dict(response.json())

        return response_200
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
    runner_group_id: int,
    *,
    client: Client,
    json_body: ActionsupdateSelfHostedRunnerGroupForOrgJsonBody,
) -> Response[RunnerGroupsOrg]:
    """Update a self-hosted runner group for an organization

     The self-hosted runner groups REST API is available with GitHub Enterprise Cloud. For more
    information, see \"[GitHub's products](https://docs.github.com/github/getting-started-with-
    github/githubs-products).\"

    Updates the `name` and `visibility` of a self-hosted runner group in an organization.

    You must authenticate using an access token with the `admin:org` scope to use this endpoint.

    Args:
        org (str):
        runner_group_id (int):
        json_body (ActionsupdateSelfHostedRunnerGroupForOrgJsonBody):

    Returns:
        Response[RunnerGroupsOrg]
    """

    kwargs = _get_kwargs(
        org=org,
        runner_group_id=runner_group_id,
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
    runner_group_id: int,
    *,
    client: Client,
    json_body: ActionsupdateSelfHostedRunnerGroupForOrgJsonBody,
) -> Optional[RunnerGroupsOrg]:
    """Update a self-hosted runner group for an organization

     The self-hosted runner groups REST API is available with GitHub Enterprise Cloud. For more
    information, see \"[GitHub's products](https://docs.github.com/github/getting-started-with-
    github/githubs-products).\"

    Updates the `name` and `visibility` of a self-hosted runner group in an organization.

    You must authenticate using an access token with the `admin:org` scope to use this endpoint.

    Args:
        org (str):
        runner_group_id (int):
        json_body (ActionsupdateSelfHostedRunnerGroupForOrgJsonBody):

    Returns:
        Response[RunnerGroupsOrg]
    """

    return sync_detailed(
        org=org,
        runner_group_id=runner_group_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    org: str,
    runner_group_id: int,
    *,
    client: Client,
    json_body: ActionsupdateSelfHostedRunnerGroupForOrgJsonBody,
) -> Response[RunnerGroupsOrg]:
    """Update a self-hosted runner group for an organization

     The self-hosted runner groups REST API is available with GitHub Enterprise Cloud. For more
    information, see \"[GitHub's products](https://docs.github.com/github/getting-started-with-
    github/githubs-products).\"

    Updates the `name` and `visibility` of a self-hosted runner group in an organization.

    You must authenticate using an access token with the `admin:org` scope to use this endpoint.

    Args:
        org (str):
        runner_group_id (int):
        json_body (ActionsupdateSelfHostedRunnerGroupForOrgJsonBody):

    Returns:
        Response[RunnerGroupsOrg]
    """

    kwargs = _get_kwargs(
        org=org,
        runner_group_id=runner_group_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    org: str,
    runner_group_id: int,
    *,
    client: Client,
    json_body: ActionsupdateSelfHostedRunnerGroupForOrgJsonBody,
) -> Optional[RunnerGroupsOrg]:
    """Update a self-hosted runner group for an organization

     The self-hosted runner groups REST API is available with GitHub Enterprise Cloud. For more
    information, see \"[GitHub's products](https://docs.github.com/github/getting-started-with-
    github/githubs-products).\"

    Updates the `name` and `visibility` of a self-hosted runner group in an organization.

    You must authenticate using an access token with the `admin:org` scope to use this endpoint.

    Args:
        org (str):
        runner_group_id (int):
        json_body (ActionsupdateSelfHostedRunnerGroupForOrgJsonBody):

    Returns:
        Response[RunnerGroupsOrg]
    """

    return (
        await asyncio_detailed(
            org=org,
            runner_group_id=runner_group_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
