<!--
.. title: Setup Raspberry Pi without Monitor & Keyboard
.. slug: setup-raspberry-pi-without-monitor-keyboard
.. date: 2025-07-31 09:20:56 UTC+05:30
.. tags: raspberry_pi, headless
.. category: programming
.. link: 
.. description: 
.. type: text
-->

### Requirements
- Raspberry Pi (any model)
- MicroSD card (8GB or larger)
- Power supply

### Setup

Download & install Raspberry Pi Imager from [here](https://www.raspberrypi.com/software/).

![![Raspberry Pi Imager]](/images/rpi-setup0.png)

After installation, connect SD Card to Computer, and start installation process.

In the config step, setup WiFi credentials and enable ssh server as well.

![![Raspberry Pi Imager]](/images/rpi-setup.png)

Once the installation is complete, insert the SD card into the Raspberry Pi and power it on.

### Find the IP Address

You can find the IP address of your Raspberry Pi by checking your router's connected devices list or using a network scanning tool like `nmap` or `arp`.

```shell
arp -an

# or using nmap
nmap -sn
```

Once you have the IP address, you can SSH into the Raspberry Pi.

```shell
ssh pi@<IP_ADDRESS>
```

### Conclusion

When we don't have a monitor and/or keyboard, this process allows us to set up a Raspberry Pi headlessly. This is particularly useful for projects where the Pi will be used as a server or in a remote location.
