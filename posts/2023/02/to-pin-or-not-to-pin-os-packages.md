<!--
.. title: Problems with pinning OS packages in Dockerfile
.. slug: pinning-os-packages-in-dockerfile
.. date: 2023-02-16 06:29:35 UTC+05:30
.. tags: python, docker, devops, draft
.. category:  
.. link: 
.. description: What are problems caused by pinning OS packages in Dockerfile
.. type: text
-->


### Introduction

If you think Docker builds are deterministic & reproducible, think again.

```dockerfile
FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y \
    python3-pip=20.0.2-5ubuntu1.6
```

This is a simple Dockerfile that just installs a pinned version of python3-pip.

This file was working fine from several months and all of a sudden it stopped working as `apt-get` is not able to locate this package.

### System Packages

If you have used any language specific package manager like `pip`, `npm`, etc. you might have noticed that you can pin a package, and you can download that package anytime you want.

However, system packages are a different kind. For example, many system packages drop older versions from their repositories. So, if you have pinned a package, and that package is no longer available in the repository, you will not be able to run the builds.

You have to update the package version in the Dockerfile to make it work again.

Unlike language specific package managers, system package managers have additional maintenance burden .

### Conclusion

Even though pinning packages is a good practice, it is a minor annoyance when you have to update the package version in the Dockerfile. But 