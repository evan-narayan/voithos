# Local Apt Service

The local Apt service is required for offline/air-gap installations.

## Deploying Apt

```bash
# Show the help
voithos service apt start --help

# Launch the apt service on port 5050, listening on all IPs
voithos service apt start --ip  0.0.0.0 --port 5050
```


## Configure Apt to trust the local package source

When conducting an offline install of OpenStack, this procedure needs to be done on all involved
servers.

Edit your apt sources file. Be sure to replace the `<ip address>:<port>` references with the IP
address and chosen port of your server running the local Apt service.

```
deb [trusted=yes arch=amd64] http://<ip address>:<port> bionic main
deb [trusted=yes arch=amd64] http://<ip address>:<port> bionic-updates main
deb [trusted=yes arch=amd64] http://<ip address>:<port> bionic-security main
```

Now as root, update your apt sources:

```bash
apt-get update
```

