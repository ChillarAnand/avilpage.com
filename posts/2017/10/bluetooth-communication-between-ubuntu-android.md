<!--
.. title: Bluetooth Serial Communication Between Ubuntu & Android
.. slug: bluetooth-communication-between-ubuntu-android
.. date: 2017-10-03 14:53:04 UTC
.. tags: android, bluetooth, ubuntu
.. category: tech, how-to
.. link:
.. description: How to do bluetooth serial communication from ubuntu laptop to android smart phone or bluetooth device like HC-05
.. type: text
-->

Most laptops and smart phones(Android/iPhone) have builtin Bluetooth modules. We can use this bluetooth module to communicate with each other or with other bluetooth modules like HC-05 or HM-10.

In this article, we will learn how to send data between laptop and android bluetooth.

First, we need to pair with a bluetooth device to send information. From Ubuntu, we can pair to a Bluetooth device from Bluetooth settings. Alternatively, we can also use CLI to do the same.

```
$ bluetoothctl
[NEW] Controller 24:0A:64:D7:99:AC asus [default]
[NEW] Device 94:E9:79:BB:F8:3A DESKTOP-C4ECO3K
[NEW] Device 88:79:7E:7B:4C:87 athene
[NEW] Device 94:65:2D:8C:2E:10 OnePlus 5
[NEW] Device 98:0C:A5:61:D5:64 Lenovo VIBE K5 Plus
[NEW] Device AC:C3:3A:A0:CE:EF Galaxy J2
[NEW] Device 98:D3:35:71:02:B3 HC-05

[bluetooth]# power on
Changing power on succeeded

[bluetooth]# agent on
Agent registered

[bluetooth]# default-agent
Default agent request successful

[bluetooth]# scan on
Discovery started
[CHG] Controller 24:0A:64:D7:99:AC Discovering: yes
[CHG] Device 94:E9:79:BB:F8:3A RSSI: -88
[CHG] Device 88:79:7E:7B:4C:87 RSSI: -66

[bluetooth]# pair 88:79:7E:7B:4C:87
Attempting to pair with 88:79:7E:7B:4C:87
[CHG] Device 88:79:7E:7B:4C:87 Paired: yes
Pairing successful
```

To communicate with paired devices, we will use [RFCOMM protocol](https://en.wikipedia.org/wiki/List_of_Bluetooth_protocols). RFCOMM is just a serial port emulation and provides reliable data tranfer like TCP.

From ubuntu, lets open a port for communication.

```sh
$ sudo rfcomm listen /dev/rfcomm0 3
```

From Android, we have to connect to ubuntu. For this, we can use [Roboremo](https://play.google.com/store/apps/details?id=com.hardcodedjoy.roboremofree&hl=en) app which supports RFCOMM.

```sh
$ sudo rfcomm listen /dev/rfcomm0 3
Waiting for connection on channel 3
Connection from 88:79:7E:7B:4C:87 to /dev/rfcomm0
Press CTRL-C for hangup
```

Once the connection is established, we can communicate between devices.

In Unix like systems, OS provides a device file as an interface for device driver. To send and read messages from Linux or Mac is as easy as reading and writing to a file.

```sh
# to send message to bluetooth
$ echo 'hello from ubuntu' > /dev/rfcomm0
```

We can see the received messages on Android

<p align="center">
<img src="/images/arduino-ubuntu-bluetooth.jpg" >
</p>


We can also send messages from android and read from ubuntu.

```sh
# to read messages from bluetooth
$ cat /dev/rfcomm0
hello from android
```

This way, we can communicate with any bluetooth module using a laptop or a smart phone.
