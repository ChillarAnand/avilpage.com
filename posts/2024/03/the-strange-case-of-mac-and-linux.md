<!--
.. title: The Strange Case of Dr. Linux and Mr. Mac
.. slug: the-strange-case-of-mac-and-linux
.. date: 2024-03-30 09:53:53 UTC+05:30
.. tags: macbook, git, linux
.. category: programming 
.. link: 
.. description: Linux is case-sensitive, Mac is case-insensitive. This can cause issues when working on a project with developers using different OS. 
.. type: text
-->

Few days back, some of the tests started failing on CI server. When I tried to run the tests locally, they were passing.

After debugging for a while, I found that the tests were failing because of the case sensitivity of the file system. One of the developer was using Linux and had committed 2 files with the same name but different case(`config.json`, `Config.json`).

Linux file system is case-sensitive. So these 2 files will be shown as 2 different files.

![linux-file-system](/images/linux-git-case-sensitive.png)


But Mac/Windows file system is case-insensitive. Out of these 2 files, only one file will be shown.

![mac-file-system](/images/mac-git-case-insensitive.png)

Due to this, the tests were failing on Linux but passing on Mac. Once the case of the file was corrected, the tests started passing on both the systems.

I have been using Mac for a long time and never faced this issue. Even though Mac's APFS is case-insensitive, we can create a case-sensitive volume using Disk Utility. 

![case-sensitive-volume](/images/mac-case-sensitive-volume.png)

We have to be aware of these differences when working on a project with developers using different OS.
