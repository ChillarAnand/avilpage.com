<!--
.. title: Record Resource Usage of Single Process
.. slug: record-resource-usage-per-process
.. date: 2023-04-14 06:18:37 UTC+05:30
.. tags: devops, mac, linux
.. category: DevOps
.. link: 
.. description: How to monitor and save CPU, RAM, network and disk usage of a single process on Linux, Mac or Windows?
.. type: text
-->

### Introduction

On Linux & Mac, we can use an inbuilt `top` command line tool to monitor the resource usage of a single process in real time. 

```bash
# On Linux, for a given pid
$ top -p 1234

# On Mac, for a given pid
$ top -pid 1234
```

In this article, we will see how to record and plot resource usage of a single process using `top` and a Python package called psrecord[^psrecord].

### Record Resource Usage

In some cases, we need to record the resource usage of a process to use it later. For example, we can use this data to find out the peak resource usage of a process. For this, we can use `top` to log resource usage into a text file. 

```bash
# On Linux, for a given pid
$ top -p 1234 -b -d 1 > top.log

# On Mac, for a given pid
$ top -l 0 -s 1 -pid 32515 | awk 'NR%13==0; fflush(stdout)' > top.log
```

Once we have the log file, we can view the raw data or we can plot the resource usage by using tools like `gnuplot` or `matplotlib`.

Instead of using `top` command, we can use `psrecord` to record the resource usage of a process. `psrecord` is a Python package that can be installed all using `pip`. 

```bash
$ python -m pip install psrecord
```

Once installed, we can use `psrecord` to record the resource usage of a process. 

```bash
# record resource usage of a process with pid 1234
$ psrecord 1234 --log top.log

# start and record resource usage of a process
$ psrecord python script.py --plot graph.png
```

We can view the raw data in the log file.

```bash
# view raw data
$ head top.log
❯ head a.txt
# Elapsed time   CPU (%)     Real (MB)   Virtual (MB)
       0.000        0.000        5.000   399461.438
       0.000       93.700        5.000   399461.438
       0.000       96.300        5.000   399461.438
       0.000       91.900        5.000   399461.438
```

Here is the generated graph.

<p align="center">
<img src="/images/single-proc-resource.png" alt="single-proc-resource" />
</p>


### Conclusion

In this article, we have seen how to record and plot resource usage of a single process using top(inbuilt tool), psrecord(3rd party package).


[^psrecord]: [https://pypi.org/project/psrecord/](https://pypi.org/project/psrecord/)