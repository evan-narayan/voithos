# Local Docker Registry

The local Docker registry is required for offline/air-gap installations.

While optional for internet-enabled installations,  multi-node clusters benefit
from using a local registry. The registry service acts as a local cache to
prevent downloading tens of gigabytes of image data repeatedly on each cloud
server.

## Deploying Registry

```bash
voithos service registry start --help

# Launch the registry on port 5000, listening on all IPs
voithos service registry start --ip 0.0.0.0 --port 5000
```


## Configure Docker to trust the local registry

**Note**: OpenStack nodes don't need to do this, Kolla-Ansible's bootstrap will modify their
systemd service instead. Making this change on those servers will cause problems.

Before you can sync images to the registry service or pull images from it,
you need to configure the Docker service to trust this registry.

On your deployment server, edit `/etc/docker/daemon.json` with content similar
to the following. Change the IP address and port as appropriate.

```
{
   "insecure-registries" : ["10.10.10.9:5000"]
}
```

Restart the docker service to apply the changes.

```bash
systemctl restart docker
```

At this point you may want to
[mirror the upstream OpenStack images](openstack-registry-mirror.html).


---


## List images in local registry

To list the images currently stored in the local registry:

```bash
voithos service registry list-images <registry ip:port>
```
