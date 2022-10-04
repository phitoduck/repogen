from typing import Any, Dict

import httpx

from ...client import Client
from ...models.actionsset_self_hosted_runners_in_group_for_org_json_body import (
    ActionssetSelfHostedRunnersInGroupForOrgJsonBody,
)
from ...types import Response


def _get_kwargs(
    org: str,
    runner_group_id: int,
    *,
    client: Client,
    json_body: ActionssetSelfHostedRunnersInGroupForOrgJsonBody,
) -> Dict[str, Any]:
    url = "{}/orgs/{org}/actions/runner-groups/{runner_group_id}/runners".format(
        client.base_url, org=org, runner_group_id=runner_group_id
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
    runner_group_id: int,
    *,
    client: Client,
    json_body: ActionssetSelfHostedRunnersInGroupForOrgJsonBody,
) -> Response[Any]:
    """Set self-hosted runners in a group for an organization

     The self-hosted runner groups REST API is available with GitHub Enterprise Cloud. For more
    information, see \"[GitHub's products](https://docs.github.com/github/getting-started-with-
    github/githubs-products).\"

    Replaces the list of self-hosted runners that are part of an organization runner group.

    You must authenticate using an access token with the `admin:org` scope to use this endpoint.

    Args:
        org (str):
        runner_group_id (int):
        json_body (ActionssetSelfHostedRunnersInGroupForOrgJsonBody):

    Returns:
        Response[Any]
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


async def asyncio_detailed(
    org: str,
    runner_group_id: int,
    *,
    client: Client,
    json_body: ActionssetSelfHostedRunnersInGroupForOrgJsonBody,
) -> Response[Any]:
    """Set self-hosted runners in a group for an organization

     The self-hosted runner groups REST API is available with GitHub Enterprise Cloud. For more
    information, see \"[GitHub's products](https://docs.github.com/github/getting-started-with-
    github/githubs-products).\"

    Replaces the list of self-hosted runners that are part of an organization runner group.

    You must authenticate using an access token with the `admin:org` scope to use this endpoint.

    Args:
        org (str):
        runner_group_id (int):
        json_body (ActionssetSelfHostedRunnersInGroupForOrgJsonBody):

    Returns:
        Response[Any]
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
