<!--
.. title: Provisioning Laptop(s) With Ansible
.. slug: provisioning-laptop-ansible
.. date: 2017-03-11 14:16:32 UTC
.. tags: ansible, python, ubuntu
.. category: tech, automation,
.. link:
.. description: How to automatically sync configuration between systems?
.. type: text
-->


Setting up a new laptop manually takes a lot of time and there is a good chance of forgetting tweaks made to configuration files. It is good idea to automate it via a shell script or using configuration management tools like Ansible. It also makes easy to sync configuration across multiple systems.


## Why Ansible?

Ansible is lightweight and provides only a thin layer of abstraction. It connects to hosts via ssh and pushes changes. So, there is no need to setup anything on remote hosts.


## Writing A Playbook

You should check out Ansible documentation to get familiar with ansible and [writing playbooks](https://docs.ansible.com/ansible/playbooks.html). Ansible uses yaml format for playbooks and it's human readable. Here is a simple playbook to install redis on ubuntu server.

```
hosts: all
sudo: True

tasks:
  - name: install redis
    apt: name=redis-server update_cache=yes
```

Here is [a playbook](https://github.com/ChillarAnand/01/blob/master/ubuntu/config/playbooks/setup.yml) which I use to configure my laptop. As the playbook needs to run locally, just run

```
ansible-playbook laptop-setup.yml -i localhost, -c local
```


## Bootstrap Script

To automate provisioning, a bootstrap script is required to make sure python, ansible are installed, to download and execute playbook on the system.

```
sudo apt update --yes
sudo apt install --yes python python-pip

sudo apt install --yes libssl-dev
sudo -H pip install ansible

wget -c https://path/to/playbook.yml

sudo ansible-playbook setup.yml -i localhost, -c local
```

Now, to provision a laptop, just run the bootstrap script.

```
sh -c "$(wget https://path/to/bootstrap_script.sh"
```

You can use a git repo to track changes in playbook and bootstrap script. If you are using multiple laptops, running bootstrap script on them will make sure everything is synced across them.
