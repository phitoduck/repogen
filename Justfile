set dotenv-load := true

pulumi-up:
    #!/bin/bash
    pulumi up -v 3

pulumi-destroy:
    #!/bin/bash
    pulumi destroy