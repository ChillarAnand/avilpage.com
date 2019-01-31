<!--
.. title: How To Install Private Python Packages With Pip
.. slug: how-to-install-private-python-packages-with-pip
.. date: 2019-01-31 12:12:12 UTC+05:30
.. tags: python, devops
.. category:
.. link:
.. description: how to install private python packages from github, gitlab, bitbucket with pip
.. type: text
-->

### Introduction

To distribute python code, we need to package it and host it somewhere, so that users can install and use it. If the code is public, it can be published to [PyPi](https://pypi.org) or any public repository, so that anyone can access it. If the code is private, we need to provide proper authentication mechanism before allowing users to access it.

In this article, we will see how to use [pip][pip] to install Python packages hosted on GitLab, GitHub, Bitbucket or any other services.


### Packaging

To package python project, we need to create `setup.py` file which is build script for setuptools. Below is a sample setup file to create a package named `library`.


```python
import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="library",
    version="0.0.1",
    author="chillaranand",
    author_email="foo@avilpage.com",
    description="A simple python package",
    long_description=long_description,
    url="https://github.com/chillaranand/library",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
```

Python provides [detailed packaging documentation](https://packaging.python.org/tutorials/packaging-projects/) on structuring and building the package.

### Installation

Once module(s) is packaged and pushed to hosting service, it can be installed with pip.

```sh
# using https
$ pip install git+https://github.com/chillaranand/library.git

# using ssh
pip install git+ssh://git@github.com/chillaranand/library.git
```

This usually requires authentication with usersname/password or ssh key. This setup works for developement machines. To use it in CI/CD pipelines or as a dependency, we can use tokens to simplify installation.

```sh
$ export GITHUB_TOKEN=foobar

$ pip install git+https://$GITHUB_TOKEN@github.com/chillaranand/library.git
```

### Conclusion

In this article, we have seen how to package python code and install private packages with pip. This makes it easy to manage dependencies or install packages on multiple machines.


[pip]: https://packaging.python.org/key_projects/#pip
