<!--
.. title: Django Tips & Tricks #3 - Hyperlink Foreignkey Fields In Admin
.. slug: django-tips-tricks-hyperlink-foreignkey-fields-in-admin
.. date: 2017-11-15 02:22:59 UTC
.. tags: python, django, django-tips-tricks
.. category: tech, programming, python
.. link:
.. description: Django productivity tips. How to hyperlink foreignkey fields in django admin interface for faster access.
.. type: text
-->

Consider two models which are linked with a foreignkey.

```py
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author)
```

These models can be registered with admin interface as follows.

```py
from django.contrib import admin

from .models import Author, Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', )

admin.site.register(Author)
admin.site.register(Book, BookAdmin)
```

Once they are registed, admin page shows `Book` model like this.

<p align="center">
<img src="/images/django-tips-tricks-1.png" />
</p>


Now to go to coresponding author, we have to previous page, go to `Author` model and then find relevant author. This becomes tedious if we spend lot of time in admin. Instead, author field can be hyperlinked so that we can directly go to its change view.

Django provides an option to [access admin views by its URL](https://docs.djangoproject.com/en/dev/ref/contrib/admin/#reversing-admin-urls) reversing system. For example to get add view of author model in book app, we can do `reverse("admin:book_author_add")`.

To hyperlink author field in book admin, get url from reversing `book_author_change` with its id and return required html.

```
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author_link', )

    def author_link(self, book):
        link = reverse("admin:book_author_change", args=[book.author.id])
        return u'<a href="%s">%s</a>' % (link, book.author.name)
    author_link.allow_tags = True
    author_link.short_description = 'Author'
```

<p align="center">
<img src="/images/django-tips-tricks-2.png" />
</p>

Now in the book admin view, author field will be hyperlinked and we can visit it just by clicking it.
