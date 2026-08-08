<!--
.. title: Install GDAL/OGR anywhere with single pixi command
.. slug: install-gdal-anywhere-with-single-command
.. date: 2025-12-25 18:19:51 UTC+05:30
.. tags: gdal, pixi, cross-platform, draft
.. category: programming
.. link: 
.. description: Install gdal on any operating system with a single command using pixi package manager.
.. type: text
-->

If you have installed [GDAL](https://en.wikipedia.org/wiki/GDAL)/OGR in the past, you know how painful it is to install it on multiple operating systems.

### Pixi

[Pixi](https://github.com/prefix-dev/pixi) is cross plarform (Linux, Mac[Apple Silicon], Windows) multi language package manager.

Install pixi.

```
$ curl -fsSL https://pixi.sh/install.sh | sh
```

Install gdal globally with pixi.

```
$ pixi global install libgdal-core
```

Verify gdal installation.

```
$ gdal --version
GDAL 3.12.1 "Chicoutimi", released 2025/12/12
```

Thats it.

### Conclusion

Without worrying about the dependencies, OS specific installation steps,
GDAL/OGR can be installed with a single command using pixi.