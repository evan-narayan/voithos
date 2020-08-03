""" Manage the local Pip package service """


import click
import voithos.lib.service.pip as pip


@click.option("--ip", "ip_address", default="0.0.0.0", help="[optional] bind IP address")
@click.option("--port", default="3141", help="[optional] bind port (default 3141)")
@click.command()
def start(ip_address, port):
    """ Launch the local Pip server """
    pip.start(ip_address, port)


def get_pip_group():
    """ return the pip group function """

    @click.group(name="pip")
    def pip_group():
        """ Local pip service """

    pip_group.add_command(start)
    return pip_group
