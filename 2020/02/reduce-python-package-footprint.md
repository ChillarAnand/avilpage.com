<!--
.. title: How To Reduce Python Package Footprint?
.. slug: reduce-python-package-footprint
.. date: 2020-02-29 20:20:38 UTC+05:30
.. tags: python, featured
.. category: programming
.. link:
.. description: How to reduce disk space usage of python package
.. type: text
-->

PyPi[^1] hosts over 210K+ projects and the average size of Python package is less than 1MB. However some of the most used packages in scientific computing like NumPy, SciPy has large footprint as they bundle shared libraries[^2] along with the package.

### Build From Source

If a project needs to be deployed in AWS Lambda, the total size of deployment package should be less than 250MB[^3].

```
$ pip install numpy

$ du -hs ~/.virtualenvs/py37/lib/python3.7/site-packages/numpy/
 85M	/Users/avilpage/.virtualenvs/all3/lib/python3.7/site-packages/numpy/
```

Just numpy occupies 85MB space on Mac machine. If we include a couple of other packages like scipy & pandas, overall size of the package crosses 250MB.

An easy way reduce the size of python packages is to build from source instead of use pre-compiled wheels.

```
$ CLFAGS='-g0 -Wl -I/usr/include:/usr/local/include -L/usr/lib:/usr/local/lib' pip install numpy --global-option=build_ext

$ du -hs ~/.virtualenvs/py37/lib/python3.7/site-packages/numpy/
 23M	/Users/avilpage/.virtualenvs/all3/lib/python3.7/site-packages/numpy/
```

We can see the footprint has reduced by ~70% when using sdist instead of wheel. This[^4] article provides more details about these CFLAG optimization when installing a package from source.


### Shared Packages

When using a laptop with low storage for multiple projects with conflicting dependencies, a seperate virtual environment is needed for each project. This will lead to installing same version of the package in multiple places which increases the footprint.

To avoid this, we can create a shared virtual environment which has most commonly used packages and share it across all the enviroments. For example, we can create a shared virtual enviroment with all the packages required for scientific computing.

For each project, we can create a virtual enviroment and share all packages of the common enviroment. If any project requires a specific version of the package, the same package can be install in project enviroment.

```
$ cat common-requirements.txt  # shared across all enviroments
numpy==1.18.1
pandas==1.0.1
scipy==1.4.1

$ cat project1-requirements.txt  # project1 requirements
numpy==1.18.1
pandas==1.0.0
scipy==1.4.1

$ cat project2-requirements.txt  # project2 enviroments
numpy==1.17
pandas==1.0.0
scipy==1.4.1
```

After creating a virtual enviroment for a project, we can create a `.pth` file with the path of site-packages of common virtual enviroment so that all those packages are readily available in the new project.

```
$ echo '/users/avilpage/.virtualenvs/common/lib/python3.7/site-packages' >
 ~/.virtualenvs/project1/lib/python3.7/site-packages/common.pth
```

Then we can install the project requirements which will install only missing packages.

```
$ pip install -r project1-requirements.txt
```

### Global Store

The above shared packages solution has couple issues.

1. User has to manually create and track shared packages for each Python version and needs to bootstrap it in every project.
2. When there is an incompatible version of package in multiple projects, user will end up with duplicate installations of the same version.

To solve this[^5], we can have a global store of packages in a single location segregated by python and package version. Whenever a user tries to install a package, check if the package is in global store. If not install it in global store. If present, just link the package to virtualenvs.

For example, numpy1.17 for Python 3.7 and numpy1.18 for Python 3.6 can be stored in the global store as follows.

```
$ python3.6 -m pip install --target ~/.mpip/numpy/3.6_1.18 numpy

$ python3.7 -m pip install --target ~/.mpip/numpy/3.7_1.17 numpy

# in project venv
echo '~/.mpip/numpy/3.7_1.17' > PATH_TO_ENV/lib/python3.7/site-packages/numpy.pth
```

With this, we can ensure one version of the package is stored in the disk only once. I have created a simple package manager called mpip[^6] as a POC to test this and it seems to work as expected.


These are couple of ways to reduce to footprint of Python packages in a single environment as well as muliple enviroments.


[^1]: [https://pypi.org/](https://pypi.org/)

[^2]: [https://github.com/numpy/numpy/issues/10920](https://github.com/numpy/numpy/issues/10920)

[^3]: [https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html)

[^4]: [https://towardsdatascience.com/how-to-shrink-numpy-scipy-pandas-and-matplotlib-for-your-data-product-4ec8d7e86ee4](https://towardsdatascience.com/how-to-shrink-numpy-scipy-pandas-and-matplotlib-for-your-data-product-4ec8d7e86ee4)

[^5]: [https://github.com/pypa/packaging-problems/issues/328](https://github.com/pypa/packaging-problems/issues/328)

[^6]: [https://github.com/ChillarAnand/mpip](https://github.com/ChillarAnand/mpip)
