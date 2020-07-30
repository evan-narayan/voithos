""" Operate the apt service """

from voithos.lib.system import shell


def start(ip_address, port):
    """ Start the local apt container"""
    shell(f"docker run -d --name apt -p {ip_address}:{port}:80 breqwatr/apt:stable")
