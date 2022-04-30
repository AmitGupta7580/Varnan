import os
import time

import validators
import typer
from typing import List, Optional

from varnan import __app_name__, __version__, varnan
from varnan.category import Category
from varnan.task import Task


app = typer.Typer()
task_app = typer.Typer()
app.add_typer(task_app, name="task", help="Tasks commands")
category_app = typer.Typer()
app.add_typer(category_app, name="category", help="Category commands")


tool = None
_WORKSPACE = os.getcwd() + "\\"
_CONFIG_FILE_PATH = _WORKSPACE + ".varnan_config.xml"


@app.command()
def test() -> None:
    tool.update_workspace()


@app.command()
def init(
    ctf_name: str = typer.Option(
        f"Unnamed_{int(time.time())}", "-n", "--name", prompt="Name of the CTF"
    ),
    ctf_url: Optional[str] = typer.Option("", "--ctf"),
    creds: Optional[str] = typer.Option("", "--creds"),
) -> None:
    """
    Initialize Standard/Customized Workspace.
    """
    global tool

    # simple check for the exsistence of config file
    if tool.configured:
        response = typer.prompt(
            "This action will delete your current progreess in the the CTF [y/n]"
        )
        if response == "y":
            # delete config file
            os.remove(_CONFIG_FILE_PATH)
            tool = varnan.Varnan()
        else:
            return

    if ctf_url == "":
        tool.initialize(ctf_name)
    else:
        if validators.url(ctf_url):  # url validation check
            tool.initialize(ctf_name, ctf_url=ctf_url, creds=creds)
        else:
            print("[-] Invalid url")
            return

    tool.update_workspace()

    # write worspace information to config file
    tool.write_config()


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
    """
    Link a CTF with currnet working workspace.\n
    Warning : This command will delete all files and clean up the workspace.
    """
    global tool

    # simple check for the exsistence of config file
    if tool.configured:
        response = typer.prompt(
            "This action will delete your current progreess in the the CTF [y/n]"
        )
        if response == "y":
            # delete config file
            os.remove(_CONFIG_FILE_PATH)
            tool = varnan.Varnan()
        else:
            return

    if validators.url(ctf_url):  # url validation check
        tool.link(ctf_url, creds)
    else:
        print("[-] Invalid url")
        return

    tool.write_config()


@app.command()
def stats() -> None:
    """
    Show your progress in the CTF
    """
    global tool

    # simple check for the exsistence of config file
    if not tool.configured:
        print("First initialize your workspace.")
        return

    tool.show_stats()


@app.command()
def generate() -> None:
    """
    Generate an overall Writeup for whole CTF.
    """
    global tool

    # simple check for the exsistence of config file
    if not tool.configured:
        print("First initialize your workspace.")
        return

    tool.generate()


@category_app.command("list")
def list_category() -> None:
    """
    List all the present CTF Categories in the workspace.
    """
    global tool

    # simple check for the exsistence of config file
    if not tool.configured:
        print("First initialize your workspace.")
        return

    tool.list_category()


@category_app.command("add")
def add_category(
    category_name: str = typer.Option(
        "Misc",
        "-c",
        "--category",
        prompt="Name of the category",
    )
) -> None:
    """
    Add CTF Category in the workspace
    """
    global tool

    # simple check for the exsistence of config file
    if not tool.configured:
        print("First initialize your workspace.")
        return

    tool.add_category(Category(category_name))

    tool.update_workspace()
    tool.write_config()


@category_app.command("remove")
def remove_category(
    category_name: str = typer.Option(
        "",
        "-c",
        "--category",
        prompt="Name of the category",
    )
) -> None:
    """
    Remove CTF Category in the workspace
    """
    global tool

    # simple check for the exsistence of config file
    if not tool.configured:
        print("First initialize your workspace.")
        return

    tool.remove_category(Category(category_name))

    tool.update_workspace()
    tool.write_config()


@task_app.command("list")
def list_task() -> None:
    """
    List all the present CTF Tasks in the workspace.
    """
    global tool

    # simple check for the exsistence of config file
    if not tool.configured:
        print("First initialize your workspace.")
        return

    tool.list_task()


@task_app.command("add")
def add_task(
    task_name: str = typer.Option(
        "Unnamed",
        "-tn",
        "--task-name",
        prompt="Name of the task",
    ),
    description: str = typer.Option(
        "",
        "-d",
        "--desc",
        prompt="Description of the task",
    ),
    category_name: str = typer.Option(
        "Misc", "-c", "--category", prompt="Category of the task"
    ),
    attatchments: Optional[List[str]] = typer.Option(
        [],
        "-a",
        "--attach",
        help="Attachment URLs of the task",
    ),
    points: Optional[int] = typer.Option(
        0,
        "-p",
        "--points",
        help="Points of the task",
    ),
) -> None:
    """
    Add CTF Task in the workspace
    """
    global tool

    # simple check for the exsistence of config file
    if not tool.configured:
        print("First initialize your workspace.")
        return

    # issue with attachments

    tool.add_task(Task(task_name, description, points, attatchments), category_name)

    tool.update_workspace()
    tool.write_config()


@task_app.command("remove")
def remove_task(
    task_name: str = typer.Option("", "-tn", "--task-name", prompt="Name of the Task"),
    category_name: str = typer.Option(
        "", "-c", "--category", prompt="Category of the task"
    ),
) -> None:
    """
    Remove CTF Task in the workspace.
    """
    global tool

    # simple check for the exsistence of config file
    if not tool.configured:
        print("First initialize your workspace.")
        return

    tool.remove_task(task_name, category_name)

    tool.update_workspace()
    tool.write_config()


@task_app.command("solve")
def solve_task(
    task_name: str = typer.Option(
        "Unnamed",
        "-tn",
        "--task-name",
        prompt="Name of the task",
    ),
    category_name: str = typer.Option(
        "", "-c", "--category", prompt="Category of the task"
    ),
    flag: str = typer.Option(
        "",
        "-f",
        "--flag",
        prompt="Description of the task",
    ),
) -> None:
    """
    Mark CTF Task as solved
    """
    global tool

    # simple check for the exsistence of config file
    if not tool.configured:
        print("First initialize your workspace.")
        return

    # issue with attachments

    tool.solve_task(task_name, category_name, flag)
    tool.write_config()


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

    # fetch configuration of tool from working directory
    if os.path.exists(_CONFIG_FILE_PATH):
        tool.ctf = tool.read_config()
        tool.configured = True

    return
