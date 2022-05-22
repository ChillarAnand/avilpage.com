<!--
.. title: Continuous Deployment To Kubernetes With Skaffold
.. slug: setup-continuous-deployment-with-kubernetes
.. date: 2020-04-30 16:45:36 UTC+05:30
.. tags: kubernetes, devops
.. category: tech, programming
.. link:
.. description: How to setup continuous deployment to kubernetes in a continuous integration environment?
.. type: text
-->


In this article, let us see how to setup a continuous deployment pipeline to Kubernetes in CircleCI using Skaffold.


### Prerequisites

You should have a kubernetes cluster in a cloud environment or in your local machine. Check your cluster status with the following commands.

```sh
$ kubectl cluster-info
$ kubectl config get-contexts
```

You should know how to manually deploy your application to kubernetes.

```sh
# push latest docker image to container registry
$ docker push chillaranand/library

# deploy latest image to k8s
$ kubectl apply -f app/deployment.yaml
$ kubectl apply -f app/service.yaml
```


### Skaffold

[Skaffold](https://github.com/GoogleContainerTools/skaffold) is a CLI tool to facilitate continuous development and deployment workflows for Kubernetes applications.

Skaffold binaries are available for all platforms. Download the binary file for your OS and move it to bin folder.

```sh
$ curl -Lo skaffold https://storage.googleapis.com/skaffold/releases/latest/skaffold-darwin-amd64
$ chmod +x skaffold
$ sudo mv skaffold /usr/local/bin
```

Inside your project root, run `init` command to generate a config file. If your project has k8s manifests, it will detect them and include it in the configuration file.

```sh
$ skaffold init
Configuration skaffold.yaml was written

$ cat skaffold.yaml
apiVersion: skaffold/v2beta1
kind: Config
metadata:
  name: library
build:
  artifacts:
  - image: docker.io/chillaranand/library
deploy:
  kubectl:
    manifests:
    - kubernetes/deployment.yaml
    - kubernetes/service.yaml
```

To deploy latest changes to your cluster, run

```sh
$ skaffold run
```

This will build the docker image, push to registry and will apply the manifests in the clusters. Now, k8s will pull the latest image from the registry and create a new deployment.


### CircleCI Workflow


```sh
version: 2.1

orbs:
  aws-cli: circleci/aws-cli@0.1.19
  kubernetes: circleci/kubernetes@0.11.0

commands:
  kubernetes-deploy:

    steps:
      - setup_remote_docker

      - aws-cli/setup:
          profile-name: default

      - kubernetes/install-kubectl:
          kubectl-version: v1.15.10

      - checkout

      - run:
          name: container registry log in
          command: |
            sudo $(aws ecr get-login --region ap-south-1 --no-include-email)

      - run:
          name: install skaffold
          command: |
            curl -Lo skaffold https://storage.googleapis.com/skaffold/releases/latest/skaffold-linux-amd64
            chmod +x skaffold
            sudo mv skaffold /usr/local/bin

      - run:
          name: update kube config to connect to the required cluster
          command: |
            aws eks --region ap-south-1 update-kubeconfig --name demo-cluster

      - run:
          name: deploy to k8s
          command: |
            skaffold run
```

CircleCI orbs are shareable packages to speed up CI setup. Here we are using aws-cli, kubernetes orbs to easily install/setup them inside the CI environment.

Since CircleCI builds run in a docker container, to run docker commands inside container, we have to specify `setup_remote_docker` key so that a seperate environment is created for it.

Remaining steps are self explainatory.


### Conclusion

Here we have seen how to setup CD to kubernetes in CircleCI. If we want to setup this another CI like Jenkins or Travis, instead of using orbs, we have to use system package mangers like apt-get to install them. All others steps will remain same.
