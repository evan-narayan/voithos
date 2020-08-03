""" Tests for Apt service """
from unittest.mock import patch

from click.testing import CliRunner

import voithos.cli.service.apt


def test_apt_group():
    """ test the apt group cli call """
    runner = CliRunner()
    result = runner.invoke(voithos.cli.service.apt.get_apt_group())
    assert result.exit_code == 0


@patch("voithos.lib.service.apt.shell")
def test_apt_start(mock_shell):
    """ test apt start  """
    runner = CliRunner()
    result = runner.invoke(
        voithos.cli.service.apt.start,
        [
            "--port",
            "81"
        ],
        catch_exceptions=False,
    )
    assert mock_shell.call_count == 1
    assert result.exit_code == 0, result.output
