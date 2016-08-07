<!--
.. title: emblem-mode for Emacs!
.. slug: emblem-mode-for-emacs
.. date: 2016-07-25 17:32:35 UTC
.. tags:
.. category: tech, emacs, ember, programming
.. link:
.. description: How write emblem in emacs?
.. type: text
-->



# emblem-mode for Emacs!

Emblem.js is a ember friendly templating engine used as an alternative for handlebars.js.

Emblem.js doesn't have any official plugins for emacs. However they recommend to use slim plugins as they are similar.

You get slim-mode from melpa. Install with

```el
M-x install-package slim-mode
```

Now we have to activate slim-mode for emblem files which will be ending with `.em` or `.emblem`. We can use `auto-mode-alist` to set major modes that needs to activated for files with specific extension.

```lisp
(add-to-list 'auto-mode-alist '("\\.\\(em\\|emblem\\)\\'" . slim-mode))
```

We can add this to emacs configuration which automatically activates slim mode for emblem.js files.
