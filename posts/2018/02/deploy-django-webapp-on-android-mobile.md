<!--
.. title: Running Django Web Apps On Android Devices
.. slug: deploy-django-web-app-android
.. date: 2018-02-19 17:40:56 UTC+05:30
.. tags: python, django, android
.. category:
.. link:
.. description: How to run python and django web applications on android mobiles or tablets?
.. type: text
-->

When deploying a django webapp to Linux servers, Nginx/Apache as server, PostgreSQL/MySQL as database are preferred. For this tutorial, we will be using django development server with SQLite database.

First install [SSHDroid](https://play.google.com/store/apps/details?id=berserker.android.apps.sshdroid) app on Android. It will start ssh server on port 2222. If android phone is rooted, we can run ssh on port 22.

Now install [QPython](https://play.google.com/store/apps/details?id=org.qpython.qpy). This comes bundled with pip, which will install required python packages.

Instead of installing these two apps, we can use [Termux](https://github.com/termux/termux-app/), [GNURoot Debian](https://github.com/corbinlc/GNURootDebian) or some other app which provides Linux environment in Android. These apps will provide `apt` package manager, which can install `python` and `openssh-server` packages.

I have used [django-bookmarks](https://github.com/ChillarAnand/django-bookmarks), a simple CRUD app to test this setup. We can use rsync or adb shell to copy django project to android.

```sh
rsync -razP django-bookmarks :$USER@$HOST:/data/local/
```

Now ssh into android, install django and start django server.

```sh
$ ssh -v $USER@$HOST
```

```
$ python -m pip install django
$ cd /data/local/django-bookmarks
$ python manage.py runvserver
```

This will start development server on port 8000. To share this webapp with others, we will expose it with [serveo](https://serveo.net/).

```
$ ssh -R 80:localhost:8000 serveo.net

Forwarding HTTP traffic from https://incepro.serveo.net
Press g to start a GUI session and ctrl-c to quit.
```

Now we can share our django app with anyone.

I have used Moto G4 Plus phone to run this app. I have done a quick load test with Apache Bench.

```sh
ab -k -c 50 -n 1000  \
-H "Accept-Encoding: gzip, deflate" \
http://incepro.serveo/list/
```
It is able to server 15+ requests concurrently with an average response time of 800ms.

We can write a simple shell script or ansible playbook to automate this deployment process and we can host a low traffic website on an android phone if required.
