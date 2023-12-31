<!--
.. title: Running tests in parallel with pytest & xdist
.. slug: coverage-reports-with-pytest-xdist
.. date: 2023-12-30 01:16:31 UTC+05:30
.. tags: python, testing
.. category: programming
.. link: 
.. description: How to run tests in parallel with pytest & xdist
.. type: text
-->

When tests are taking too long to run, an easy way to speed them up is to run them in parallel.

When using `pytest` as test runner, `pytest-xdist` & `pytest-parallel` plugins makes it easy to run tests concurrently or in parallel.

`pytest-parallel` works better if tests are independent of each other. If tests are dependent on each other, `pytest-xdist` is a better choice.

If there are parameterised tests, pytest-xdist will fail as the order of the tests is not guaranteed.

```sh
$ pytest -n auto tests/

Different tests were collected between gw0 and gw1. The difference is: ...
```

To fix this, we have to make sure that the parameterised tests are executed in the same order on all workers. It can be achieved by sorting the parameterised tests by their name.

Alternatively, we can use `pytest-randomly` plugin to order the tests.

[//]: # (Another thing to note is that coverage.py package doesn't track sub-processes coverage by default. )

[//]: # ()
[//]: # (To enable coverage reports for sub-processes, we need to use `--cov-append` option. This option appends coverage data to existing `.coverage` file. )

[//]: # ()
[//]: # (```shell)

[//]: # ($ pytest --cov-append --cov=app tests/)

[//]: # (```)

[//]: # ()
[//]: # (This command will run tests in parallel, and append coverage data to `.coverage` file.)

[//]: # ()
[//]: # (To generate coverage report, we can use `coverage` command-line utility.)

[//]: # ()
[//]: # (```shell)

[//]: # ($ coverage report)

[//]: # (```)
