<!--
.. title: Setup FTP server on Mac OS X
.. slug: how-to-setup-ftp-server-on-mac-os
.. date: 2024-04-30 23:34:14 UTC+05:30
.. tags: python, ftp, macbook
.. category: programming
.. link: 
.. description: How to set up FTP server on Mac OS X, Linux & Windows using Python without root privileges.
.. type: text
-->

<div class="embed-responsive embed-responsive-16by9">
<iframe class="embed-responsive-item" src="https://www.youtube.com/embed/WmmB-6MXRYc" allowfullscreen>
</iframe>
</div>

<br />

On Linux & Mac OS X, Python comes pre-installed. On Windows, we can install it from Windows store or from [https://python.org](https://python.org) website.

We can verify the Python version using the below command.

```bash
$ python --version
Python 3.11.6
```

We can use the `pyftpdlib` library to create an FTP server. We can install the library using the below command.

```bash
$ python -m pip install pyftpdlib
[I 11:28:21] concurrency model: async
[I 11:28:21] masquerade (NAT) address: None
[I 11:28:21] passive ports: None
[I 11:28:21] >>> starting FTP server on :::2121, pid=99951 <<<
```

Now, we can start the FTP server using the below command.

```bash
$ python -m pyftpdlib
```

It will start the FTP server on port 2121. We can connect to the FTP server using the below command.

```bash
$ ftp localhost 2121
```
