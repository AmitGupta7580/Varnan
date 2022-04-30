import os
import xml.etree.ElementTree as ET
from typer.testing import CliRunner

from varnan.varnan import Varnan
from varnan.ctf import *

runner = CliRunner()
ROOT_DIR = os.getcwd()


def test_show_stats():
    config = ET.parse(os.path.join(ROOT_DIR, "tests/data", "test_config.xml")).getroot()
    platform_cls = globals()[config.find("platform").text]
    tool = Varnan()
    tool.ctf = platform_cls.read_config(config)

    # adding test category and task to the ctf class
    solved_tasks, tasks_cnt, points = tool.show_stats()

    assert solved_tasks == 2
    assert tasks_cnt == 4
    assert points == 750
