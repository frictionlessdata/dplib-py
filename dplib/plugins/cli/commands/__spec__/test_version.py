from typer.testing import CliRunner

from dplib import __version__
from dplib.plugins.cli.commands.main import program

runner = CliRunner()


def test_program_version():
    result = runner.invoke(program, "version")
    assert result.exit_code == 0
    assert result.stdout.count(__version__)
