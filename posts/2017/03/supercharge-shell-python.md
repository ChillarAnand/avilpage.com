<!--
.. title: Super Charge Your Shell For Python Development
.. slug: super-charge-your-shell-for-python-development
.. date: 2017-03-26 02:40:31 UTC
.. tags: python, automation, shell
.. category: python
.. link:
.. description: Shell tips and tricks for python & django developers to save your time.
.. type: text
-->

Last month, I gave a lightning talk about supercharging your shell for python development at [BangPypers meetup](http://www.meetup.com/BangPypers/).

<iframe width="600" height="350" src="https://www.youtube.com/embed/lvmJ0tWCjFA" frameborder="0" allowfullscreen></iframe>

This is a detailed blog post on how to setup your laptop for the same.


## Autojump

When working on terminal, `cd` is used to traverse directories.

```sh
cd ~/projects/python/django
```

`cd` is inefficient to quickly traverse directories which are in different paths and far away from each other.

```sh
cd /var/lib/elasticsearch/
cd ~/sandbox/channels/demo
```

`z`, a oh-my-zsh plugin is efficient for traversing directories. With `z`, directory can be changed by typing name of directory.

```sh
z junction
```

Instead of full name, just a substring would do.

```sh
z ju
```

`z` keeps a score of all visited directories and moves to most frecency(frequent+recent) directory that matches the substring.

To install `z`, install [oh-my-zsh](/2015/03/install-oh-my-zsh-on-ubuntu.html) and add `z` to plugins in `.zshrc` file.

```sh
plugins=(git z)
```

## Aliases

Read this old blog post on how [aliases will improve your productivity](/2014/10/useful-shell-aliases-for-python-and.html).


## Autoenv

When working on multiple projects, it becomes necessary to use virtualenvs so that multiple versions of same package can be used. In addition to that, it be necessary to set environment variables on a per project basis.

To automate all these things, [autoenv](https://pypi.python.org/pypi/autoenv/) provides directory based environments. Whenever user changes directory, it will help to automatically activate environment and set environment variables.

If you have file named `.env` in a directory, autoenv will automatically source that file whenever user enters into it.

`autoenv` is a python package. It can be installed with

```sh
pip install autoenv
```

It provides a shell script which needs to sourced.

```sh
echo "source `which activate.sh`" >> ~/.bashrc
```

You can create a .env file like this in project root.

```sh
source ~/.virtualenvs/exp/bin/activate
export SECRET_KEY=foobar
```

Next time, when your enter into that directory, `autoenv` finds `.env` file and it will source it automatically.


## Autoreload

I have written a sepeate blog post on how to [automagically reload imports](/2014/11/python-automagically-reload-imports-in.html) long time back.


## Autoimports

When you copy code and paste it in ipython interpreter, it might fail with `ImportError` if required modules aren't already imported by the interpreter.

Also when playing with code, having some predefined data would be handy. This avoids populating of data everytime shell starts.

You can write an init script which will do all these things and load it automatically when ipython starts.

Here is a [simple init script](https://github.com/ChillarAnand/01/blob/master/python/ipython_config.py) which I use to auto import modules and data. This file can be auto loaded by specifying it in your config file.

```py
c.InteractiveShellApp.exec_files = [os.path.join(directory, 'ipython_init.py')]
```

## Autocall

When using python interpreter, to call a function, you have to type parenthesis.Typing parenthesis is not ergonomic as you have to move both hands far away from homerow.

IPython provides `autocall` option to make functions callable without typing parenthesis. This can be activate with `%autocall` magic.

```py
In [6]: %autocall 1
Automatic calling is: Smart
```

Now functions can be called without parenthesis.

```py
In [7]: range 5
------> range(5)
Out[7]: range(0, 5)
```

You can also enable this by default by activating it in ipython config file.

```py
c.InteractiveShellApp.exec_lines = ['%autocall	1']
```

These are some tips to become more productive with your shell when working on python projects.
