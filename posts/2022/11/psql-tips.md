;<!--
.. title: psql tips
.. slug: psql-tips
.. date: 2022-11-07 07:23:50 UTC+05:30
.. tags: draft
.. category:
.. link:
.. description:
.. type: text
-->


https://pgdash.io/blog/postgres-psql-tips-tricks.html

https://github.com/search?q=psqlrc


# psql tips

Create a custom `psqlrc` file in your home directory and add required defaults and custom settings based on your usage.

```bash
$ cat ~/.psqlrc

# show time - user - host - db in prompt
\set PROMPT1 '\n%[%033[1;31m%]➤ %[%033[2;37m%]%`\! date "+%F %I:%M %p %Z"`%[%033[0m%] %[%033[1;36m%]%n%[%033[34m%]@%[%033[1;36m%]%M:%>%[%033[1;33m%]/%/ %[%033[1;31m%]%x %[%033[K%]%[%033[0m%]\n%[%033[1;33m%]%R%#%[%033[0m%] '
`

export to csv - remote host



use -E flag
