<!--
.. title: Minimum Viable Testing - Get Maximum Stability With Minimum Effort
.. slug: minimum-viable-testing-risk-based
.. date: 2020-12-31 19:23:11 UTC+06:30
.. tags: testing
.. category:
.. link:
.. description: How to get more stability of the product with less effort?
.. type: text
-->

### Introduction

Even though Test Driven Development(TDD)[^tdd] saves time & money in the long run, there are many excuses why developers don't test the software. In this article, lets look at Minimum Viable Testing(aka Risk-Based Testing)[^mvt] and how it helps to achieve maximum stability with minimum effort.


### Minimum Viable Testing

Pareto principle states that 80% of consequences come from 20% of the causes. In software proucts, 80% of the users use 20% of the features. A bug in these 20% features is likely to cause higher impact than the rest. It makes sense to prioritize testing of these features than the rest.

Assessing the importance of a feature or risk of a bug depends on the product that we are testing. For example, in a project a paid feature gets more importance than free feature.

In TDD, we start with writing tests and then writing code. Compared to TDD, MVT consumes less time. When it comes to testing, there are unit tests, integration tests, snapshot tests, ui tests and so on.

When getting started with testing, it is important to have integration tests in place to make sure if something is working. Also the cost of integration tests is much cheaper compared to unit tests.

Most of the SAAS products have a web/mobile application and an API server to handle requests for the front end applications. Having UI tests for the applications and integration tests for APIs for the most crucial functionality should cover the ground. This will make sure any new code that is being pushed doesnt break the core functionality.


### Conclusion

Even though RBT helps with building a test suite quicker that TDD, it should be seen as an alternate option to TDD. We should see RBT as a starting point for testing from which we can take next step towards achieving full stability for the product.



[^tdd]: [https://en.wikipedia.org/wiki/Test-driven_development](https://en.wikipedia.org/wiki/Test-driven_development)

[^mvt]: [https://en.wikipedia.org/wiki/Risk-based_testing](https://en.wikipedia.org/wiki/Risk-based_testing)
