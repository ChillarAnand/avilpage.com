<!--
.. title: Tips On Writing Data Migrations in Django Application
.. slug: django-tips-data-migrations
.. date: 2019-09-30 21:21:21 UTC+05:30
.. tags: django, django-tips-tricks
.. category: python
.. link:
.. description: Django Tips & Tricks - How to write data migrations in django.
.. type: text
-->


### Introduction

In a Django application, when schema changes Django automatically generates a migration file for the schema changes. We can write additional migrations to change data.

In this article, we will learn some tips on writing [data migrations in Django applications][].


### Use Management Commands

Applications can register custom actions with `manage.py` by creating a file in `management/commands` directory of the application. This makes it easy to (re)run and test data migrations.

Here is a management command which migrates the `status` column of a `Task` model.

```python
from django.core.management.base import BaseCommand
from library.tasks import Task

class Command(BaseCommand):

    def handle(self, *args, **options):
        status_map = {
            'valid': 'ACTIVE',
            'invalid': 'ERROR',
            'unknown': 'UKNOWN',
        }
        tasks = Task.objects.all()
        for tasks in tasks:
            task.status = status_map[task.status]
            task.save()
```


If the migration is included in Django migration files directly, we have to rollback and re-apply the entire migration which becomes cubersome.


### Link Data Migrations & Schema Migrations

If a data migration needs to happen before/after a specific schema migration, include the migration command using [RunPython][] in the same schema migration or create seperate schema migration file and add schema migration as a dependency.


```python
def run_migrate_task_status(apps, schema_editor):
    from library.core.management.commands import migrate_task_status
    cmd = migrate_task_status.Command()
    cmd.handle()


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(run_migrate_task_status, RunSQL.noop),
    ]
```


### Watch Out For DB Queries

When working on a major feature that involves a series of migrations, we have to be careful with data migrations(which use ORM) coming in between schema migrations.

For example, if we write a data migration script and then make schema changes to the same table in one go, then the migration script fails as Django ORM will be in invalid state for that data migration.

To overcome this, we can explicitly select only required fields and process them while ignoring all other fields.

```python
# instead of
User.objects.all()

# use
User.objects.only('id', 'is_active')
```

As an alternative, we can use raw SQL queries for data migrations.


### Conclusion

In this article, we have seen some of the problems which occur during data migrations in Django applications and tips to alleviate them.


[data migrations in Django applications]: https://docs.djangoproject.com/en/dev/topics/migrations/#data-migrations
[runpython]: https://docs.djangoproject.com/en/dev/ref/migration-operations/#django.db.migrations.operations.RunPython
