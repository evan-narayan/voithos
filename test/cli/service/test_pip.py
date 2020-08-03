""" Tests for Pip service """
from unittest.mock import patch

from click.testing import CliRunner

import voithos.cli.service.pip


def test_apt_group():
    """ test the pip group cli call """
    runner = CliRunner()
    result = runner.invoke(voithos.cli.service.pip.get_pip_group())
    assert result.exit_code == 0


@patch("voithos.lib.service.pip.shell")
def test_pip_start(mock_shell):
    """ test pip start  """
    runner = CliRunner()
    result = runner.invoke(
        voithos.cli.service.pip.start,
        [
            "--port",
            "81"
        ],
        catch_exceptions=False,
    )
    assert mock_shell.call_count == 1
    assert result.exit_code == 0, result.output
