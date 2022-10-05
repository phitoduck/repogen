from phito_projen import PythonPackage

project = PythonPackage(
    name="repogen",
    module_name="repogen",
    version="0.0.0",
    install_requires=[
        "pulumi>=3.0.0,<4.0.0",
        "pulumi_github",
        "pynacl",
        "GitPython",
        "python-dotenv",
        "phitoduck-projen",
        "typer",
        "rich",
    ],
    entrypoints={"repogen": "repogen.cli:run"}
)
project.gitignore.add_patterns("!sample.env")

project.synth()