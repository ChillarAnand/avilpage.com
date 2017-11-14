<!--
.. title: Remove Clock From LockScreen/StatusBar On Android
.. slug: remove-clock-lock-screen-status-bar-android
.. date: 2016-09-15 13:24:38 UTC
.. tags:
.. category: tech, android
.. link:
.. description: How to remove/hide date and time from lock screen and status bar on android phones
.. type: text
-->

I have been living without time from a few years and it is a bliss. I have removed time from my laptop. For android mobile, I couldn't find a reliable way to remove time and I used to change timezone to a random zone. With Xposed framework we can remove clock from lock screen and status bar.

Before proceeding, make sure your phone is [rooted][] and [Xposed framework][xposed] is installed.

### Remove Clock From LockScreen

To remove clock from lockscreen, download [Lock screen widgets][lsw] module and activate it.

If you open it, it has an option to hide date and time.

<p align="center">
<img src="/remove_clock_android/remove_clock_anrdoid_0.png" height="400px" width="220" />
</p>


### Remove Time From StatusBar
To remove clock from status bar, you have to install [GravityBox][]. Open GravityBox and goto statusbar settings

<p align="center">
<img src="/remove_clock_android/remove_clock_anrdoid_3.png" height="400px" width="220" />
</p>

<p align="center">
<img src="/remove_clock_android/remove_clock_anrdoid_4.png" height="400px" width="220" />
</p>

<p align="center">
<img src="/remove_clock_android/remove_clock_anrdoid_5.png" height="400px" width="220" />
</p>



If you are already using CyanogenMod, there is an option to hide time in settings.

<p align="center">
<img src="/remove_clock_android/remove_clock_anrdoid_1.png" height="400px" width="220" />
</p>

<p align="center">
<img src="/remove_clock_android/remove_clock_anrdoid_2.png" height="400px" width="220" />
</p>

Once you do this, you will have a neat lockscreen without any time on it.

<p align="center">
<img src="/remove_clock_android/remove_clock_anrdoid_6.png" height="400px" width="220" />
</p>

[GravityBox]: http://repo.xposed.info/module/com.ceco.marshmallow.gravitybox
[xposed]: http://repo.xposed.info/module/de.robv.android.xposed.installer
[rooted]: http://www.xda-developers.com/root/
[lsw]: http://repo.xposed.info/module/com.ssrdroide.lockscreenwidgets
