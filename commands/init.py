from pathlib import Path
import typer

from utils.config import create_config_file, configure_flow


def run():
    """
    Initialise and authenticate with the reppd-cli application.
    """
    typer.echo("Initialising the Reppd CLI")

    configure_flow()

    typer.echo(f"Config file created at: {config_path}")
    

init_app = typer.Typer(
    callback=run,
    invoke_without_command=True,
    help="Intiialise Reppd CLI and set up the configuration."
)