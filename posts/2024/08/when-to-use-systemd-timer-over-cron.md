<!--
.. title: How (and when) to use systemd timer instead of cronjob
.. slug: guide-systemd-timer-cronjob
.. date: 2024-08-05 13:07:50 UTC+05:30
.. tags: devops, automation
.. category: programming
.. link: 
.. description: How to replace cronjobs with systemd timer and what are benefits of it.
.. type: text
-->

### Introduction

```shell
* * * * * bash demo.sh
```

Just a single line of code is sufficient to schedule a cron job. However, there are some scenarios where I find systemd timer more useful than cronjob.

### How to use systemd timer

We need to create a service file(contains the script to be run) and a timer(contains the schedule).

```shell
# demo.service
[Unit]
Description=Demo service

[Service]
ExecStart=bash demo.sh
```
  
```shell
# demo.timer
[Unit]
Description=Run myscript.service every 1 minutes

[Timer]
OnBootSec=1min
OnUnitActiveSec=1min

[Install]
WantedBy=multi-user.target
```

We can copy these files to `/etc/systemd/system/` and enable the timer.

```shell
$ sudo cp demo.service demo.timer /etc/systemd/system/

$ sudo systemctl daemon-reload

$ sudo systemctl enable --now demo.timer
```

We can use `systemctl` to see when the task is executed last and when it will be executed next.

```shell
$ sudo systemctl list-timers --all
```

<img src="/images/systemd-timer-cronjob.png" alt="systemd timer" />


### Use Cases

- Singleton - In the above example, lets say `demo.sh` takes ~10 minutes to run. With cron job, in ten minutes we will have 10 instances of `demo.sh` running. This is not ideal. With systemd timer, it will ensure only one instance of `demo.sh` is running at a time.

- On demand runs - If we want to test out the script/job, systemd allows us to immediately run it with usual `systemctl start demo` without needing to run the script manually.

- Timer - With cron, we can run tasks upto a minute precision. Timer can run tasks till `second` level precision. 

```shell
[Timer]
OnCalendar=*-*-* 15:30:15
```

In addition to that, we can run tasks based on system events. For example, we can run a script 15 minutes from reboot.

```shell
[Timer]
OnBootSec=15min
```


### Conclusion

Systemd timer is a powerful tool that can replace cronjob in many scenarios. It provides more control and flexibility over cronjob. However, cronjob is still a good choice for simple scheduling tasks.
