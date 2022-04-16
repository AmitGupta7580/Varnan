import validators

import typer
from typing import List, Optional

from varnan import __app_name__, __version__, varnan
from varnan.category import Category
from varnan.task import Task

app = typer.Typer()
list_app = typer.Typer()
app.add_typer(list_app, name="list", help="List the items of workspace")
add_app = typer.Typer()
app.add_typer(add_app, name="add", help="Add items in workspace")

tool = None

@app.command()
def init(
    ctf: Optional[str] = typer.Option(
        "",
        "--ctf"
    ),
    creds: Optional[str] = typer.Option(
        "",
        "--creds"
    ),
) -> None:
    """Initialize Standard/Customized Workspace."""
    if ctf == "":
        tool.initialize()
    else:
        if validators.url(ctf):
            tool.initialize(ctf=ctf, creds=creds)
        else:
            print("invalid url")


@app.command()
def link(
    ctf: str = typer.Option(
        "",
        "--ctf",
        prompt="CTF Platform URL for customized workspace",
    ),
    creds: str = typer.Option(
        "",
        "--creds",
        prompt="Credentials of CTF platform for customized workspace",
    ),
) -> None:
    """Link a CTF with currnet working workspace.\n
    Warning : This command will delete all files and clean up the workspace."""
    if validators.url(ctf):
        tool.link(ctf, creds)
    else:
        print("invalid url")


@list_app.command('category')
def list_category() -> None:
    """List all the present CTF Categories in the workspace."""
    tool.list_category()


@list_app.command('task')
def list_task() -> None:
    """List all the present CTF Tasks in the workspace."""
    tool.list_task()


@add_app.command('category')
def add_category(
    name: str = typer.Option(
        "Misc",
        "-n"
        "--name",
        prompt="Name of the category",
    )
) -> None:
    """Add CTF Category in the workspace"""
    tool.add_category(Category(name))


@add_app.command('task')
def add_task(
    name: str = typer.Option(
        "Unnamed",
        "-n",
        "--name",
        prompt="Name of the task",
    ),
    description: str = typer.Option(
        "",
        "-d",
        "--desc",
        prompt="Description of the task",
    ),
    author: str = typer.Option(
        "",
        "-au",
        "--author",
        prompt="Author of the task",
    ),
    attatchments: List[str] = typer.Option(
        [],
        "-a",
        "--attach",
        prompt="Attachment URLs of the task",
    ),
    points: int = typer.Option(
        0,
        "-p",
        "--points",
        prompt="Points of the task",
    ),
) -> None:
    """Add CTF Task in the workspace"""
    # issue with attachments
    print(attatchments)
    tool.add_task(Task(name, description, author, points, attatchments))


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    global tool
    tool = varnan.Varnan()
    return