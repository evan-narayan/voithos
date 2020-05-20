# Pulling Kolla Docker Images to All Servers

Each of the services which make up OpenStack are containerized by Breqwatr using the Kolla project,
and available on Docker Hub.

This command will download each Docker image to the appropriate OpenStack servers. Kolla-Ansible's
"deploy" task can also do pull the images, but pulling them ahead of time helps identify any
missing images without getting stuck with a half-deployed cloud.

```bash
voithos openstack kolla-ansible pull \
  --release stein \
  --ssh-private-key-file ~/.ssh/id_rsa \
  --globals-file globals.yml \
  --passwords-file passwords.yml \
  --inventory-file inventory \
  --certificates-dir certificates
```
