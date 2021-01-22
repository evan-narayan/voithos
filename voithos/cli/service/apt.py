""" Manage the local Apt package service """


import click
import voithos.lib.service.apt as apt


@click.option("--ip", "ip_address", default="0.0.0.0", help="[optional] bind IP address")
@click.option("--port", default="80", help="[optional] bind port (default 80)")
@click.option("--tag", default="train", help="[optional] image tag (default train)")
@click.command()
def start(ip_address, port, tag):
    """ Launch the local Apt server """
    apt.start(ip_address, port, tag)


def get_apt_group():
    """ return the apt group function """

    @click.group(name="apt")
    def apt_group():
        """ Local apt service """

    apt_group.add_command(start)
    return apt_group
