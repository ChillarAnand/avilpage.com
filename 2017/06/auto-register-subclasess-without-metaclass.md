<!--
.. title: Auto Register Subclasses Without Metaclass in Python
.. slug: auto-register-subclasess-without-metaclass
.. date: 2017-06-10 15:30:27 UTC
.. tags: metaclass, design patterns, python
.. category: programming, python
.. link:
.. description: How to auto register subclasses without using metaclasses
.. type: text
-->

In registry pattern, a `registry` maintains global association from keys to objects, so that objects can be reached from anywhere by simple identifier. This is useful for doing reverse lookups.

When building a registry, programmers have to explicitly register each object with registry. Manually building a registry is error prone and it is tedious if there are too many objects to register. It is better to auto register objects if possible.

A commonly used approach is to use inheritance as an organizing mechanism. Create [a meta class which will auto register](https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Metaprogramming.html#example-self-registration-of-subclasses) classes and then create base class with this meta class.

```python
REGISTRY = {}


def register_class(target_class):
    REGISTRY[target_class.__name__] = target_class


class MetaRegistry(type):

    def __new__(meta, name, bases, class_dict):
        cls = type.__new__(meta, name, bases, class_dict)
        if name not in registry:
            register_class(cls)
        return cls


class BaseClass(metaclass=MetaRegistry):
    pass


class Foo(BaseClass):
    pass


class Bar(BaseClass):
    pass
```

Now whenever you subclass `BaseClass`, it gets registered in the global registry. In the above example, `Foo`, `Bar` gets registered automatically.

Eventhough it solves registration problem, it is hard to understand the code unless you know how metaclasses work.

A simple alternative for this is to use `__subclasses__()` to get subclasess and register them.

```python
REGISTRY = {cls.__name__: cls for cls in BaseClass.__subclasses__()}
```

This will work only for direct subclasses and won't with indirect subclasses like this.

```python
class Baz(Bar):
    pass
```

To solve this, we can use a function to recursively retrieve all subclasses of a class.

```python
def subclasses(cls, registry=None):
    if registry is None:
        registry = set()

    subs = cls.__subclasses__()

    for sub in subs:
        if sub in registry:
            return
        registry.add(sub)
        yield sub
        for sub in subclasses(sub, registry):
            yield sub


REGISTRY = {cls.__name__: cls for cls in subclasses(BaseClass)}
```

[PEP 487](https://www.python.org/dev/peps/pep-0487/) provides `__init_subclass__` hook in class body  to customize class creation without the use of metaclass. We can our registration logic in this `__init_subclass__` hook.

```python
class BaseClass:
    def __init_subclass__(cls, **kwargs):
        if cls not in registry:
            register_class(cls)
        super().__init_subclass__(**kwargs)

print(registry)
```

This is available only in Python 3.6+. For older versions, we have to use the recursive function to get all subclasess. This code is easier to understand than metaclass example.
