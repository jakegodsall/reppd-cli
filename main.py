import typer
from dotenv import load_dotenv

from commands.config import config_app
from commands.init import init_app
from commands.competency import competency_app
from commands.actions import action_app

load_dotenv()

app = typer.Typer()

app.add_typer(init_app, name="init")
app.add_typer(competency_app, name="competency")
app.add_typer(action_app, name="action")
app.add_typer(config_app, name="config")

if __name__ == "__main__":
    app()