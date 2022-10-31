<!--
.. title: Django Tips & Tricks #12 - Automatically Set CSRF Token in Postman
.. slug: django-tips-csrf-token-postman-curl
.. date: 2019-02-28 21:21:21 UTC+05:30
.. tags: python, django, automation
.. category: programming
.. link:
.. description: How to set CSRF token automatically in REST API clients.
.. type: text
-->

### Introduction

Django has inbuilt [CSRF protection][csrf] mechanism for requests via unsafe methods to prevent [Cross Site Request Forgeries][csrf]. When CSRF protection is enabled on AJAX POST methods, `X-CSRFToken` header should be sent in the request.

[Postman][postman] is one of the widely used tool for testing APIs. In this article, we will see how to set csrf token and update it automatically in Postman.


### CSRF Token In Postman

Django sets `csrftoken` cookie on login. After logging in, we can see the csrf token from cookies in the Postman.


<p align="center">
<img src="/images/django-csrf-postman1.png" />
</p>

We can grab this token and set it in headers manually.

<p align="center">
<img src="/images/django-csrf-postman2.png" />
</p>

But this token has to be manually changed when it expires. This process becomes tedious to do it on an expiration basis.

Instead, we can use Postman scripting feature to extract token from cookie and set it to an environment variable. In `Test` section of postman, add these lines.

```js
var xsrfCookie = postman.getResponseCookie("csrftoken");
postman.setEnvironmentVariable('csrftoken', xsrfCookie.value);
```

This extracts csrf token and sets it to an environment variable called `csrftoken` in the current environment.

<p align="center">
<img src="/images/django-csrf-postman3.png" />
</p>

Now in our requests, we can use this variable to set the header.

<p align="center">
<img src="/images/django-csrf-postman4.png" />
</p>

When the token expires, we just need to login again and csrf token gets updated automatically.


### Conclusion

In this article we have seen how to set and renew csrftoken automatically in Postman. We can follow similar techniques on other API clients like CURL or httpie to set csrf token.

[csrf]: https://en.wikipedia.org/wiki/Cross-site_request_forgery
[csrfp]: https://docs.djangoproject.com/en/dev/ref/csrf/
[postman]: https://www.getpostman.com
