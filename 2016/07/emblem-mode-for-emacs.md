<!--
.. title: emblem-mode for Emacs
.. slug: emblem-mode-for-emacs
.. date: 2016-07-25 17:32:35 UTC
.. tags: emacs
.. category: programming
.. link:
.. description: How write emblem code in emacs?
.. type: text
-->


Emblem.js is a ember friendly templating engine used as an alternative for handlebars.js.

Emblem.js doesn't have any official plugins for emacs. However they recommend to use slim plugins as they are similar.

`slim-mode` is available on melpa. To install it, run

```el
M-x install-package slim-mode
```

After installing it, activate `slim-mode` by running `M-x slim-mode`.

Instead of activating manually, `auto-mode-alist` can be used to set major modes that needs to activated for files with specific extension. To activate slim-mode for emblem files which will be ending with `.em` or `.emblem`, use

```lisp
(add-to-list 'auto-mode-alist '("\\.\\(em\\|emblem\\)" . slim-mode))
```

By adding this line to emacs configuration file, slim-mode gets activated for emblem.js files.
