from pathlib import Path
import typer


config_app = typer.Typer()

config_path = Path.home()

@config_app.command()
def show():
    """
    Show the contents of the reppd-cli configuration file.
    """
    print(config_path)