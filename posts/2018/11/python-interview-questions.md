<!--
.. title: 200+ Python Interview Questions With Answers
.. slug: python-interview-questions-answers
.. date: 2018-11-15 09:34:21 UTC+05:30
.. tags: programming, python, career, draft
.. category:
.. link:
.. description: Python interview questions to prepare for interviews.
.. type: text
-->


### Introduction

### Beginner Questions

Q. What is the difference between lists and tuples?

A. Lists are mutable i.e they can changed after creation. Tuples are immutable and they can’t be changed after creation

```py
In [3]: info = ['name', 'mail', 'address']

In [4]: info[1] = 'email'

In [5]: info
Out[5]: ['name', 'email', 'address']

In [6]: info = ('name', 'mail', 'address')

In [7]: info[1] = 'email'
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-7-e3c5663a08dd> in <module>
----> 1 info[1] = 'email'

TypeError: 'tuple' object does not support item assignment
```

<b>
Q. What is the difference between deep copy and shallow copy?
</b>

The difference between shallow and deep copying is only relevant for compound objects (objects that contain other objects, like lists or class instances):

A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.

A. Shallow copy is used when a new instance type gets created and it keeps the values that are copied in the new instance. Shallow copy is used to copy the reference pointers just like it copies the values. These references point to the original objects and the changes made in any member of the class will also affect the original copy of it. Shallow copy allows faster execution of the program and it depends on the size of the data that is used.

Deep copy is used to store the values that are already copied. Deep copy doesn’t copy the reference pointers to the objects. It makes the reference to an object and the new object that is pointed by some other object gets stored. The changes made in the original copy won’t affect any other copy that uses the object. Deep copy makes execution of the program slower due to making certain copies for each object that is been called.




Q. What advantages do NumPy arrays offer over (nested) Python lists?
Python’s lists are efficient general-purpose containers. They support (fairly) efficient insertion, deletion, appending, and concatenation, and Python’s list comprehensions make them easy to construct and manipulate.
They have certain limitations: they don’t support “vectorized” operations like elementwise addition and multiplication, and the fact that they can contain objects of differing types mean that Python must store type information for every element, and must execute type dispatching code when operating on each element.
NumPy is not just more efficient; it is also more convenient. You get a lot of vector and matrix operations for free, which sometimes allow one to avoid unnecessary work. And they are also efficiently implemented.
NumPy array is faster and You get a lot built in with NumPy, FFTs, convolutions, fast searching, basic statistics, linear algebra, histograms, etc.


Q38. Explain the use of decorators.
Ans: Decorators in Python are used to modify or inject code in functions or classes. Using decorators, you can wrap a class or function method call so that a piece of code can be executed before or after the execution of the original code. Decorators can be used to check for permissions, modify or track the arguments passed to a method, logging the calls to a specific method, etc.



<!--  -->
##
singleton pattern in python

string case permutation

implement linkedlist in python


1+n django

django middleware

custom query to dict


### Conclusion
