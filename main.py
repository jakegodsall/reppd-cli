import typer

from commands.config import config_app
from commands.init import init_app

app = typer.Typer()

app.add_typer(init_app, name="init")
app.add_typer(config_app, name="config")

if __name__ == "__main__":
    app()