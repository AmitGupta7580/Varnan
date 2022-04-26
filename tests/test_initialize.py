from typer.testing import CliRunner

from varnan.ctf import StandardCTF
from varnan.varnan import Varnan

runner = CliRunner()

def test_initialize_standard_ctf():
    '''
    For Standard CTF
    '''
    tool= Varnan()
    tool.initialize("Test CTF")
    assert isinstance(tool.ctf, StandardCTF)
    assert len(tool.ctf.categories) == 4
    assert tool.ctf.name == "Test CTF"

def test_initialize_custom_ctf():
    pass