<!--
.. title: How To Deploy Mirth Connect To Kubernetes
.. slug: deploy-mirth-to-kubernetes
.. date: 2020-09-30 23:25:46 UTC+05:30
.. tags: devops, kubernetes, HealthIT
.. category: programming
.. link:
.. description: How to Deploy NextGen Connect (aka Mirth Connect) to a Kubernetes cluster.
.. type: text
-->


### Introduction

NextGen Connect(previously Mirth Connect) is widely used integration engine for information exchange in health-care domain. In this article, let us see how to deploy Mirth Connect to a Kubernetes cluster.


### Deployment To k8s

From version 3.8, NextGen has started providing official docker images for Connect[^nc]. By default, Connect docker exposes 8080, 8443 ports. We can start a Connect instance locally, by running the following command.


```sh
$docker run -p 8080:8080 -p 8443:8443 nextgenhealthcare/connect
```


We can use this docker image and create a k8s deployment to start a container.

```
---
apiVersion: apps/v1beta1
kind: Deployment
metadata:
  name: mirth-connect
  namespace: default
spec:
  template:
    spec:
      containers:
      - name: mirth-connect
        image: docker.io/nextgenhealthcare/connect
        ports:
        - name: http
          containerPort: 8080
        - name: https
          containerPort: 8443
        - name: hl7-test
          containerPort: 9001
        env:
          - name: DATABASE
            value: postgres
          - name: DATABASE_URL
            value: jdbc:postgresql://avilpage.com:5432/mirth_db
```

This deployment file can be applied on a cluster using `kubectl`.

```
$ kubectl apply -f connect-deployment.yaml
```

To access this container, we can create a service to expose this deployment to public.


```
---
apiVersion: v1
kind: Service
metadata:
  name: mirth-connect
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-ssl-cert: arn:aws:acm:ap-south-1:foo
    service.beta.kubernetes.io/aws-load-balancer-ssl-ports: "443"
    external-dns.alpha.kubernetes.io/hostname: connect.avilpage.com
spec:
  type: LoadBalancer
  selector:
    app: mirth-connect
  ports:
    - name: http
      port: 80
      targetPort: 8080
      protocol: TCP
    - name: https
      port: 443
      targetPort: 8443
      protocol: TCP
    - name: hl7-test
      port: 9001
      targetPort: 9001
      protocol: TCP
```

This will create a load balancer in AWS through which we can access mirth connect instance. If an ingress controller is present in the cluster, we can use it directly instead of using a seperate load balancer for this service.

Once Mirth Connect is up & running, we might have to create HL7 channels running on various ports. In the above configuration files, we have exposed 9001 HL7 port for testing of channel. Once we configure Mirth Channels, we need to expose appropriate ports in deployment as well as service similiar to this.

### Conclusion

Earlier, there were no official docker images for Mirth Connect and it was bit diffucult to dockerize Mirth Connect and deploy it. With the release of official Docker images, deploying Mirth Connect to k8s or any other container orchestration platform has become much easier.



[^nc]: [https://hub.docker.com/r/nextgenhealthcare/connect/](https://hub.docker.com/r/nextgenhealthcare/connect/)
