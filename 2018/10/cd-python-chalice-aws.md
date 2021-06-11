<!--
.. title: Setup Continous Deployment For Python Chalice
.. slug: cd-python-chalice-aws
.. date: 2018-10-30 21:21:21 UTC+06:30
.. tags: aws, python, devops
.. category:
.. link:
.. description: How to setup continous deployment pipeline on AWS for chalice framework
.. type: text
-->

### Outline

[Chalice](https://pypi.org/project/chalice/) is a microframework developed by Amazon for quickly creating and deploying serverless applications in Python.

In this article, we will see how to setup continous deployment with [GitHub](https://github.com) and [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html).


### CD Setup

Chalice provides cli command `deploy` to deploy from local system.

Chalice also provides cli command `generate-pipeline` command to generate CloudFormation template. This template is useful to automatically generate several resources required for AWS pipeline.

<p align="center">
<img src="/images/aws-python-pipeline.png"  height="300px" width="600" />
</p>

This by default uses CodeCommit repository for hosting code. We can use GitHub repo as a source instead of CodeCommit.

Chalice by default provides a build file to package code and push it to S3. In the deploy step, it uses this artifact to deploy the code.

We can use a custom buildpsec file to directly deploy the code from build step.

```yml
version: 0.1

phases:
  install:
    commands:
      - echo Entering the install phase
      - echo Installing dependencies
      - sudo pip install --upgrade awscli
      - aws --version
      - sudo pip install chalice
      - sudo pip install -r requirements.txt

  build:
    commands:
      - echo entered the build phase
      - echo Build started on `date`
      - chalice deploy --stage staging
```

This buildspec file install requirements and deploys chalice app to staging. We can add one more build step to deploy it production after manual intervention.


### Conclusion

We have seen how to setup continous deployment for chalice application with GitHub and AWS CodePipeline.
