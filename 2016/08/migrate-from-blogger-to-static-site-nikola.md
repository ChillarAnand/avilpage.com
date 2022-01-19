<!--
.. title: Migrate From Blogger To Static Site (Nikola)
.. slug: migrate-from-blogger-to-static-site-nikola
.. date: 2016-08-07 11:32:15 UTC
.. tags: blogging
.. category: tech, blogging
.. link:
.. description:
.. type: text
-->

Long back I have started this blog on [blogger][] platform. Now I choose to migrate to a static because of limitations of blogger.

Blogger has a simple editor in browser to write posts in html. With static site, you can write post in your editor in markdown and keep them in version control system like git.

Jekyll, Pelican, Lektor were my initial choices for static site generators. Unfortunately, they didn't had any useful plugins for smooth migration of data from blogger. Then I stumbled across [import_blogger][] plugin of [Nikola][] and it is able to migrate text content, images without any issues. So, I decided to use Nikola.

[Nikola][] has great documentation and setup was simpler. I used `import_blogger` plugin and imported all the data. All the posts and pages were working well with exact same urls.

Blogger tags all posts of particular label under `/search/label/foo`. I have used these urls in some posts. Nikola shows posts under `/categories/foo.html`.

This is where nikola `REDIRECTIONS` come in handy. Using this, a list of from & to urls can be mapped. I wrote a simple function for redirections and then enabled `STRIP_INDEXES` which removes trailing `.html`.

```py
labels = ['python', 'emacs', 'zen', 'django', 'chrome']
LABEL_REDIRECTIONS = []

for label in labels:
    LABEL_REDIRECTIONS.append((
        '/search/label/{}/index.html'.format(label),
        '/categories/{}'.format(label),
    ))
```

Since I stripped `.html` from urls, old urls broke. So I generated a list of old urls and wrote another function to redirect them to new urls.

Nikola has few builtin themes. I wanted something minimalistic and so I rolled out custom theme which you are seeing right now.

Thanks to [Puneeth Chaganti][], [Chris Warrick][], [Roberto Alsina][] for helping me with migration.



[Blogger]: https://blogger.com
[import_blogger]: https://plugins.getnikola.com/#import_blogger
[nikola]: https://getnikola.com
[Puneeth Chaganti]: https://github.com/punchagan
[Chris Warrick]: https://github.com/Kwpolska
[Roberto Alsina]: https://github.com/ralsina
