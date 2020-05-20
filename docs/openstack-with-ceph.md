# OpenStack Online Install with Ceph Storage

This installation procedure is our most common use-case. It requires that
Ceph already be installed. If you haven't installed Ceph yet, follow the
[Ceph install guide](/ceph-install.html) first.


## Prepare Ceph

1. [**Create Ceph OSD pools for OpenStack**](/ceph-pools.html)
1. [**Create Ceph keyring, ceph.conf, glance-api.conf and cinder-volume.conf files**](/openstack-ceph.html)

## Install OpenStack

1. [**Prepare the metal cloud servers**](/openstack-server-setup.html)
1. (optional)
   [**Launch a local Docker registry**](/registry.html) and
   [**Sync Kolla images to it**](/openstack-registry-mirror.html)
1. [**Generate unique passwords for OpenStack service**](/openstack-kolla-passwords.html)
   - Create `passwords.yml`
1. [**Create globals.yml for Kolla-Ansible**](/openstack-kolla-globals.html) - Create `globals.yml`
1. [**Write the inventory file for Kolla-Ansible**](/openstack-kolla-inventory.html)
1. [**Collect or generate HTTPS certificates**](/openstack-kolla-certificates.md)
1. [**Write Kolla-Ansible's config/ files**](/openstack-kolla-config.html)
1. [**Bootstrap the OpenStack servers**](/openstack-kolla-bootstrap.html)
1. [**Pull Docker images to each node**](/openstack-kolla-pull.html)
1. [**Initialize OpenStack's service containers**](/openstack-kolla-deploy.html)
