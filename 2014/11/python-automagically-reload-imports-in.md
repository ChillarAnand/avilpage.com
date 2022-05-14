<!--
.. title: Automagically Reload Imports In iPython!
.. slug: python-automagically-reload-imports-in
.. date: 2014-11-19 17:21:00
.. tags: productivity, ipython
.. category: tech, programming, python
.. link:
.. description: Reload imports automatically in ipython shell
.. type: text
-->

When using iPython, users can import required modules to test them. After importing them, if they get modified either by user or some other process, users have to reload it for futher usage.

Depending on the Python version, appropriate `reload` function can reload modules.

```py
# Python 2.x
In [15]: imp.reload(module)

# Python 3.0–3.3
In [15]: imp.reload(module)

# Python 3.4+
In [15]: importlib.reload(module)
```

Instead of manually reloading, ipython has `autoreload` extention which can auto reload modules. For that, load the extention and activate it.

```py
In [15]: %load_ext autoreload

In [16]: %autoreload 2
```

This can be added to ipython config file so that autoreload gets activated, whenver it starts.

```sh
$ ipython profile create
```

This creates a default config file. Open config file which is present at `~/.ipython/profile_default/ipython_config.py`  and add these two lines to it.

```
c.InteractiveShellApp.extensions = ['autoreload']
c.InteractiveShellApp.exec_lines = ['%autoreload 2']
```

Note that it won't reloads c extensions automatically.
