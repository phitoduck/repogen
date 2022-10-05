set dotenv-load := true

install:
    python -m pip install -e .
    # install the generated GitHub api client
    python -m pip install -e ./github-api-client

pulumi-up:
    #!/bin/bash
    pulumi up --yes -v 3 --stack repogen

    # this was logging the github access token to out.txt!!! very bad. Luckily GitHub auto-revokes those
    # pulumi up --logtostderr --logflow -v=9 2> out.txt

pulumi-destroy:
    #!/bin/bash
    pulumi destroy --skip-preview --yes --stack repogen

pulumi-cancel:
    pulumi cancel

github-public-key:
    #!/bin/bash
    REPO_ID=543829938
    ENVIRONMENT_NAME=Sandbox
    REPO_NAME=sample-repo
    curl \
        -H "Accept: application/vnd.github+json" \
        -H "Authorization: Bearer $GITHUB_TOKEN" \
        https://api.github.com/repositories/$REPO_ID/environments/$REPO_NAME:$ENVIRONMENT_NAME/secrets/public-key
        # https://api.github.com/repositories/$REPO_ID/environments/$ENVIRONMENT_NAME/secrets/public-key

generate-github-api-python-client-deprecated:
    #!/bin/bash
    OPENAPI_JSON_FPATH="github-openapi.json"
    # wget https://raw.githubusercontent.com/github/rest-api-description/main/descriptions/api.github.com/api.github.com.json \
    #     -O $OPENAPI_JSON_FPATH
    docker run --rm \
        -v $PWD:/local openapitools/openapi-generator-cli generate \
        -i /local/$OPENAPI_JSON_FPATH \
        -g python \
        -o /local/github-client/

generate-github-api-python-client:
    #!/bin/bash
    GITHUB_OPENAPI_JSON_URL="https://raw.githubusercontent.com/github/rest-api-description/main/descriptions/api.github.com/api.github.com.json"
    which pipx || python -m pip install pipx
    pipx run openapi-python-client generate --url "$GITHUB_OPENAPI_JSON_URL" 


update-project:
    python .projenrc.py

build:
    #!/bin/bash
    python -m pip install build
    python -m build --wheel

publish-test:
    twine upload \
        --repository-url "https://test.pypi.org/legacy/" \
        --username "$TEST_PYPI__TWINE_USERNAME" \
        --password "$TEST_PYPI__TWINE_PASSWORD" \
        --verbose \
        dist/*

publish-prod:
    twine upload \
        --repository-url "https://upload.pypi.org/legacy/" \
        --username "$TWINE_USERNAME" \
        --password "$TWINE_PASSWORD" \
        --verbose \
        dist/*

clean:
    rm -rf dist/ build/
    
release: update-project clean build publish-test publish-prod