import os
import xml.etree.ElementTree as ET
from typer.testing import CliRunner

from varnan.varnan import Varnan
from varnan.ctf import *

runner = CliRunner()


def test_add_task():
    ROOT_DIR = os.getcwd()
    config = ET.parse(os.path.join(ROOT_DIR, "tests/data", "test_config.xml")).getroot()
    platform_cls = globals()[config.find("platform").text]
    tool = Varnan()
    tool.ctf = platform_cls.read_config(config)


def test_remove_task():
    pass


def test_solve_task():
    pass
