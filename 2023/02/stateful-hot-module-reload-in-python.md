<!--
.. title: Hot Module Reload In Python With Reloadium
.. slug: stateful-hot-module-reload-in-python
.. date: 2023-02-16 11:58:58 UTC+05:30
.. tags: python, hot-reload
.. category: programming
.. link: 
.. description: How to do stateful hot module reload in python with reloadium?
.. type: text
-->

### Introduction

Hot module reloading is a feature that allows you to reload a module without restarting the whole application. This is very useful when we are developing/debugging an application, and we want to see the changes instantaneously.


### Reloadium

Reloadium[^reloadium] is an advanced hot reloading library for python.

Instead of writing an article, I thought it would be much easier to show a live demo of Reloadium. In the below video, we can see how reloadium greatly improves developer experience.

<div class="embed-responsive embed-responsive-16by9">
<iframe class="embed-responsive-item" src="https://www.youtube.com/embed/9UO1raFQdo8" allowfullscreen>
</iframe>
</div>
<br />

Currently, reloadium can be used as a standalone tool. We can install it from PyPi and run any arbitrary python script with reloadium.

```
$ pip install reloadium
$ reloadium run myscript.py
```

Alternatively, it is available as a plugin for PyCharm as shown in the above video. VS Code support is also in the works.

Reloadium is capable of profiling too. Without writing a single line of code, we can profile Python code. But that's a topic for another article.


### Conclusion

I have been using Reloadium from a few months, and it has become an essential part of my development workflow. These days I always run all the scripts or apps in debug mode with reloadium directly. 



[^reloadium]: [https://github.com/reloadware/reloadium](https://github.com/reloadware/reloadium)

