import typer

from rich.console import Console
from rich.table import Table
from datetime import datetime

from utils.reppd_client import ReppdClient
from utils.config import configure_flow
from utils.exceptions import ConfigurationError

competency_app = typer.Typer()
console = Console()

reppd_client = ReppdClient()

@competency_app.command()
def list():
    try:
        competencies = reppd_client.get_competency_list()

        table = Table("id", "title", "desciption", "status", "start_date")
        for c in competencies:
            table.add_row(
                str(c.id),
                c.title,
                c.description,
                c.status,
                datetime.strftime(datetime.fromisoformat(c.start_date), '%d/%m/%Y')
            )
        console.print(table)
    except ConfigurationError as e:
        print(f"You must configure the application to begin using it. {e}")
        configure_flow()
