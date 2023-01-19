<!--
.. title: A Typo Got Me $100 Bug Bounty
.. slug: typo-lead-to-bug-bounty
.. date: 2021-10-25 08:52:19 UTC+05:30
.. update: 2023-01-18 08:52:19 UTC+05:30
.. tags: security, HealthIT
.. category: security
.. link:
.. description: How a typo got me a bug bounty.
.. type: text
-->

### Introduction

On a lazy evening, while on a call with a friend, I made a typo while entering the url. Instead of typing [http://app-00421.on-aptible.com](), I typed [http://app-00412.on-aptible.com]()[^aptible].


In this article, lets see how this typing mistake got me a bug bounty.


### Vulnerability

A [bug bounty program]()[^bb] is a deal offered by companies by which individuals can receive recognition and compensation for reporting bugs, security exploits and vulnerabilities.

Aptible provides HIPAA[^hipaa] compliant PAAS platform so that healthcare companies can deploy their apps without compliance hassle.

After deploying an application on aptible, users can create an endpoint for public access. For this purpose, atpible generates domain names in sequential order.

Due to this, a set of publicly exposed servers will have incremental domain names. A lot of companies use these sequentially generated domain names for staging & testing purposes. In general, many companies don't bother about implementing security best practices on non-production servers.

When I was trying to access a demo site at [http://app-00421.on-aptible.com](), I made a typo and visited [http://app-00412.on-aptible.com](). This site was a staging site of some other company without any authentication. The company's source code, AWS keys and a lot of sensitive information was publicly accessible.

I quickly sent an email to that company regarding this issue and they took their site offline. As per [Aptible disclosure policy]()[^disclosure], this bug is out of scope. However I sent an email to their team regarding the severity of the issue. Since sequential domain names are generating additional target surface for attackers, I suggested to move to random urls.

For this disclosure, they have provided a bounty of 100$ and Aptible decided to move away from sequential domain names.



[^aptible]: URL has been changed for anonymity.

[^bb]: [https://en.wikipedia.org/wiki/Bug_bounty_program](https://en.wikipedia.org/wiki/Bug_bounty_program)

[^hipaa]: [HIPAA - Wikipedia](https://en.wikipedia.org/wiki/Health_Insurance_Portability_and_Accountability_Act)

[^disclosure]: [https://www.aptible.com/legal/responsible-disclosure/](https://www.aptible.com/legal/responsible-disclosure/)
