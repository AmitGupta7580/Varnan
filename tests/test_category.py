import os
import xml.etree.ElementTree as ET
from typer.testing import CliRunner

from varnan.varnan import Varnan
from varnan.ctf import *

runner = CliRunner()
ROOT_DIR = os.getcwd()


def test_add_category():
    config = ET.parse(os.path.join(ROOT_DIR, "tests/data", "test_config.xml")).getroot()
    platform_cls = globals()[config.find("platform").text]
    tool = Varnan()
    tool.ctf = platform_cls.read_config(config)

    # adding test category and task to the ctf class
    tool.add_category(
        Category(
            "Test Category",
            [
                Task("Test Task 1", "Test Task Description 1"),
                Task("Test Task 2", "Test Task Description 2", points=350, solved=True),
            ],
        )
    )


def test_remove_category():
    pass
