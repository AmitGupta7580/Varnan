import os
import xml.etree.ElementTree as ET
from typer.testing import CliRunner

from varnan.varnan import Varnan
from varnan.ctf import *

runner = CliRunner()

def test_show_stats():
    ROOT_DIR = os.getcwd()
    config = ET.parse(os.path.join(ROOT_DIR, 'tests/data', 'test_config.xml')).getroot()
    platform_cls = globals()[config.find('platform').text]
    tool = Varnan()
    tool.ctf = platform_cls.read_config(config)
    tool.show_stats()