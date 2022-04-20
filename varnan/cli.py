import os

import validators
import typer
from typing import List, Optional

from varnan import __app_name__, __version__, varnan
from varnan.category import Category
from varnan.exceptions import ConfigException
from varnan.task import Task


app = typer.Typer()
task_app = typer.Typer()
app.add_typer(task_app, name="task", help="Tasks commands")
category_app = typer.Typer()
app.add_typer(category_app, name="category", help="Category commands")


tool = None
_WORKSPACE = os.getcwd() + '\\'
_CONFIG_FILE_PATH = _WORKSPACE + '.varnan_config.xml'


@app.command()
def init(
    ctf_url: Optional[str] = typer.Option(
        "",
        "--ctf"
    ),
    creds: Optional[str] = typer.Option(
        "",
        "--creds"
    ),
) -> None:
    """Initialize Standard/Customized Workspace."""
    global tool
    if ctf_url == "":
        try:
            tool.initialize()
        except ConfigException:
            # prompt for user
            response = typer.prompt("This action will delete your current progreess in the the CTF [y/n]")
            if response == 'y':
                # delete config file
                os.remove(_CONFIG_FILE_PATH)
                tool = varnan.Varnan()
                tool.initialize()
            else:
                return
    else:
        if validators.url(ctf_url):
            tool.initialize(ctf_url=ctf_url, creds=creds)
        else:
            print("invalid url")


@app.command()
def link(
    ctf_url: str = typer.Option(
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
    if validators.url(ctf_url):
        tool.link(ctf_url, creds)
    else:
        print("invalid url")


@category_app.command('list')
def list_category() -> None:
    """List all the present CTF Categories in the workspace."""
    tool.list_category()


@category_app.command('add')
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


@task_app.command('list')
def list_task() -> None:
    """List all the present CTF Tasks in the workspace."""
    tool.list_task()


@task_app.command('add')
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
