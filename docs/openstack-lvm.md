# OpenStack LVM Storage Setup

## Create LVM Volume Group

Choose a volume group name. By default, we use `cinder-volumes`.

Configure the volume group on each OpenStack cinder-volume node.

```bash
# List your drives
fdisk -l

# Identify the drive to be used. Example: /dev/sdb

# Create a phsical volume in LVM
pvcreate /dev/sdb

# Confirm the physical volume was created by listing them
pvdisplay

# Create the volume group
vgcreate cinder-volumes /dev/sdb

# Confirm the volume group was created
vgdisplay
```

Later, after volumes for VMs have been created, you can see them in LVM as
logical volumes.

```bash
lvdisplay cinder-volumes
```


## Configure Nova-Compute servers

On each nova-compute node, iSCSI is needed to mount the images.

### Load ConfigFS

```bash
modprobe configfs
```
Also add the configfs module to /etc/modules.

Rebuild initramfs

```bash
update-initramfs -u
```

Confirm the service is running

```bash
systemctl status sys-kernel-config.mount
```

Confirm the mount is present

```bash
mount | grep /sys/kernel/config
```


### Disable iscsid on the host

```bash
systemctl stop open-iscsi
systemctl disable  open-iscsi
```



