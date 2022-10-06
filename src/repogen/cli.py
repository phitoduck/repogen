from repogen.repo_program import run as run_program
from typer import Typer, Argument, Option

def run():
    cli = create_cli()
    cli()

def create_cli() -> Typer:
    cli = Typer()

    @cli.command(name="create-repo")
    def __create_repo(repo_name: str = Option(..., allow_dash=True)):
        create_repo(repo_name=repo_name)

    @cli.command(name="destroy-repo")
    def __destroy_repo(repo_name: str = Option(..., allow_dash=True)):
        destroy_repo(repo_name=repo_name)

    return cli

def create_repo(repo_name: str):
    run_program(repo_name=repo_name, destroy=False)

def destroy_repo(repo_name: str):
    run_program(repo_name=repo_name, destroy=True)

if __name__ == "__main__":
    run()