<!--
.. title: Build & Distribute a Python C Extension Module
.. slug: build-distribute-a-python-c-extension-module
.. date: 2022-10-30 07:31:29 UTC+05:30
.. tags: python, c
.. category: programming
.. link: 
.. description: How to build and distribute a Python C extension module using wheels
.. type: text
-->

### Introduction

Python is a great language for prototyping and building applications. However, when it comes to performance, it is not the best choice. Python is an interpreted language and it is not compiled. This means that the code is not optimized for the machine it is running on. This is where C comes in. C is a compiled language and it is much faster than Python. So, if you want to write a Python module that is fast, you can write it in C and compile it. This is called a C extension module. In this article, we will see how to build and distribute a Python C extension module using wheels.


### Building a C extension module

Let's start by creating a simple C extension module called `maths`. In this, we will create a `square` function that takes a number and returns its square.

First, create a directory called `maths` and create a file called `maths.c` inside it. This is where we will write our C code.

```c
#include <Python.h>


int square(int num) {
    return num * num;
}


static PyObject *py_square(PyObject *self, PyObject *args) {
  int n_num, result;
  if (!PyArg_ParseTuple(args, "i", &n_num)) {
    return NULL;
  }
  result = square(n_num);

  return Py_BuildValue("i", result);
}


static PyMethodDef mathsMethods[] = {
  {"square", py_square, METH_VARARGS, "Function for calculating square in C"},
  {NULL, NULL, 0, NULL}
};


static struct PyModuleDef maths = {
  PyModuleDef_HEAD_INIT,
  "maths",
  "Custom maths module",
  -1,
  mathsMethods
};


PyMODINIT_FUNC PyInit_maths(void)
{
    return PyModule_Create(&maths);
}
```

We need to create a `setup.py` file to build our module. This file tells Python how to build our module.

```python
from setuptools import setup, Extension

setup(
    name="maths",
    version="0.1",
    ext_modules=[Extension("maths", ["maths.c"])]
)
```

Now, we can build our module by running `python setup.py build`. This will create a `build` directory with a `lib` directory inside it.
This `lib` directory contains our compiled module. We can import this module in Python and use it.

```python
>>> import maths
>>> maths.square(5)
25
```

Instead of testing our module by importing it in Python, we can also test it by running `python setup.py test`. This will run the tests in the `test` directory. We can create a `test` directory and create a file called `test_maths.py` inside it. This is where we will write our tests.

```python
import unittest

import maths

class TestMaths(unittest.TestCase):
    def test_square(self):
        self.assertEqual(maths.square(5), 25)

```

### Distributing a C extension module

Now that we have built our module, we can distribute it. We can distribute it as a source distribution or a binary distribution. A source distribution is a zip file that contains the source code of our module. We can distribute our module as a source distribution by running `python setup.py sdist`. This will create a `dist` directory with a zip file inside it. This zip file contains our source code.

However, source distribution of C extension modules is not recommended. This is because the user needs to have a C compiler installed on their machine to build the module. Most users just want to `pip install` the module and use it. So, we need to distribute our module as a binary distribution.

We can use `cibuildwheel` package to build wheels across all platforms. We can install it by running `pip install cibuildwheel`.

To build a wheel for a specific platform and a specific architecture, we can run `cibuildwheel --platform <platform> --architecture <architecture>`. For example, to build a wheel for Linux x86_64, we can run `cibuildwheel --platform linux --architecture x86_64`. This will create a `wheelhouse` directory with a wheel file inside it. This wheel file contains our compiled module.

`cibuildwheel` runs on most CI servers. With proper workflows, we can easily get wheels for all platforms and architectures. We can then upload these wheels to PyPI and users can easily install these wheels.

### Conclusion

In this article, we saw how to build and distribute a Python C extension module using wheels. We saw how to build a C extension module and how to distribute it as a binary distribution. We also saw how to use `cibuildwheel` to build wheels across all platforms and architectures.

