<!--
.. title: Detecting USB Events In Ubuntu With Python
.. slug: detecting-device-events-in-ubuntu-with-python
.. date: 2016-09-02 13:24:38 UTC
.. tags: python, linux, usb
.. category: programming
.. link:
.. description: how to detect device events(like USB events) in ubuntu with python
.. type: text
-->

[udev](https://en.wikipedia.org/wiki/Udev) is responsible for managing devices on Linux. It provides `udevadm`, a CLI utility to monitor and control devices.

If we run `udevadm monitor` on terminal and connect a USB drive or hard disk or a mobile via USB to your computer, it will show that kernel has detected the device and it will send a signal to udev about it.

```sh
→ udevadm monitor
monitor will print the received events for:
UDEV - the event which udev sends out after rule processing
KERNEL - the kernel uevent

KERNEL[4336.899091] add      /devices/pci0000:00/0000:00:14.0/usb1/1-2 (usb)
KERNEL[4336.899774] add      /devices/pci0000:00/0000:00:14.0/usb1/1-2/1-2:1.0 (usb)
KERNEL[4336.902553] add      /devices/pci0000:00/0000:00:14.0/usb1/1-2/1-2:1.1 (usb)
UDEV  [4336.911201] add      /devices/pci0000:00/0000:00:14.0/usb1/1-2 (usb)
UDEV  [4336.936453] add      /devices/pci0000:00/0000:00:14.0/usb1/1-2/1-2:1.1 (usb)
UDEV  [4337.947174] add      /devices/pci0000:00/0000:00:14.0/usb1/1-2/1-2:1.0 (usb)
```

[Pyudev](https://pypi.python.org/pypi/pyudev), a third party package provides python bindings for udev. It can be installed with `pip install pyudev`.

With this we can create a simple monitor to detect USB events.

```py
import pyudev

context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='usb')

for device in iter(monitor.poll, None):
    if device.action == 'add':
        print('{} connected'.format(device))
        # do something
```

Save this to a file say monitor.py and run it with `python monitor.py` and connect a mobile or pendrive and it will show something like this.

```sh
Device('/sys/devices/pci0000:00/0000:00:14.0/usb1/1-6/1-6:1.0') connected
Device('/sys/devices/pci0000:00/0000:00:14.0/usb1/1-1/1-1:1.0') connected
```

Here we are just detecting `add` event. Similary we can detect other events like `delete`.

This is useful for automatically running shell scripts once the device gets plugged or unplugged.
