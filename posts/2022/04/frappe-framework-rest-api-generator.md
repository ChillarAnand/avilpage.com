<!--
.. title: Using Frappe Framework As REST API Generator
.. slug: frappe-framework-rest-api-generator
.. date: 2022-04-30 19:01:53 UTC+05:30
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

### Introduction

When a company plans to build a mobile application and/or a web application, they need to create REST APIs to store data. This is a common requirement for CRUD applications.

In the Python ecosystem, there are several projects like Django Rest Framework, Flask-RESTful, FastApi which does the heavy lifting of implementing REST APIs. In other ecosystems, there are similar projects/frameworks for this job.

### REST API Generators

By using the above mentioned frameworks, developers can build REST APIs at a faster rate. Still, developers have to develop and maintain code for these APIs.

To avoid even this work, there are REST API generators like postgrest[^postgrest], prest which can instantly generate REST APIs by inspecting database schema. With these, developers just have to design the DB schema and these tools take care of generating APIs without writing a single line of code.

In this post, let us see how Frappe framework can be used as a REST API generator and what are the advantages of using Frappe.

### Frappe Framework

Frappe framework is meta data driven low code, web framework written in Python and Javascript.


#### Web UI

Frappe framework provides web UI to create models(called doctypes in Frappe) and it provides REST API[^rest_api] for all the models out of the box.


There is no need to write manual SQL queries to manage schema. With some training even non-developers can even manage models in Frappe.


#### Roles & Permissions

With traditional API generators, managing roles & permissions involves additional development and maintenance costs. Frappes comes with an authentication system and it has support for role based permissions out of the box. From the web UI, users can manage roles & permissions.


#### Hooks

Even though REST API generators give API out of the box, there will be scenarios where custom business logic needs to be hooked in for various events. 
In such scenarios, developers end up using an alternate framework/tool to manage hooks and business logic.

Frappe provides server scripts by which arbitrary python code can be executed dynamically based on model events. There is no need to set up another framework for these things.

#### Utilities

Frappe framework comes with a lot of utilities like Job Queues, Schedulers, Admin interface, socket.io etc. As the project grows and the need evolves, Frappe has all the common utilities that are required for a web application development.

#### Conclusion

When a company wants to build a solution to a problem, it should focus most of the time in solving that problem instead of wasting their time on building CRUD interfaces or REST APIs.


Frappe framework was designed to rapidly build web applications with low code. If you need a REST API generator and some additional functionality for the REST APIs, Frappe framework fits the bill and reduces a lot of development time.


[^postgrest]: [https://github.com/PostgREST/postgrest](https://github.com/PostgREST/postgrest)

[^rest_api]: [https://frappeframework.com/docs/user/en/api/rest](https://frappeframework.com/docs/user/en/api/rest)
