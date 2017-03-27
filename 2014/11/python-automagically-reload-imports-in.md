<!--
.. title: Automagically Reload Imports In IPython
.. slug: python-automagically-reload-imports-in
.. date: 2014-11-19 17:21:00
.. tags: ipython, python-tips
.. category: programming, python
.. link:
.. description: How to reload python imports without restarting the interpreter.
.. type: text
-->

If you are using IPython, you will be importing some of the modules you have written. While playing with them, you may want to change them or if there is a bug, you will have to fix them.

Once you changed your code, you have to exit and start new interpreter or you can reload the module.

To reload the already imported modules:

```py
# Python 2.x
>>> imp.reload(module)

# Python 3.0–3.3
>>> imp.reload(module)

# Python 3.4+
>>> importlib.reload(module)
```

If you are developing something this will be annoying because for every small change you need to reload the module. IPython has `autoreload` magic which automatically reloads modules. You can enable it with

```py
In [15]: %load_ext autoreload

In [16]: %autoreload 2
```

You can do this everytime you start IPython or you can configure IPython to that automatically.

Create a default profile using this command

```
$ ipython profile create
```

Go to your default profile at `~/.ipython/profile_default/ipython_config.py` and add these two lines at the end.

```py
c.InteractiveShellApp.extensions = ['autoreload']
c.InteractiveShellApp.exec_lines = ['%autoreload 2']
```

Nex time when you start IPython, autoreload will be enabled by default. Also note that reload doesn't reloads c extensions automatically.
