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
    assert tool.add_category(
        Category(
            "Test Category",
            [
                Task("Test Task 1", "Test Task Description 1"),
                Task("Test Task 2", "Test Task Description 2", points=350, solved=True),
            ],
        )
    )

    assert len(tool.ctf.categories) == 5
    assert tool.ctf.categories[-1].name == "Test Category"
    assert len(tool.ctf.categories[-1].tasks) == 2


def test_remove_category():
    config = ET.parse(os.path.join(ROOT_DIR, "tests/data", "test_config.xml")).getroot()
    platform_cls = globals()[config.find("platform").text]
    tool = Varnan()
    tool.ctf = platform_cls.read_config(config)

    # removing last indexed category
    test_category = tool.ctf.categories[-1]

    assert tool.remove_category(test_category)
    assert len(tool.ctf.categories) == 3
