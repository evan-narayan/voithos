# Installing Arcus

Arcus is ran as a few Docker containers. Deploy Voithos to install Arcus.

## Apply license key

Voithos can't download Arcus without the license

```bash
voithos config license --set <license>
```

## Collect Information

RabbitMQ password:

```bash
cat passwords.yml | grep rabbitmq_password
```

Database root password:

```bash
cat passwords.yml | grep ^database
```



## Arcus API

Arcus API (arcus-api)is the orchestration agent that operates against OpenStack Ceph, and other
private cloud services.

Initialize the database

```
voithos service arcus api database-init \
  --arcus-pass <password to set for the arcus database user> \
  --admin-pass <database password from passwords.yml> \
  --admin-user root \
  --host <internal vip>
```

Pull the image from Breqwatr's private registry

```bash
voithos service arcus api pull --release 7.5
```

Start the service

```bash
voithos service arcus api start --help
```


### LDAP Config

If Active Directory LDAP will be used, follow the [Arcus LDAP config guide](/arcus-ldap-config.html).



## Arcus Manager

Arcus Manager (arcus-mgr) is a distributed task-runner that operates Arcus's periodic automation.

Pull the image from Breqwatr's private registry

```bash
voithos service arcus mgr pull --release 7.5
```

Launch the arcus-mgr service

```bash
voithos service arcus mgr start --help
```


## Arcus Client

Arcus Client (arcus-client) is the web UI built to leverage the Arcus API.


Pull the image from Breqwatr's private registry

```bash
voithos service arcus client pull --release 7.5
```

Start the client

```bash
voithos service arcus client start --help
```


## Configure the service account

### Create the SA in OpenStack

This requires that the openstack client be set up somewhere, and assumes you have an openrc
file located at `/etc/kolla/admin-openrc.sh`. Adjust accordingly.

```bash
openstack user create arcusadmin --password <service account password>
openstack role add --user arcusadmin --project admin admin
openstack role add --user arcusadmin --project admin _member_
openstack role add --user arcusadmin --domain default admin
```

### Set the SA in Arcus

```bash
voithos service arcus api set-service-account \
  --api-url https://<external vip>/api \
  --username arcusadmin \
  --password <password> \
  --auth-url https://<external vip/fqdn>:5000/v3
```
