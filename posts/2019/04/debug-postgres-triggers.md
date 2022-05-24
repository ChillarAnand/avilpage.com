<!--
.. title: A Short Guide To Debugging PostgreSQL Triggers
.. slug: how-to-debug-postgres-triggers
.. date: 2019-04-30 21:21:21 UTC+05:30
.. category: programming
.. tags: database, postgresql
.. link:
.. description: How to debug and fix issues with postgresql triggers?
.. type: text
-->


### Introduction

[PostgreSQL triggers][psql-triggers] will associate a `function` to a table for an event. If multiple triggers of the same kind are defined for the same event, they will executed in alphabetical order by name.

In this article we will see how to debug PostgreSQL triggers.


### Triggers

First ensure triggers are enabled on the required tables for INSERT/UPDATE/DELETE events. We can check available triggers by running the following query.

```sql
SELECT * FROM information_schema.triggers;
```

We can also use `EXPLAIN` to show triggers which are executed for an event by running relevant queries.



### PostgreSQL Logging

After ensuring triggers are applied correctly, set logging level for postgresql server and client in postgres.conf file.

```sql
# let server log all queries
log_statement = 'all'

# set client message to log level
client_min_messages = log
```

Restart postgresql to reflect configuration changes.

```sh
# Linux
sudo service postgres restart

# Mac
brew services restart postgres
```

Tail the logs and check if queries are executing correctly with appropriate values.



### Triggers Logging

After enabling logging for PostgreSQL, we can [raise messages/errors in triggers][lmit] so that we can see if any unexpected things are happening at any point in the trigger.

```sql
RAISE 'Updating row with ID: %', id;
RAISE division_by_zero;
RAISE WARNING 'Unable to deleted record';
```

This makes sure triggers are executing as expected and if there are any warnings/errors, it will log a message.


### SQL/PostgreSQL Gotchas

Even though queries and triggers are executing correctly, we might not see the desired result because of potentially suprising behaviour of PostgreSQL. There are a some scenarios where PostgreSQL seems to be not working at first but it actually is the expected behaviour.

1. Unquoted object names will be treated as lower case. `SELECT FOO FROM bar` will become `SELECT foo FROM bar`.
2. Comparing nullable fields. This might yield strange results as `NULL != NULL`.
3. PostgreSQL uses POSIX offsets. For `04:21:42 UTC+01`, +1  means the timezone is west of Greenwich.


### Conclusion

By being aware of common PostgreSQL gotchas and enabling logging for PostgreSQL client, server & triggers, pinpointing the bug in triggers becomes easy. Once the bug is identified, appropriate action can be taken to fix the issue.




<!-- links -->

[Psql-triggers]:  https://www.postgresql.org/docs/9.1/sql-createtrigger.html
[lmit]: https://www.postgresql.org/docs/9.0/plpgsql-errors-and-messages.html
