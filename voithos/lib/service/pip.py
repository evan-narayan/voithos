""" Operate the pip service """

from voithos.lib.system import shell


def start(ip_address, port):
    """ Start the local pip container"""
    shell(f"docker run -d --name pip -p {ip_address}:{port}:3141 breqwatr/pip:stable")
