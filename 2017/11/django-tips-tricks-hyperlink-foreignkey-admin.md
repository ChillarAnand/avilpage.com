<!--
.. title: Django Tips & Tricks #8 - Hyperlink Foreignkey Fields In Admin
.. slug: django-tips-tricks-hyperlink-foreignkey-admin
.. date: 2017-11-14 21:21:21 UTC
.. tags: python, django, django-tips-tricks
.. category: tech, programming, python
.. link:
.. description: Django productivity tips. How to hyperlink foreignkey fields in django admin interface for faster access.
.. type: text
-->

Consider `Book` model which has `Author` as foreignkey.

```py
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author)
```

We can register these models with admin interface as follows.

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


While browing books, to go to a particular author, we have to previous page, go to `Author` model and then find relevant author. This becomes tedious if we spend lot of time in admin. Instead, if author field has a hyperlink, we can directly go to its page.

Django provides an option to [access admin views by its URL](https://docs.djangoproject.com/en/dev/ref/contrib/admin/#reversing-admin-urls) reversing system. For example, we can get add view of author model in book app from `reverse("admin:book_author_add")`.

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

Now in the book admin view, author field will be hyperlinked and we can visit just by clicking it.

<p align="center">
<img src="/images/django-tips-tricks-2.png" />
</p>


<b>Update:</b>

Django has inbuilt option for this. It provides [`list_display_links`](https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display_links), to control which fields should be linked to change page. So, we can just add author field to it.


```py
from django.contrib import admin

from .models import Author, Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', )
    list_display_links = ('name', 'author',)

admin.site.register(Author)
```

Now, author field will be hyperlinked to its change page.
