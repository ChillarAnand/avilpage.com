<!--
.. title: tailscale: Remote SSH Access to Pi or Any Device
.. slug: tailscale-remote-ssh-raspberry-pi
.. date: 2023-09-25 07:19:54 UTC+05:30
.. tags: devops, command-line
.. category: programming
.. link:
.. description: How to set up tailscale and access raspberry pi remotely anywhere.
.. type: text
-->

I recently started using Raspberry Pi and I wanted to access it when I am outside of home as well. After trying out few solutions, I stumbled upon Tailscale[^tailscale].

Tailscale is a mesh VPN that makes it easy to connect out devices, wherever they are. It is free for personal use and supports all major platforms like Linux, Windows, Mac, Android, iOS, etc.

### Installation

I installed tailscale on Raspberry Pi using the following command.

```bash
$ curl -fsSL https://tailscale.com/install.sh | sh
```

### Setup

Once the installation is done, I run `tailscale up` to start the daemon. This opened a browser window and asked me to log in with email address. After I logged in, I can see all the devices in the tailscale dashboard.

![tailscale dashboard](/images/tailscale-pi.png)

`tailscale` has CLI tool as well and status can be viewed with the following command.

```bash
$ tailscale status
100.81.13.75   m1                    avilpage@  macOS   -
100.12.12.92   rpi1.tailscale.ts.net avilpage@  linux   offline
```

I also set up a cron job to start tailscale daemon on boot.

```bash
$ crontab -e
@reboot tailscale up
```


### Access

Now I can access the device from anywhere using the tailscale IP address. For example, if the IP address is `100.34.2.23`. I can ssh into the device using the following command.

```bash
$ ssh pi@100.81.12.92
```

It also provides DNS names for each device. For example, I can ssh into the device using the following command as well.

```bash
$ ssh pi@raspberry3.tailscale.net
```

### Conclusion

Tailscale is a great tool to access devices remotely. It is easy to set up and works well with Raspberry Pi, Mac & Linux as well.


[^tailscale]: [https://en.wikipedia.org/wiki/Tailscale](https://en.wikipedia.org/wiki/Tailscale)
