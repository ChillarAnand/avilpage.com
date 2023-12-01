<!--
.. title: Coverage reports with pytest & xdist
.. slug: coverage-reports-with-pytest-xdist
.. date: 2023-11-16 21:16:31 UTC+05:30
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
-->

When tests are taking too long to run, an easy way to speed them up is to run them in parallel.

When using `pytest` as test runner, `pytest-xdist` & `pytest-parallel` plugins makes it easy to run tests concurrently or in parallel. However, coverage.py package doesn't track sub-processes by default. 

To enable coverage reports for sub-processes, we need to use `--cov-append` option. This option appends coverage data to existing `.coverage` file. 

```shell
$ pytest --cov-append --cov=app tests/
```

This command will run tests in parallel, and append coverage data to `.coverage` file.

To generate coverage report, we can use `coverage` command-line utility.

```shell
$ coverage report
```

