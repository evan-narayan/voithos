# Generate admin-openrc.sh
The admin-openrc file is used to authenticate as the default administrative
service account in OpenStack. This account is used to bootstrap other services
and create the initial regular users.

```bash
# creates ./admin-openrc.sh
voithos openstack get-admin-openrc \
  --release train \
  --globals-file globals.yml \
  --passwords-file passwords.yml \
  --inventory-file inventory
```

To use this file, execute `source admin-openrc` prior to running the openstack
command line commands.

This file can also be used within BWDT's [containerized command-line](/openstack-cli.html)
