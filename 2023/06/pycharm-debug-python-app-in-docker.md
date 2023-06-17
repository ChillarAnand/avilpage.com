<!--
.. title: Remote Debug Docker Container with PyCharm
.. slug: pycharm-debug-python-app-in-docker
.. date: 2023-06-11 21:06:04 UTC+05:30
.. tags: docker, python, debugging
.. category: programming
.. link: 
.. description: How to remote debug a docker container started from a third-party process using Inellij PyCharm IDE?
.. type: text
-->

### Problem Statement

How to debug a Python application running inside a Docker container that is launched by a third-party process using PyCharm?

### Solution

- Install the `pydevd-pycharm` package in the Docker image.

```Dockerfile
RUN pip install 'pydevd-pycharm~=222.4554.11'
```

- Add the following lines to the Python script that you want to debug.

```python
import pydevd_pycharm
pydevd_pycharm.settrace('host.docker.internal', port=12345, stdoutToServer=True, stderrToServer=True)
```

- Create a new Python Remote Debug configuration in PyCharm with the following settings.

![PyCharm Remote Debug Configuration](/images/pycharm-docker-debug.png)

- Run the Remote Debug configuration in PyCharm.

- Run the Docker container with the following command or let a shell script or another package run the container.

```bash
$ docker build . -t flask_web
$ docker run --rm flask_web
```

### Explanation

The `pydevd-pycharm` package is a Python debugger that can be used to debug a Python application running inside a Docker container. The `pydevd_pycharm.settrace()` function is used to connect the debugger to the PyCharm IDE. The `host.docker.internal` is the hostname of the host machine from inside the Docker container. The `port` is the port number that is used to connect to the PyCharm IDE. The `stdoutToServer` and `stderrToServer` are used to redirect the standard output and standard error to the PyCharm IDE.

### Gotchas

- You might face the following error depending on the version of the `pydevd-pycharm` package.

```bash
Traceback (most recent call last):
  File "/usr/local/lib/python3.10/site-packages/flask/cli.py", line 218, in locate_app
    __import__(module_name)
  File "/app/app.py", line 5, in <module>
    import pydevd_pycharm
  File "/usr/local/lib/python3.10/site-packages/pydevd_pycharm.py", line 3, in <module>
    from pydevd import settrace
  File "/usr/local/lib/python3.10/site-packages/pydevd.py", line 41, in <module>
    from _pydevd_bundle import pydevd_utils
  File "/usr/local/lib/python3.10/site-packages/_pydevd_bundle/pydevd_utils.py", line 24, in <module>
    from _pydevd_asyncio_util.pydevd_asyncio_utils import eval_async_expression_in_context
ModuleNotFoundError: No module named '_pydevd_asyncio_util'
```

There seems to be an issue with all 223.\*.\* versions. The solution is to use the 222.\*.\* version.

- You might face `ConnectionRefused` error when running the docker container.

```bash
  File "/usr/local/lib/python3.10/site-packages/pydevd.py", line 1758, in _locked_settrace
    debugger.connect(host, port)  # Note: connect can raise error.
  File "/usr/local/lib/python3.10/site-packages/pydevd.py", line 660, in connect
    s = start_client(host, port)
  File "/usr/local/lib/python3.10/site-packages/_pydevd_bundle/pydevd_comm.py", line 463, in start_client
    s.connect((host, port))
ConnectionRefusedError: [Errno 111] Connection refused
```

Ensure that you have started the Remote Debug configuration in PyCharm before running the docker container.

