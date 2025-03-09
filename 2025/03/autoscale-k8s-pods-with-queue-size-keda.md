<!--
.. title: Autoscale k8s pods with queue size (KEDA)
.. slug: autoscale-k8s-pods-with-queue-size-keda
.. date: 2025-03-07 11:37:52 UTC+05:30
.. tags: devops, kubernetes
.. category: DevOps
.. link: 
.. description: 
.. type: text
-->

### Introduction

Kubernetes(k8s) is a popular container orchestration tool and it provides Horizontal Pod Autoscaler(HPA) to scale pods based on CPU and Memory usage. 

To scale pods based on the queue size we can use [KEDA](https://keda.sh/).

### Setup

As written earlier, we can use k3d and setup k8s cluster with a single command anywhere.

Once, 
