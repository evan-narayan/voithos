# Generate admin-openrc.sh
The admin-openrc file is used to authenticate as the default administrative
service account in OpenStack. This account is used to bootstrap other services
and create the initial regular users.

```bash
# creates ./admin-openrc.sh
voithos openstack get-admin-openrc \
  --release train \
  --globals globals.yml \
  --passwords passwords.yml \
  --inventory inventory
```

To use this file, execute `source admin-openrc` prior to running the openstack
command line commands.

---

## Suggestion

It's a good idea to SCP this file to the control nodes of your cluster. It will make working on
OpenStack easier. By convention Breqwatr likes to place it in `/etc/kolla/` on each control node
server.
