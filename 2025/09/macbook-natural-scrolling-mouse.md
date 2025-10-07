<!--
.. title: MacBook - Natural Scrolling for Mouse
.. slug: macbook-natural-scrolling-mouse
.. date: 2025-09-30 23:50:58 UTC+05:30
.. tags: macbook, how-to
.. category: programming
.. link:
.. description: How to seperate trackpad and mouse natural scrolling settings on macOS
.. type: text
-->

### Problem

If we connect a mouse to macOS, the scrolling direction changes to "unnatural" for the mouse. 
This is because macOS has a single setting for natural scrolling that applies to both trackpad and mouse.

![macos mouse settings](/images/macos-mouse-natural-scrolling00.png)

### Solution

To have natural scrolling for both trackpad and mouse, we can use third-party tools like 
[UnnaturalScrollWheels](https://github.com/ther0n/UnnaturalScrollWheels).

If we already use [Karabiner-Elements](https://karabiner-elements.pqrs.org/), we can use it to set natural scrolling for mouse separately.

Open Karabiner-Elements and go to the "Devices" tab, select your mouse, and click on "Open mouse settings".

![Karabiner-Elements Devices Tab](/images/macos-mouse-natural-scrolling11.png)

In the mouse settings, check the "Flip mouse vertical wheel" option.

![Karabiner-Elements Devices Tab](/images/macos-mouse-natural-scrolling22.png)

Now, both trackpad and mouse will have natural scrolling.

