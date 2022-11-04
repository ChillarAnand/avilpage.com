<--
.. title: WD My Cloud NAS Setup On Linux
.. slug: wd-my-cloud-nas-setup-on-ubuntu
.. date: 2015-03-17 14:20:00
.. updated: 2022-11-04 14:20:00
.. category: tech
.. tags: ubuntu, linux, command-line
.. description: How to set up personal network attached storage device on ubuntu or linux machines.
-->

### Introduction

I recently bought a WD My Cloud NAS[^nas] device to store my personal data. I wanted to set it up on my Ubuntu machine. For WD My Cloud, there is no official support for Ubuntu or any other Linux distros. But setting up it is quite easy.


### NAS Setup

Make sure You have connected power adapter & LAN cables to it. If You open Your router config, You will see WD My cloud in client list. Make note of its IP address. If You want, You can assign a static IP also in the router settings.

Next step is to install NFS client package. NFS(Network File System) allows a system to share directories and files with others over a network. By using NFS, users and programs can access files on remote systems almost as if they were local files. So, update your packages & install `nfs-common` package.

```bash
$ sudo apt-get update
$ sudo apt-get install nfs-common
```

Now we can list folders which are available to mount using `showmount` command.

```bash
$ showmount -e <ip-address>
```

Create an empty folder to mount any of the folder you wanted and mount it.

```bash
$ sudo mount -o rw,soft,intr,nfsvers=3 <ip>:<folder-to-mount> <path-to-mount>
```

Now You can start moving data into/out of WD My Cloud.

If You want to mount it automatically on boot, add following line to `/etc/fstab` file.

```bash
<ip>:<folder-to-mount> <path-to-mount> nfs rw,soft,intr,nfsvers=3 0 0
```

### Conclusion

Even though there is no official support for Ubuntu, WD My Cloud works pretty well with Ubuntu and other Linux distros. 


[^nas]: [https://en.wikipedia.org/wiki/Network-attached_storage](https://en.wikipedia.org/wiki/Network-attached_storage)