[Index](/)
\> OpenStack Installation

# OpenStack Installation

There's no one "right" way to install OpenStack. Breqwatr's procedure has
been repeatedly tested, used in production, and enterprise support is
available.

Breqwatr has selected a subset of the OpenStack ecosystem to support
and distribute to ensure that while not every possible service is available,
the supported ones are production-ready at all times.

Currently Breqwatr has standardized on the [Kolla-Ansible](https://github.com/openstack/kolla-ansible)
project and its [Kolla](https://github.com/openstack/kolla)-based images to deploy and manage
OpenStack. Voithos wraps the projects to improve ease-of-use. Breqwatr distributes known-stable
builds Kolla images, with only minor customization such as the introduction of various
Cinder-volume plugins.


Deployment scenarios vary widely. These guides hope to cover the most common
scenarios. For more complicated scenarios Breqwatr offers training,
professional services, support, and managed services - [contact us](mailto:sales@breqwatr.com)
to learn more.


# Installation Procedures

- [**Online Installation with Ceph-backed volumes**](/openstack-with-ceph.html)
- [**Online Installation with LVM-backed volumes**](/openstack-with-lvm.html)
- [**Offline Installation with iSCSI-backed volumes**](/offline-openstack-with-iscsi.html)

---
