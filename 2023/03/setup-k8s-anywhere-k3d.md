<!--
.. title: Setup Kubernetes Anywhere with Single Command
.. slug: setup-k8s-anywhere-k3d
.. date: 2023-03-04 02:55:27 UTC+05:30
.. tags: kubernets, devops, linux
.. category: 
.. link: 
.. description: 
.. type: text
-->

<div class="embed-responsive embed-responsive-16by9">
<iframe class="embed-responsive-item" src="https://www.youtube.com/embed/Vo0mAsXe-hI" allowfullscreen>
</iframe>
</div>
<br />


### Introduction

In an earlier article, we have seen how to set up [Kubernetes on M1 Mac](/2022/10/local-kubernetes-with-k3s-on-mac.html). That involved spinning up a VM and installing Kubernetes[^kubernetes] on it. In this article, we will see how to set up Kubernetes directly on Docker so that we can use the same set-up on any operating system.

### Prerequisites

Ensure you have Docker installed on your system. If you are on a Mac or Windows, you can install Docker Desktop[^docker-desktop].

### k3s/k3d

k3s[^k3s] is a lightweight Kubernetes distribution by Rancher. It is a single binary that can be run on any Linux machine. But it doesn't work on Mac or Windows.

k3d[^k3d] is a wrapper around k3s that allows you to run k3s on Docker. It is a great option for running Kubernetes on your local machine.

### Installation

k3d can be installed using the following command:

```shell
$ brew install k3d  # mac
$ chocolatey install k3d  # windows
$ curl -s https://raw.githubusercontent.com/k3d-io/k3d/main/install.sh | bash # linux
```

Once it is installed, we can create a cluster using the following command:

```shell
$ k3d cluster create demo
```

This will launch a cluster with a single node. We can also setup a multi-node cluster using the following command:

```shell
$ k3d cluster create demo --servers 3 --agents 2
```

We can verify the cluster is up and running using the following command:

```shell
$ kubectl get nodes
```

We can also use GUI tools like Lens to manage and navigate the cluster. In the above video we have used Lens to create a Jenkins deployment as well.

### Conclusion

In this article, we have seen how to set up Kubernetes on Docker. This is a great option for running Kubernetes on your local machine. We can also use this to run production setup for small applications.

[^kubernetes]: [https://kubernetes.io/](https://kubernetes.io/)

[^docker-desktop]: [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)

[^k3s]: [https://k3s.io/](https://k3s.io/)

[^k3d]: [https://k3d.io/](https://k3d.io/)
