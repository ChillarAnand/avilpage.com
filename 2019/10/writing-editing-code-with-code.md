<!--
.. title: Writing & Editing Code With Code - Part 1
.. slug: writing-editing-code-with-code
.. date: 2019-10-31 21:21:21 UTC+05:30
.. tags: metaprogramming, python
.. category:
.. link:
.. description:
.. type: text
-->

In Python community, metaprogramming is often used in conjunction with metaclasses. In this article, we will learn about metaprogramming, where programs have the ability to treat other programs as data.


### Metaprogramming

When we start writing programs that write programs, it opens up a lot of possibilities. For example, here is a metaprogramme that generates a program to print numbers from 1 to 100.

```python
with open('num.py', 'w') as fh:
    for i in range(100):
        fh.write('print({})'.format(i))
```

This 3 lines of program generates a hundred line of program which produces the desired output on executing it.

This is a trivial example and is not of much use. Let us see practical examples where metaprogramming is used in Django for admin, ORM, inspectdb and other places.


### Metaprogramming In Django

Django provides a management command called `inspectdb` which generates Python code based on SQL schema of the database.

```sh
$ ./manage.py inspectdb

from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    ...
```


In django admin, models can be registered like this.

```python
from django.contrib import admin

from book.models import Book


admin.site.register(Book)
```

Eventhough, we have not written any HTML, Django will generate entire CRUD interface for the model in the admin. Django Admin interface is a kind of metaprogramme which inspects a model and generates a CRUD interface.

Django ORM generates SQL statements for given ORM statements in Python.

```python
In [1]: User.objects.last()
SELECT "auth_user"."id",
       "auth_user"."password",
       "auth_user"."last_login",
       "auth_user"."is_superuser",
       "auth_user"."username",
       "auth_user"."first_name",
       "auth_user"."last_name",
       "auth_user"."email",
       "auth_user"."is_staff",
       "auth_user"."is_active",
       "auth_user"."date_joined"
  FROM "auth_user"
 ORDER BY "auth_user"."id" DESC
 LIMIT 1


Execution time: 0.050304s [Database: default]

Out[1]: <User: anand>
```


Some frameworks/libraries use metaprogramming to solve problems realted to generating, modifying and transforming code.

We can also use these techniques in everyday programming. Here are some use cases.

1. Generate REST API automatically.
2. Automatically generate unit test cases based on a template.
3. Generate integration tests automatically from the network traffic.

These are a some of the things related to web development where we can use metaprogramming techniques to generate/modify code. We will learn more about this in the next part of the article.
