<!--
.. title: Django Tips & Tricks #7 - Django Auth Plugin For HTTPie
.. slug: django-auth-plugin-for-httpie
.. date: 2017-04-20 15:00:28 UTC
.. tags: python, django, django-tips-tricks
.. category: tech, programming, python
.. link:
.. description: how to authenticate django web app using httpie?
.. type: text
-->

[HTTPie](https://pypi.python.org/pypi/httpie) is an alternative to curl for interacting with web services from CLI. It provides a simple and intuitive interface and it is handy to send arbitrary HTTP requests while testing/debugging APIs.

When working with web applications that require authentication, using httpie is  difficult as authentication mechanism will be different for different applications. httpie has in built support for `basic` & `digest` authentication.

To authenticate with Django apps, a user needs to make a `GET` request to login page. Django sends login form with a CSRF token. User can submit this form with valid credentials and a session will be initiated.

Establish session manually is boring and it gets tedious when working with multiple apps in multiple environments(development, staging, production).

I have written a plugin called [httpie-django-auth](https://pypi.python.org/pypi/httpie-django-auth) which automates django authentication. It can be installed with pip

```shell
pip install httpie-django-auth
```

By default, it uses `/admin/login` to login. If you need to use some other URL for logging, set `HTTPIE_DJANGO_AUTH_URL` environment variable.

```shell
export HTTPIE_DJANGO_AUTH_URL='/accounts/login/'
```

Now you can send authenticated requests to any URL as

```sh
http :8000/profile -A=django --auth='username:password'
```
