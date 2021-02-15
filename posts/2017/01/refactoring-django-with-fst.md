<!--
.. title: Refactoring Django With Full Syntax Tree
.. slug: refactoring-django-with-fst
.. date: 2017-01-29 17:51:37 UTC
.. tags: python, django, featured
.. category: tech, programming, python
.. link:
.. description: Writing python code to modify code using Full Syntax Trees
.. type: text
-->

Django developers decided to [drop Python 2 compatability][1]{:target="_blank"} in Django 2.0. There are serveral things that should be refactored/removed.

For example, in Python 2, programmers has to explicitly specify the class & instance when invoking `super`.

```python
class Foo:
    def __init__(self):
        super(Foo, self).__init__()
```

In Python 3, `super` can be invoked without arguments and it will choose right class & instance automatically.

```python
class Foo:
    def __init__(self):
        super().__init__()
```

For this refactoring, a simple `sed` search/replace should suffice. But, there are several hacks in codebase where super calls the grandparent instead of the parent. So, `sed` won't work in such cases. It is hard to refactor them manually and much harder for reviewers as there are 1364 super calls in code base.

```sh
→ grep -rI "super(" | wc -l
   1364
```

So changes has to be scripted. A [simple python script][2]{:target="_blank"} to replace super calls by class names will fail to capture classes with on top of them, classes with decorators and nested classes.

To handle all these cases, this python script gets more complicated and there is no guarantee that it can handle all edge cases. So, a better choice is to use syntax trees.

Python has [ast module][3]{:target="_blank"} to convert code to AST but it can't convert AST back to code. There are 3rd party packages like [astor](https://pypi.python.org/pypi/astor){:target="_blank"} which can do this.


```python
# this is a comment
def foo():

   print(
    "hello world"
)
```

Converting above code to AST and then converting back gives this

```python
def foo():
    print('hello world')
```

Code to AST is a lossy transformation as they cannot preserve empty lines, comments and code formatting.

```python
ast_to_code(code_to_ast(source_code)) != source_code
```

For lossless transformation, FST(Full Syntax Trees) is needed.

```python
fst_to_code(code_to_fst(source_code)) == source_code
```

[RedBaron][5]{:target="_blank"} package provides FST for given piece of code. With this, just locate super calls, find nearest class node, check class name with super and replace accordingly. With RedBaron, this refactoring can be done in [less than 10 lines][6]{:target="_blank"} of code.

RedBaron has good documentation with relveant examples and its API is similar to BeautifulSoup. To write code that modifies code RedBaron seems to be an apt choice.

Thanks to [Tim Graham](https://github.com/timgraham){:target="_blank"} & [Aymeric Augustin](https://github.com/aaugustin){:target="_blank"} for [reviewing the patch](https://github.com/django/django/pull/7905/commits/d6eaf7c0183cd04b78f2a55e1d60bb7e59598310){:target="_blank"}.

[1]: https://code.djangoproject.com/ticket/23919
[2]: https://github.com/ChillarAnand/01/blob/master/python/super_exp.py
[3]: https://docs.python.org/3/library/ast.html
[4]: https://github.com/PyCQA/baron
[5]: https://github.com/PyCQA/redbaron
[6]: https://github.com/ChillarAnand/01/blob/master/python/redbaron_super.py
