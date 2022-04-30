import os
import xml.etree.ElementTree as ET
from typer.testing import CliRunner

from varnan.varnan import Varnan
from varnan.ctf import *

runner = CliRunner()


def test_list_task():
    ROOT_DIR = os.getcwd()
    config = ET.parse(os.path.join(ROOT_DIR, "tests/data", "test_config.xml")).getroot()
    platform_cls = globals()[config.find("platform").text]
    tool = Varnan()
    tool.ctf = platform_cls.read_config(config)

    solved_tasks, tasks = tool.list_task()

    assert len(tasks) == 4
    assert solved_tasks == 2


def test_add_task():
    ROOT_DIR = os.getcwd()
    config = ET.parse(os.path.join(ROOT_DIR, "tests/data", "test_config.xml")).getroot()
    platform_cls = globals()[config.find("platform").text]
    tool = Varnan()
    tool.ctf = platform_cls.read_config(config)

    # Task-1
    assert tool.add_task(Task("Web Task 2", "Web Task Description"), "Web")
    assert len(tool.ctf.categories[0].tasks) == 2
    assert tool.ctf.categories[0].tasks[1].name == "Web Task 2"

    # Task-2 (new category as well)
    assert tool.add_task(Task("Pwn Task 1", "Pwn Task Description"), "Pwn")
    assert len(tool.ctf.categories) == 5
    assert len(tool.ctf.categories[-1].tasks) == 1
    assert tool.ctf.categories[-1].tasks[0].name == "Pwn Task 1"


def test_remove_task():
    ROOT_DIR = os.getcwd()
    config = ET.parse(os.path.join(ROOT_DIR, "tests/data", "test_config.xml")).getroot()
    platform_cls = globals()[config.find("platform").text]
    tool = Varnan()
    tool.ctf = platform_cls.read_config(config)

    assert tool.remove_task("Crypto", "Crypto task 2")
    assert len(tool.ctf.categories[1].tasks) == 1


def test_solve_task():
    ROOT_DIR = os.getcwd()
    config = ET.parse(os.path.join(ROOT_DIR, "tests/data", "test_config.xml")).getroot()
    platform_cls = globals()[config.find("platform").text]
    tool = Varnan()
    tool.ctf = platform_cls.read_config(config)

    assert tool.solve_task("Crypto task 2", "Crypto", "flag{fake_flag}")
    assert tool.ctf.categories[1].tasks[1].solved
