<!--
.. title: Install Cockpit on Remote Linux VM
.. slug: install-cockpit-on-remote-linux-vm
.. date: 2024-12-31 04:24:07 UTC+05:30
.. tags: linux, productivity
.. category: DevOps
.. link: 
.. description: How to easily manage Linux servers using Cockpit web interface(like cPanel).
.. type: text
-->


### Introduction

![Cockpit](/images/cockpit-how-to.png)

Cockpit is an easy to use web-based interface(like a cPanel) for managing Linux servers. When we want to provide access to non-developers or people who are new to linux, it is a good idea to get them started with Cockpit. It provides a user-friendly interface to manage services, containers, storage, logs, and more.

### Setup

Let's create a new Ubuntu VM and install Cockpit on it.

```bash
sudo apt update
. /etc/os-release
sudo apt install -t ${VERSION_CODENAME}-backports cockpit
```

Once the installation is complete, we can get the public ip of the VM and access the Cockpit web interface running on port 9090.

It will be difficult to remember the public ip of the VM. So, let's create a DNS record for the VM. Let's add an `A` record in DNS settings to point `cockpit.avilpage.com` to the public ip of the VM.

### Reverse Proxy

Let's set up a reverse proxy to access the Cockpit web interface using a subdomain.

```bash
sudo apt install caddy
```

Add the below configuration to `/etc/caddy/Caddyfile`.

```bash
cockpit.avilpage.com {
    reverse_proxy localhost:9090
}
```

We need `Origins` to Cockpit configuration at `/etc/cockpit/cockpit.conf` to allow requests from the subdomain.

```bash
[WebService]
Origins = https://cockpit.avilpage.com
```

Restart both services and open [https://cockpit.avilpage.com](https://cockpit.avilpage.com) in browser.

```bash
sudo systemctl restart cockpit
sudo systemctl restart caddy
```

### Conclusion

Cockpit web UI is a great tool to manage Linux servers even for non-developers. Users can browse/manage logs, services, etc. It also provides a terminal to run commands on the server
