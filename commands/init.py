from pathlib import Path
import typer

from utils.config import create_config_file


def run():
    """
    Initialise and authenticate with the reppd-cli application.
    """
    typer.echo("Initialising the Reppd CLI")

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    config_path = create_config_file({
        "username": username,
        "password": password
    })

    typer.echo(f"Config file created at: {config_path}")
    

init_app = typer.Typer(
    callback=run,
    invoke_without_command=True,
    help="Intiialise Reppd CLI and set up the configuration."
)