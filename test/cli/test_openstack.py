""" Tests for openstack cli """
from unittest.mock import patch
from click.testing import CliRunner

import voithos.cli.openstack


def test_openstack_group():
    """ test the openstack group cli call """
    runner = CliRunner()
    result = runner.invoke(voithos.cli.openstack.get_openstack_group(), catch_exceptions=False)
    assert result.exit_code == 0


@patch("voithos.lib.openstack.shell")
def test_openstack_get_passwords(mock_shell):
    """ test generating passwords """
    runner = CliRunner()
    result = runner.invoke(
        voithos.cli.openstack.get_passwords, ["--release", "train"], catch_exceptions=False
    )
    assert result.exit_code == 0
    assert mock_shell.call_count == 1


@patch("voithos.lib.openstack.shell")
def test_openstack_get_inventory_template(mock_shell):
    """ test generating inventory """
    runner = CliRunner()
    result = runner.invoke(
        voithos.cli.openstack.get_inventory_template, ["--release", "train"], catch_exceptions=False
    )
    assert result.exit_code == 0
    assert mock_shell.call_count == 1


@patch("voithos.lib.docker.assert_path_exists")
@patch("voithos.lib.openstack.shell")
def test_openstack_get_certificates(mock_shell, mock_assert):
    """ test generating certs """
    runner = CliRunner()
    result = runner.invoke(
        voithos.cli.openstack.get_certificates,
        ["--release", "train", "--passwords", "passwords.yml", "--globals", "globals.yml"],
        catch_exceptions=False,
    )
    assert result.exit_code == 0
    assert mock_shell.called
    assert mock_assert.called


@patch("voithos.lib.openstack.shell")
def test_openstack_get_globals_template(mock_shell):
    """ test generating certs """
    runner = CliRunner()
    result = runner.invoke(
        voithos.cli.openstack.get_globals_template, ["--release", "train"], catch_exceptions=False
    )
    assert result.exit_code == 0
    assert mock_shell.called


@patch("voithos.lib.docker.assert_path_exists")
@patch("voithos.lib.openstack.shell")
def test_openstack_get_admin_openrc(mock_shell, mock_assert):
    """ test generating admin-openrc file """
    runner = CliRunner()
    result = runner.invoke(
        voithos.cli.openstack.get_admin_openrc,
        [
            "--passwords",
            "passwords.yml",
            "--globals",
            "globals.yml",
            "--release",
            "train",
            "--inventory",
            "inventory",
        ],
        catch_exceptions=False,
    )
    assert result.exit_code == 0, result.output
    assert mock_shell.called
    assert mock_assert.called


@patch("voithos.lib.docker.assert_path_exists")
@patch("voithos.lib.openstack.shell")
def test_openstack_cli(mock_shell, mock_assert):
    """ test openstack cli """
    runner = CliRunner()
    result = runner.invoke(
        voithos.cli.openstack.cli,
        ["--release", "train", "--openrc", "admin-openrc.sh"],
        catch_exceptions=False,
    )
    assert result.exit_code == 0, result.output
    assert mock_shell.called
    assert mock_assert.called


@patch("voithos.lib.docker.assert_path_exists")
@patch("voithos.lib.openstack.shell")
def test_openstack_kolla_ansible(mock_shell, mock_assert):
    """ test running kolla-ansible """
    runner = CliRunner()
    result = runner.invoke(
        voithos.cli.openstack.kolla_ansible,
        [
            "--release",
            "train",
            "--ssh-key",
            "id_rsa",
            "--inventory",
            "inventory",
            "--passwords",
            "passwords.yml",
            "--globals",
            "globals.yml",
            "--certificates",
            "certificates/",
            "--config",
            "config/",
            "deploy",
        ],
        catch_exceptions=False,
    )
    assert result.exit_code == 0, result.output
    assert mock_shell.called
    assert mock_assert.called


@patch("voithos.lib.openstack.shell")
def test_sync_local_registry(mock_shell):
    """ test running local registry sync """
    runner = CliRunner()
    result = runner.invoke(
        voithos.cli.openstack.sync_local_registry,
        ["--release", "train", "--keep", "registry.example.com:5000"],
        catch_exceptions=False,
    )
    assert result.exit_code == 0, result.output
    assert mock_shell.called


def test_image_group():
    """ test the image group cli call """
    runner = CliRunner()
    result = runner.invoke(voithos.cli.openstack.get_image_group(), catch_exceptions=False)
    assert result.exit_code == 0, result.output


@patch("voithos.lib.openstack.s3")
def test_image_download(mock_s3):
    """ test running image download"""
    runner = CliRunner()
    result = runner.invoke(
        voithos.cli.openstack.download_image, ["--image", "windows2019"], catch_exceptions=False,
    )
    assert result.exit_code == 0, result.output
    assert mock_s3.download.called
