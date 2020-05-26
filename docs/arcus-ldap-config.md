# Arcus LDAP config

Once OpenStack has been configured to use an Active-Directory LDAP domain, Arcus can automatically
provision projects for users and otherwise support the LDAP domain.


## Create a service account

```bash
openstack user create --password-prompt arcusadmin
```

## Grant the service account roles

- Grant the `admin` role for both the local and AD domains.
- Grant the `admin` and `_member_` role for the default domain's admin project.

```bash
# Local domain
openstack role add --user arcusadmin --domain default admin

# AD Domain (breqwatr.com is an example)
openstack role add --user arcusadmin --domain breqwatr.com admin

# Admin project
openstack role add \
  --user arcusadmin --user-domain default \
  --project admin --project-domain default \
  admin
openstack role add \
  --user arcusadmin --user-domain default \
  --project admin --project-domain default \
  _member_
```

## Update the Arcus DB

Update the arcus.clouds table data to set the service account username and password.

[JSC2F](https://pypi.org/project/jsc2f/) is a general-use tool that was built specifically with
this database table in mind.
