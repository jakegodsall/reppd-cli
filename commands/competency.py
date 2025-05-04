import typer
from utils.reppd_client import ReppdClient
from utils.config import configure_flow
from utils.exceptions import ConfigurationError

competency_app = typer.Typer()

reppd_client = ReppdClient()

@competency_app.command()
def list():
    try:
        reppd_client.authenticate()
    except ConfigurationError as e:
        print("You must configure the application to begin using it.")
        configure_flow()
