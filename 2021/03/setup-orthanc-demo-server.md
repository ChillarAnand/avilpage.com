<!--
.. title: Mastering PACS/DICOM #2 - Setup Orthanc Demo Server
.. slug: setup-orthanc-demo-server
.. date: 2021-03-26 06:00:00 UTC+05:30
.. tags: dicom, HealthIT
.. category: programming
.. link:
.. description: Setup orthanc pacs & dicom server locally or on aws for learning dicom.
.. type: text
-->

This is a series of [articles on mastering Dicom](/tags/dicom.html). In the earlier article, we have learnt how PACS/DICOM simplifies the clinical work flow.

In this article, lets setup a dicom server so that we have a server to play around with Dicom files.


### Orthanc Server

There are several Dicom servers like Orthanc, Dicoogle etc. [Orthanc](https://en.wikipedia.org/wiki/Orthanc_(server)) is a lightweight open source dicom server and is widely used by many Health care organisations.

Sébastien Jodogne, original author of Orthanc maintains docker images. We can use these images to run Orthanc server locally.

Ensure docker is installed on the machine and then run the following command to start Orthanc server.

```
$ docker run -p 4242:4242 -p 8042:8042 --rm \
    jodogne/orthanc-python
```

Once the server is started, we can visit [http://localhost:8042](http://localhost:8042) and explore Orthanc server.


### Heroku Deployment

Heroku is PAAS platform which supports docker deployments. Lets deploy Orthac server to Heroku for testing.

By default, Orthanc server runs on 8042 port as defined in the config file. Heroku dynamically assigns port for the deployed process.

We can write a shell script which will read port number from environment variable, replace it in Orthanc configuration file and then start Orthanc server.

```
#! /bin/sh

set -x

echo $PORT

sed 's/ : 8042/ : '$PORT'/g' -i /etc/orthanc/orthanc.json

Orthanc /etc/orthanc/
```

We can use this shell script as entry point in docker as follows.

```
FROM jodogne/orthanc-python

EXPOSE $PORT

WORKDIR /app
ADD . /app

ENTRYPOINT [ "./run.sh" ]
```

We can create a new app in heroku and we can deploy this container.

```
$ heroku apps:create orthanc-demo

$ heroku container:push web
$ heroku container:release web
```

Once the deployment is completed, we can access our app from the endpoint provided by heroku. Here is a [orthanc demo server](https://orthanc-demo.herokuapp.com) running on heroku.


### Conclusion

In this article, we have learnt how to setup Orthanc server and deployed it to Heroku. In the next article, let dig deeper into dicom protocol by upload/accessing dicom files to the server.
