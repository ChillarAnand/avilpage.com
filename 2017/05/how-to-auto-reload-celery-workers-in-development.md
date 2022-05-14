<!--
.. title: How To Auto Reload Celery Workers In Development?
.. slug: how-to-auto-reload-celery-workers-in-development
.. date: 2017-05-07 04:22:47 UTC
.. tags: celery, automation, python
.. category: tech, programming, python
.. link:
.. description: How to automatically reload celery workers in development environment.
.. type: text
-->

We can pass `--autoreload` option when starting celery worker. This will restart worker when codebase changes.

```shell
celery worker -l info -A foo --autoreload
```

Unfortunately, it doesn't work as expected and [it is deprecated](https://github.com/celery/celery/issues/1658).

During development, we will keep on changing the code base. Manually restarting  celery worker everytime is a tedious process. It would be handy if workers can be auto reloaded whenever there is a change in the codebase.

[Watchdog](https://pypi.python.org/pypi/watchdog) provides Python API and shell utilities to monitor file system events. We can install it with

```sh
pip install watchdog
```

Watchdog provides `watchmedo` a shell utilitiy to perform actions based on file events. It has `auto-restart` subcommand to start a long-running subprocess and restart it. So, celery workers can be auto restarted using this.

```shell
watchmedo auto-restart -- celery worker -l info -A foo
```

By default it will watch for all files in current directory. These can be changed by passing corresponding parameters.

```shell
watchmedo auto-restart -d . -p '*.py' -- celery worker -l info -A foo
```

If you are using django and don't want to depend on watchdog, there is a simple trick to achieve this. Django has autoreload utility which is used by `runserver` to restart WSGI server when code changes.

The same functionality can be used to reload celery workers. Create a seperate management command called `celery`. Write a function to kill existing worker and start new worker. Now hook this function to autoreload as follows.

```python
import shlex
import subprocess

from django.core.management.base import BaseCommand
from django.utils import autoreload


def restart_celery():
    cmd = 'pkill -9 celery'
    subprocess.call(shlex.split(cmd))
    cmd = 'celery worker -l info -A foo'
    subprocess.call(shlex.split(cmd))


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Starting celery worker with autoreload...')
        autoreload.main(restart_celery)
```

Now you can run celery worker with `python manage.py celery` which will start a celery worker and autoreload it when codebase changes.
