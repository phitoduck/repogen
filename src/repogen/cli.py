from repogen.repo_program import run as run_program
from typer import Typer

def run():
    cli = create_cli()
    cli()

def create_cli() -> Typer:
    cli = Typer()
    cli.command()(create_repo)
    cli.command()(destroy_repo)
    return cli

def create_repo(repo_name: str):
    run_program(repo_name=repo_name, destroy=False)

def destroy_repo(repo_name: str):
    run_program(repo_name=repo_name, destroy=True)

if __name__ == "__main__":
    run()