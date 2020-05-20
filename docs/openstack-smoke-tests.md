# OpenStack Smoke Tests

This optional tast will deploy some sane defaults to a cloud, allowing manual interactive testing
to ensure that the setup is functional. This can be considered a "post-deploy" step.

It uses many arguments, so take care filling it out.

First, download a cirros image

```bash
wget http://download.cirros-cloud.net/0.5.1/cirros-0.5.1-x86_64-disk.img -O ./cirros.qcow2
```

Run the smoke-test.
```bash
voithos openstack smoke-test --help
```
