<!--
.. title: Mastering PyCharm - Break on Handled Exceptions
.. slug: mastering-pycharm-break-on-handled-exceptions
.. date: 2023-02-03 16:22:25 UTC+05:30
.. tags: draft
.. category: 
.. link: 
.. description: 
.. type: text
-->


When we are debugging, we might have to find out where the exception is raised. We can set breakpoints to find out where the exception is raised. But, if the codebase is large, it is difficult to find out where the exception is raised.

PyCharm has option to break on unhandled exceptions. But, what if the exception is handled.


In the codebase, there might be many places where the exception is handled. So instead of setting individual breakpoints to find out where the code might be failing, we can create a base exception and add it in pycharm settings.

With this, when ever code enters exception block it will automatically break. We can take a look at the exception and proceed from there.

