<!--
.. title: Reliable Way To Test External APIs Without Mocking
.. slug: reliable-way-to-test-external-apis-without-mocking
.. date: 2018-04-08 21:21:21 UTC+05:30
.. tags: python, testing, django
.. category:
.. link:
.. description: Cache responses from external APIs for writing better integration tests.
.. type: text
-->


Let us write a function which retrieves user information from GitHub API.

```
import requests


def get_github_user_info(username):
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)
    if response.ok:
        return response.json()
    else:
        return None
```

To test this function, we can write a test case to call the external API and check if it is returning valid data.

```py
def test_get_github_user_info():
    username = 'ChillarAnand'
    info = get_github_user_info(username)
    assert info is not None
    assert username == info['login']
```

Even though this test case is reliable, this won't be efficient when we have many APIs to test as it sends unwanted requests to external API and makes tests slower due to I/O.

A widely used solution to avoid external API calls is [mocking](https://en.wikipedia.org/wiki/Mock_object). Instead of getting the response from external API, use a mock object which returns similar data.


```
from unittest import mock


def test_get_github_user_info_with_mock():
    with mock.patch('requests.get') as mock_get:
        username = 'ChillarAnand'

        mock_get.return_value.ok = True
        json_response = {"login": username}
        mock_get.return_value.json.return_value = json_response

        info = get_github_user_info(username)

        assert info is not None
        assert username == info['login']
```

This solves above problems but creates additional problems.

- Unreliable. Even though test cases pass, we are not sure if API is up and is returning a valid response.
- Maintenance. We need to ensure mock responses are up to date with API.

To avoid this, we can cache the responses using [requests-cache](https://pypi.python.org/pypi/requests-cache).

```py
import requests_cache

requests_cache.install_cache('github_cache')


def test_get_github_user_info_without_mock():
    username = 'ChillarAnand'
    info = get_github_user_info(username)
    assert info is not None
    assert username == info['login']
```

When running tests from developer machine, it will call the API for the first time and uses the cached response for subsequent API calls. On CI pipeline, it will hit the external API as there won't be any cache.

When the response from external API changes, we need to invalidate the cache. Even if we miss cache invalidation, test cases will fail in CI pipeline before going into production.
