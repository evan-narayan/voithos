# OpenStack Online Install with Ceph Storage

This installation procedure is our most common use-case. It requires that
Ceph already be installed. If you haven't installed Ceph yet, follow the
[Ceph install guide](/ceph-install.html) first.


## Prepare Ceph

1. [**Create Ceph OSD pools for OpenStack**](/ceph-pools.html)
1. [**Collect Ceph keyring and ceph.conf files**](/openstack-ceph.html)

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
