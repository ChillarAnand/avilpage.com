<--
.. title: Django Tips & Tricks #1 - Shell Aliases For Python/Django Developers
.. slug: useful-shell-aliases-for-python-and
.. date: 2014-10-25 18:27:00
.. tags: python, command-line, django, django-tips-tricks
.. category: python
.. description: Using shell aliases for productivity.
-->

Developers and hackers prefer using terminal and spend a lot of time on it. Instead of typing long commands over and over, they can be aliased to shortnames. The shell builtin alias allows users to set aliases.

One of the most used command while setting up development environment is `pip install -r requirements.txt` This can be aliased to `pir`.


```sh
alias pir='pip install -r requirements.txt
```

Now to install requirements, type `pir` and pressing enter. Here are some other aliases related to python which will be useful on a daily basis.

```sh
alias py='python'
alias ipy='ipython'
alias py3='python3'
alias ipy3='ipython3'

alias jn='jupyter notebook'

alias wo='workon'
alias pf='pip freeze | sort'
alias pi='pip install'
alias pun='pip uninstall'

alias dj="python manage.py"
alias drs="python manage.py runserver"
alias drp="python manage.py runserverplus"
alias drps="python manage.py runserverplus --print-sql"
alias dsh="python manage.py shell"
alias dsp="python manage.py shell_plus"
alias dsps="python manage.py shell_plus --print-sql"
alias dsm="python manage.py schemamigration"
alias dm="python manage.py migrate"
alias dmm="python manage.py makemigrations"
alias ddd="python manage.py dumpdata"
alias dld="python manage.py loaddata"
alias dt="python manage.py test"
```

Just add the above aliases to your `~/.bashrc` or `~/.zshrc`. That's it. Hpy alsng!
