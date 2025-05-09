import typer

from datetime import datetime
from rich.console import Console
from rich.table import Table

from utils.config import configure_flow
from utils.exceptions import ConfigurationError

action_app = typer.Typer()
console = Console()

reppd_client = ReppdClient()

@action_app.command()
def list():
    """"""
    try:
        actions = reppd_client.get_actions_list()

        table = Table("id", "title", "desciption", "status", "start_date")
        for a in actions:
            table.add_row(
                str(a.id),
                a.title,
                a.description,
                a.status,
                datetime.strftime(datetime.fromisoformat(a.start_date), '%d/%m/%Y')
            )
        console.print(table)
    except ConfigurationError as e:
        print(f"You must configure the application to begin using it. {e}")
        configure_flow()