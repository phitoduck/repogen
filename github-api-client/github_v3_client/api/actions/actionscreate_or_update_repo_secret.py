from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.actionscreate_or_update_repo_secret_json_body import ActionscreateOrUpdateRepoSecretJsonBody
from ...models.empty_object import EmptyObject
from ...types import Response


def _get_kwargs(
    owner: str,
    repo: str,
    secret_name: str,
    *,
    client: Client,
    json_body: ActionscreateOrUpdateRepoSecretJsonBody,
) -> Dict[str, Any]:
    url = "{}/repos/{owner}/{repo}/actions/secrets/{secret_name}".format(
        client.base_url, owner=owner, repo=repo, secret_name=secret_name
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, EmptyObject]]:
    if response.status_code == 201:
        response_201 = EmptyObject.from_dict(response.json())

        return response_201
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, EmptyObject]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    owner: str,
    repo: str,
    secret_name: str,
    *,
    client: Client,
    json_body: ActionscreateOrUpdateRepoSecretJsonBody,
) -> Response[Union[Any, EmptyObject]]:
    """Create or update a repository secret

     Creates or updates a repository secret with an encrypted value. Encrypt your secret using
    [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). You must authenticate
    using an access
    token with the `repo` scope to use this endpoint. GitHub Apps must have the `secrets` repository
    permission to use
    this endpoint.

    #### Example encrypting a secret using Node.js

    Encrypt your secret using the [tweetsodium](https://github.com/github/tweetsodium) library.

    ```
    const sodium = require('tweetsodium');

    const key = \"base64-encoded-public-key\";
    const value = \"plain-text-secret\";

    // Convert the message and key to Uint8Array's (Buffer implements that interface)
    const messageBytes = Buffer.from(value);
    const keyBytes = Buffer.from(key, 'base64');

    // Encrypt using LibSodium.
    const encryptedBytes = sodium.seal(messageBytes, keyBytes);

    // Base64 the encrypted secret
    const encrypted = Buffer.from(encryptedBytes).toString('base64');

    console.log(encrypted);
    ```


    #### Example encrypting a secret using Python

    Encrypt your secret using [pynacl](https://pynacl.readthedocs.io/en/latest/public/#nacl-public-
    sealedbox) with Python 3.

    ```
    from base64 import b64encode
    from nacl import encoding, public

    def encrypt(public_key: str, secret_value: str) -> str:
      \"\"\"Encrypt a Unicode string using the public key.\"\"\"
      public_key = public.PublicKey(public_key.encode(\"utf-8\"), encoding.Base64Encoder())
      sealed_box = public.SealedBox(public_key)
      encrypted = sealed_box.encrypt(secret_value.encode(\"utf-8\"))
      return b64encode(encrypted).decode(\"utf-8\")
    ```

    #### Example encrypting a secret using C#

    Encrypt your secret using the [Sodium.Core](https://www.nuget.org/packages/Sodium.Core/) package.

    ```
    var secretValue = System.Text.Encoding.UTF8.GetBytes(\"mySecret\");
    var publicKey = Convert.FromBase64String(\"2Sg8iYjAxxmI2LvUXpJjkYrMxURPc8r+dB7TJyvvcCU=\");

    var sealedPublicKeyBox = Sodium.SealedPublicKeyBox.Create(secretValue, publicKey);

    Console.WriteLine(Convert.ToBase64String(sealedPublicKeyBox));
    ```

    #### Example encrypting a secret using Ruby

    Encrypt your secret using the [rbnacl](https://github.com/RubyCrypto/rbnacl) gem.

    ```ruby
    require \"rbnacl\"
    require \"base64\"

    key = Base64.decode64(\"+ZYvJDZMHUfBkJdyq5Zm9SKqeuBQ4sj+6sfjlH4CgG0=\")
    public_key = RbNaCl::PublicKey.new(key)

    box = RbNaCl::Boxes::Sealed.from_public_key(public_key)
    encrypted_secret = box.encrypt(\"my_secret\")

    # Print the base64 encoded secret
    puts Base64.strict_encode64(encrypted_secret)
    ```

    Args:
        owner (str):
        repo (str):
        secret_name (str):
        json_body (ActionscreateOrUpdateRepoSecretJsonBody):

    Returns:
        Response[Union[Any, EmptyObject]]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        secret_name=secret_name,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    owner: str,
    repo: str,
    secret_name: str,
    *,
    client: Client,
    json_body: ActionscreateOrUpdateRepoSecretJsonBody,
) -> Optional[Union[Any, EmptyObject]]:
    """Create or update a repository secret

     Creates or updates a repository secret with an encrypted value. Encrypt your secret using
    [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). You must authenticate
    using an access
    token with the `repo` scope to use this endpoint. GitHub Apps must have the `secrets` repository
    permission to use
    this endpoint.

    #### Example encrypting a secret using Node.js

    Encrypt your secret using the [tweetsodium](https://github.com/github/tweetsodium) library.

    ```
    const sodium = require('tweetsodium');

    const key = \"base64-encoded-public-key\";
    const value = \"plain-text-secret\";

    // Convert the message and key to Uint8Array's (Buffer implements that interface)
    const messageBytes = Buffer.from(value);
    const keyBytes = Buffer.from(key, 'base64');

    // Encrypt using LibSodium.
    const encryptedBytes = sodium.seal(messageBytes, keyBytes);

    // Base64 the encrypted secret
    const encrypted = Buffer.from(encryptedBytes).toString('base64');

    console.log(encrypted);
    ```


    #### Example encrypting a secret using Python

    Encrypt your secret using [pynacl](https://pynacl.readthedocs.io/en/latest/public/#nacl-public-
    sealedbox) with Python 3.

    ```
    from base64 import b64encode
    from nacl import encoding, public

    def encrypt(public_key: str, secret_value: str) -> str:
      \"\"\"Encrypt a Unicode string using the public key.\"\"\"
      public_key = public.PublicKey(public_key.encode(\"utf-8\"), encoding.Base64Encoder())
      sealed_box = public.SealedBox(public_key)
      encrypted = sealed_box.encrypt(secret_value.encode(\"utf-8\"))
      return b64encode(encrypted).decode(\"utf-8\")
    ```

    #### Example encrypting a secret using C#

    Encrypt your secret using the [Sodium.Core](https://www.nuget.org/packages/Sodium.Core/) package.

    ```
    var secretValue = System.Text.Encoding.UTF8.GetBytes(\"mySecret\");
    var publicKey = Convert.FromBase64String(\"2Sg8iYjAxxmI2LvUXpJjkYrMxURPc8r+dB7TJyvvcCU=\");

    var sealedPublicKeyBox = Sodium.SealedPublicKeyBox.Create(secretValue, publicKey);

    Console.WriteLine(Convert.ToBase64String(sealedPublicKeyBox));
    ```

    #### Example encrypting a secret using Ruby

    Encrypt your secret using the [rbnacl](https://github.com/RubyCrypto/rbnacl) gem.

    ```ruby
    require \"rbnacl\"
    require \"base64\"

    key = Base64.decode64(\"+ZYvJDZMHUfBkJdyq5Zm9SKqeuBQ4sj+6sfjlH4CgG0=\")
    public_key = RbNaCl::PublicKey.new(key)

    box = RbNaCl::Boxes::Sealed.from_public_key(public_key)
    encrypted_secret = box.encrypt(\"my_secret\")

    # Print the base64 encoded secret
    puts Base64.strict_encode64(encrypted_secret)
    ```

    Args:
        owner (str):
        repo (str):
        secret_name (str):
        json_body (ActionscreateOrUpdateRepoSecretJsonBody):

    Returns:
        Response[Union[Any, EmptyObject]]
    """

    return sync_detailed(
        owner=owner,
        repo=repo,
        secret_name=secret_name,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    owner: str,
    repo: str,
    secret_name: str,
    *,
    client: Client,
    json_body: ActionscreateOrUpdateRepoSecretJsonBody,
) -> Response[Union[Any, EmptyObject]]:
    """Create or update a repository secret

     Creates or updates a repository secret with an encrypted value. Encrypt your secret using
    [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). You must authenticate
    using an access
    token with the `repo` scope to use this endpoint. GitHub Apps must have the `secrets` repository
    permission to use
    this endpoint.

    #### Example encrypting a secret using Node.js

    Encrypt your secret using the [tweetsodium](https://github.com/github/tweetsodium) library.

    ```
    const sodium = require('tweetsodium');

    const key = \"base64-encoded-public-key\";
    const value = \"plain-text-secret\";

    // Convert the message and key to Uint8Array's (Buffer implements that interface)
    const messageBytes = Buffer.from(value);
    const keyBytes = Buffer.from(key, 'base64');

    // Encrypt using LibSodium.
    const encryptedBytes = sodium.seal(messageBytes, keyBytes);

    // Base64 the encrypted secret
    const encrypted = Buffer.from(encryptedBytes).toString('base64');

    console.log(encrypted);
    ```


    #### Example encrypting a secret using Python

    Encrypt your secret using [pynacl](https://pynacl.readthedocs.io/en/latest/public/#nacl-public-
    sealedbox) with Python 3.

    ```
    from base64 import b64encode
    from nacl import encoding, public

    def encrypt(public_key: str, secret_value: str) -> str:
      \"\"\"Encrypt a Unicode string using the public key.\"\"\"
      public_key = public.PublicKey(public_key.encode(\"utf-8\"), encoding.Base64Encoder())
      sealed_box = public.SealedBox(public_key)
      encrypted = sealed_box.encrypt(secret_value.encode(\"utf-8\"))
      return b64encode(encrypted).decode(\"utf-8\")
    ```

    #### Example encrypting a secret using C#

    Encrypt your secret using the [Sodium.Core](https://www.nuget.org/packages/Sodium.Core/) package.

    ```
    var secretValue = System.Text.Encoding.UTF8.GetBytes(\"mySecret\");
    var publicKey = Convert.FromBase64String(\"2Sg8iYjAxxmI2LvUXpJjkYrMxURPc8r+dB7TJyvvcCU=\");

    var sealedPublicKeyBox = Sodium.SealedPublicKeyBox.Create(secretValue, publicKey);

    Console.WriteLine(Convert.ToBase64String(sealedPublicKeyBox));
    ```

    #### Example encrypting a secret using Ruby

    Encrypt your secret using the [rbnacl](https://github.com/RubyCrypto/rbnacl) gem.

    ```ruby
    require \"rbnacl\"
    require \"base64\"

    key = Base64.decode64(\"+ZYvJDZMHUfBkJdyq5Zm9SKqeuBQ4sj+6sfjlH4CgG0=\")
    public_key = RbNaCl::PublicKey.new(key)

    box = RbNaCl::Boxes::Sealed.from_public_key(public_key)
    encrypted_secret = box.encrypt(\"my_secret\")

    # Print the base64 encoded secret
    puts Base64.strict_encode64(encrypted_secret)
    ```

    Args:
        owner (str):
        repo (str):
        secret_name (str):
        json_body (ActionscreateOrUpdateRepoSecretJsonBody):

    Returns:
        Response[Union[Any, EmptyObject]]
    """

    kwargs = _get_kwargs(
        owner=owner,
        repo=repo,
        secret_name=secret_name,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    owner: str,
    repo: str,
    secret_name: str,
    *,
    client: Client,
    json_body: ActionscreateOrUpdateRepoSecretJsonBody,
) -> Optional[Union[Any, EmptyObject]]:
    """Create or update a repository secret

     Creates or updates a repository secret with an encrypted value. Encrypt your secret using
    [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). You must authenticate
    using an access
    token with the `repo` scope to use this endpoint. GitHub Apps must have the `secrets` repository
    permission to use
    this endpoint.

    #### Example encrypting a secret using Node.js

    Encrypt your secret using the [tweetsodium](https://github.com/github/tweetsodium) library.

    ```
    const sodium = require('tweetsodium');

    const key = \"base64-encoded-public-key\";
    const value = \"plain-text-secret\";

    // Convert the message and key to Uint8Array's (Buffer implements that interface)
    const messageBytes = Buffer.from(value);
    const keyBytes = Buffer.from(key, 'base64');

    // Encrypt using LibSodium.
    const encryptedBytes = sodium.seal(messageBytes, keyBytes);

    // Base64 the encrypted secret
    const encrypted = Buffer.from(encryptedBytes).toString('base64');

    console.log(encrypted);
    ```


    #### Example encrypting a secret using Python

    Encrypt your secret using [pynacl](https://pynacl.readthedocs.io/en/latest/public/#nacl-public-
    sealedbox) with Python 3.

    ```
    from base64 import b64encode
    from nacl import encoding, public

    def encrypt(public_key: str, secret_value: str) -> str:
      \"\"\"Encrypt a Unicode string using the public key.\"\"\"
      public_key = public.PublicKey(public_key.encode(\"utf-8\"), encoding.Base64Encoder())
      sealed_box = public.SealedBox(public_key)
      encrypted = sealed_box.encrypt(secret_value.encode(\"utf-8\"))
      return b64encode(encrypted).decode(\"utf-8\")
    ```

    #### Example encrypting a secret using C#

    Encrypt your secret using the [Sodium.Core](https://www.nuget.org/packages/Sodium.Core/) package.

    ```
    var secretValue = System.Text.Encoding.UTF8.GetBytes(\"mySecret\");
    var publicKey = Convert.FromBase64String(\"2Sg8iYjAxxmI2LvUXpJjkYrMxURPc8r+dB7TJyvvcCU=\");

    var sealedPublicKeyBox = Sodium.SealedPublicKeyBox.Create(secretValue, publicKey);

    Console.WriteLine(Convert.ToBase64String(sealedPublicKeyBox));
    ```

    #### Example encrypting a secret using Ruby

    Encrypt your secret using the [rbnacl](https://github.com/RubyCrypto/rbnacl) gem.

    ```ruby
    require \"rbnacl\"
    require \"base64\"

    key = Base64.decode64(\"+ZYvJDZMHUfBkJdyq5Zm9SKqeuBQ4sj+6sfjlH4CgG0=\")
    public_key = RbNaCl::PublicKey.new(key)

    box = RbNaCl::Boxes::Sealed.from_public_key(public_key)
    encrypted_secret = box.encrypt(\"my_secret\")

    # Print the base64 encoded secret
    puts Base64.strict_encode64(encrypted_secret)
    ```

    Args:
        owner (str):
        repo (str):
        secret_name (str):
        json_body (ActionscreateOrUpdateRepoSecretJsonBody):

    Returns:
        Response[Union[Any, EmptyObject]]
    """

    return (
        await asyncio_detailed(
            owner=owner,
            repo=repo,
            secret_name=secret_name,
            client=client,
            json_body=json_body,
        )
    ).parsed
