<!--
.. title: Disabling Atomic Transactions In Django Test Cases
.. slug: disable-transactions-django-tests
.. date: 2020-01-31 21:21:21 UTC+05:30
.. tags: python, django
.. category:
.. link:
.. description:
.. type: text
-->

[TestCase][testcase] is the most used class for writing tests in Django. To make tests faster, it wraps all the tests in 2 nested `atomic` blocks.

In this article, we will see where these atomic blocks create problems and find ways to disable it.


### Select for update

Django provides [select_for_update()][select_for_update] method on model managers which returns a queryset that will lock rows till the end of transaction.

```python
def update_book(pk, name):
    with transaction.atomic():
        book = Book.objects.select_for_update().get(pk=pk)
        book.name = name
        book.save()
```

When writing test case for a piece of code that uses `select_for_update`, Django recomends not to use TestCase as it might not raise `TransactionManagementError`.

### Threads

Let us take a view which uses threads to get data from database.

```python
def get_books(*args):
    queryset = Book.objects.all()
    serializer = BookSerializer(queryset, many=True)
    response = serializer.data
    return response

class BookViewSet(ViewSet):

    def list(self, request):
        with ThreadPoolExecutor() as executor:
            future = executor.submit(get_books, ())
            return_value = future.result()
        return Response(return_value)
```

A test which writes some data to db and then calls this API will fail to fetch the data.


```python
class LibraryPaidUserTestCase(TestCase):
    def test_get_books(self):
        Book.objects.create(name='test book')

        self.client = APIClient()
        url = reverse('books-list')
        response = self.client.post(url, data=data)
        assert response.json()
```

Threads in the view create a new connection to the database and they don't see the created test data as the transaction is not yet commited.


### Transaction Test Case

To handle above 2 scenarios or other scenarios where database transaction behaviour needs to be tested, Django recommends to use `TransactionTestCase` instead of TestCase.

```python
from django.test import TransactionTestCase

Class LibraryPaidUserTestCase(TransactionTestCase):
    def test_get_books(self):
        ...
```

With TransactionTestCase, db will be in auto commit mode and threads will be able to fetch the data commited earlier.

Consider a scenario, where there are other utility classes which are subclassed from TestCase.

```python
class LibraryTestCase(TestCase):
    ...

class LibraryUserTestCase(LibraryTestCase):
    ...

class LibraryPaidUserTestCase(LibraryTestCase):
    ...
```

If we subclass LibraryTestCase with TransactionTestCase, it will slow down the entire test suite as all the tests run in autocommit mode.

If we subclass LibraryUserTestCase with TransactionTestCase, we will miss the functionality in LibraryTestCase. To prevent this, we can override the custom methods to call TransactionTestCase.

If we look at the source code of TestCase, it has 4 methods to handle atomic transactions. We can override them to prevent creation of atomic transactions.


```python
class LibraryPaidUserTestCase(LibraryTestCase):
    @classmethod
    def setUpClass(cls):
        super(TestCase, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TestCase, cls).tearDownClass()

    def _fixture_setup(self):
        return super(TestCase, self)._fixture_setup()

    def _fixture_teardown(self):
        return super(TestCase, self)._fixture_teardown()
```


We can also create a mixin with the above methods and subclass it wherever this functionality is needed.

### Conclusion

Django wraps tests in TestCase inside atomic transactions to speed up the run time. When we are testing for db transaction behaviours, we have to disable this using appropriate methods.


[testcase]: https://docs.djangoproject.com/en/dev/topics/testing/tools/#testcase
[select_for_update]: https://docs.djangoproject.com/en/3.0/ref/models/querysets/#select-for-update
