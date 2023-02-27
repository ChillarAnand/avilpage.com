<!--
.. title: Using Conda/Mamba with Python Pip on M1 Mac
.. slug: using-conda-mamba-instead-of-pip-on-m1-mac
.. date: 2023-02-28 01:01:01 UTC+05:30
.. tags: python
.. category: programming
.. link:
.. description:
.. type: text
-->

### Introduction

From 2020, all Apple MacBooks are powered by Apple Silicone(M1) chips. This chip uses Aarch64 architecture which is different from x86 architecture which was used by Intel chips earlier.

Python is a cross-platform language. It can run on any platform. However, Python packages are compiled for specific platforms. For example, a package compiled for x86 will not work on  Aarch64 platform. Also, many Python packages are not yet available for ARM64/Aarch64 platform.

### M1 Mac and Python

If we want to run a python package on M1 Mac which doesn't have ARM64 support, we need to use an emulator(or a cross-architecture Docker image). This will significantly slow down the application.

An alternate solution is to build packages for ARM64 platform. Building binary packages from the source code requires a lot of time and effort. Also, we need to build the package for each Python version.

Instead of building from source, we can use Conda/Mamba to install Python packages as well as other system packages. Conda/Mamba will automatically install the correct binary for the package.

For example, python-confluent-kafka[^confluent-kafka] package doesn't have Linux aarch64 support. To run it on aarch64 platform, we have to build from source which takes a lot of time. Instead, we can simply install it using Conda/Mamba with a single command.

```sh
$ conda install -c conda-forge python-confluent-kafka
```

Similar to pip, Conda can also install all the packages mentioned in a file like `requirements.txt`.

```sh
$ conda install --file requirements.txt
```

### Conclusion

In data science ecosystem, Conda[^conda]/Mamba[^mamba] are widely used as package managers. In web development ecosystem, they are not as widely used as pip.

Conda/Mamba is a great cross-platform system package manager, and it doesn't have all the Python packages available on PyPi. However, we can use it along with pip for easy package management on M1 Macbook.


[^conda]: [https://en.wikipedia.org/wiki/Conda_(package_manager)](https://en.wikipedia.org/wiki/Conda_(package_manager))

[^mamba]: [https://github.com/mamba-org/mamba](https://github.com/mamba-org/mamba)

[^confluent-kafka]: [https://pypi.org/project/confluent-kafka/](https://pypi.org/project/confluent-kafka/)
