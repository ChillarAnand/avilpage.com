<!--
.. title: Converting Strings To Correct Types In Python
.. slug: python-converting-string-type-objects
.. date: 2014-11-17 19:40:00
.. category: tech, programming, python
.. tags: python
.. description: How to convert string type objects to correct type in python


I was writing custom template tags for one of my Django package. I came across a situation where I had lists in string format. I need to convert them into lists.

```py
temp_str = '[345, 3, 456, 45]'
required_obj = [345, 3, 456, 45]
```

There are two methods to get this job done.

### ast.literal_eval:
This can be used to evaluate  strings containing Python values from untrusted sources without parsing values.
import ast
ast.literal_eval(temp_str)

### json.loads:

This is used to deserialize a string to python object using a conversion table.

```python
import json
json.loads(temp_str)
These two functions come in handy whenever you want to convert a list of python objects to their correct types. For example, if you have list of python objects like this
obj_list =  ['hello', '3', '3.64', '-1']
```

You can convert them to their corresponding types using these functions.

```python
def converter(l):
    for i in l:
        try:
            yield json.loads(i)
        except ValueError:
            yield i
def converter(l):
    for i in l:
        try:
            yield ast.literal_eval(i)
        except ValueError:
            yield i
```

They yield a objects of corresponding types
new_obj_list = ['hello', 3, 3.64, -1]
