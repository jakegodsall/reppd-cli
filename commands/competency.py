import typer
from utils.reppd_client import ReppdClient
from utils.config import configure_flow
from utils.exceptions import ConfigurationError

competency_app = typer.Typer()

reppd_client = ReppdClient()

@competency_app.command()
def list():
    try:
        reppd_client.get_competency_list()
    except ConfigurationError as e:
        print(f"You must configure the application to begin using it. {e}")
        configure_flow()
