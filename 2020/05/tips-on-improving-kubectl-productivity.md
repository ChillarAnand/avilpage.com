<!--
.. title: Tips On Improving kubectl Productivity
.. slug: tips-on-improving-kubectl-productivity
.. date: 2020-06-31 18:42:00 UTC+06:30
.. tags: kubenetes, devops
.. category:
.. link:
.. description: How to improve your productivity with kubectl from any shell and using some k8s specific tools.
.. type: text
-->

`kubectl` is CLI tool to control Kubernetes clusters. As we start using kubectl to interact with mutliple clusters, we end up running lengthy commands and even running multiple commands for simple tasks like running a shell in a container.

In this article, lets learn few tips to improve our productivity when using kubectl.


### Aliases

Aliases in general improve the productivity when using a shell.

kubectl provides shortcuts for commands. For example,

```sh
# instead of running full command
$ kubectl get services

# we can use short hand version
$ kubectl get svc
```

It also provides completion for commands.

```sh
# enable completion for zsh
$ source <(kubectl completion zsh)

# type `kubectl ` and hit `<TAB>` will show possible options
$ kubectl
annotate       attach         cluster-info
api-resources  auth           completion
api-versions   autoscale      config
apply          certificate    convert

# type `kubectl g`, and hit `<TAB>` will show possible options
$ kubectl get
```

However, setup up aliases for most commanly used commands will lot of time.

```sh
alias k='kubectl'

alias kdp='kubectl describe pod'
alias kgp='kubectl get pods'
alias kgpa='kubectl get pods --all-namespaces'
alias ket='kubectl exec -it'
alias wkgp='watch -n1 kubectl getp pods'

alias kga='kubectl get all'
alias kgaa='kubectl get all --all-namespaces'

alias kaf='kubectl apply -f'

alias kcgc='kubectl config get-contexts'
alias kccc='kubectl config current-context'
```

If you don't write your own aliases, there is [kubectl-aliases](https://github.com/ahmetb/kubectl-aliases) which provides exhuastive list of aliases. We can source this file in rc file and start using them.


### Use Functions

Even though aliases help us to run lengthy commands with an alias, there are times where we have to run multiple commands to get things done for a single task.

For example, to view kubenetes dashboard, we have to get the token, start proxy server and then open the url in browser. We can write a simple function as shown below to do all of that.

```sh
kp() {
    kubectl -n kubernetes-dashboard describe secret $(kubectl -n kubernetes-dashboard get secret | grep admin-user | awk '{print $1}') | grep 'token:' | awk '{print $2}' | pbcopy
    open http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/
    kubectl proxy
}
```

Now from the shell, when we run `kp`, it function will copy the token to clipboard, open kubernetes dashboard in browser and will start the proxy server.


### Use Labels

To describe a pod or tail logs from a pod, we can use pod names.

```sh
$ kubectl get pods
NAME                             READY   STATUS
hello-world-79d794c659-tpfv2     1/1     Running


$ kubectl describe pod hello-world-79d794c659-tpfv2

$ kubectl logs -f pod/hello-world-79d794c659-tpfv2
```

When the app gets updated, the name of pod also updates. So, instead of using pod name, we can use pod labels.

```sh
$ kubectl describe pod -l=hello-world

$ kubectl logs -f -l=pod/hello-world
```


### Kubectl Tools

k8s has a good ecosystem and the following packages are aimed to make certain k8s tasks easier.

[kubectl-debug](https://github.com/aylei/kubectl-debug) - Debug pod by a new container with all troubleshooting tools pre-installed.

[kube-forwarder](https://github.com/pixel-point/kube-forwarder) - Easy to use port forwarding manager.

[stern](https://github.com/wercker/stern) - Multi pod and container log tailing.

[kubectx](https://github.com/ahmetb/kubectx) - Quick way to switch between clusters and namespaces.

[kubebox](https://github.com/astefanutti/kubebox) - Terminal and Web console for Kubernetes.

[k9s](https://github.com/derailed/k9s) - Interactive terminal UI.

[kui](https://github.com/IBM/kui) - Hybrid CLI/UI tool for k8s.

[click](https://github.com/databricks/click) - Interactive controller for k8s.

[lens](https://github.com/lensapp/lens) - Stand alone corss platform k8s IDE.


### Conclusion

In this article we have seen some useful methods as well as some tools to improve productivity with kubectl. If you spend a lot of time interacting with kubernetes cluster, it is important to notice your workflows and find better tools or ways to improve productivity.
