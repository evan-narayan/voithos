# Local Pip Service

The local Pip service is required for offline/air-gap installations.

## Deploying Apt

```bash
# Show the help
voithos service pip start --help

# Launch the pip service on port 3141, listening on all IPs
voithos service pip start --ip  0.0.0.0 --port 3141
```


## Configure Servers to use local Pip


`vi /etc/pip.conf`

```
# /etc/pip.conf

[global]
trusted-host = <IP>
index-url = http://<IP>:<port>/root/pypi/+simple/

[search]
index = http://<IP>:<port>/root/pypi/
```

