<!--
.. title: macOS - Log & track historical CPU, RAM usage
.. slug: macos-log-track-cpu-ram-usage
.. date: 2024-06-01 01:48:02 UTC+05:30
.. tags: devops, python, macbook
.. category: DevOps
.. link: 
.. description: How to log, track and view historical CPU, RAM, network and disk usage in macOS. 
.. type: text
-->

![macOS - Log CPU & RAM history](/images/mac-log-cpu-ram-grafana.png)

In macOS, we can use inbuilt `Activity Monitor` or third party apps like `Stats` to check the live CPU/RAM usage. But, we can't track the historical CPU & memory usage. `sar`, `atop` can track the historical CPU & memory usage. But, they are not available for macOS.


### Netdata

Netdata[^Netdata] is an open source observability tool that can monitor CPU, RAM, network, disk usage. It can also track the historical data. 

Unfortunately, it is not stable on macOS. I tried installing it on multiple macbooks, but it didn't work. I raised an issue[^netdata_issue] on their GitHub repository and the team mentioned that macOS is a low priority for them.


### Glances

Glances[^Glances] is a cross-platform monitoring tool that can monitor CPU, RAM, network, disk usage. It can also track the historical data.

We can install it using Brew or pip.

```shell
$ brew install glances

$ pip install glances
```

Once it is installed, we can monitor the resource usage using the below command.

```shell
$ glances
```

![macOS - Log CPU & RAM history](/images/mac-log-cpu-ram-glances.png)

Glances can log historical data to a file using the below command.

```shell
$ glances --export-csv /tmp/glances.csv
```

In addition to that, it can log data to services like influxdb, prometheus, etc.

Let's install influxdb and export stats to it.

```shell
$ brew install influxdb
$ brew services start influxdb
$ influx setup

$ python -m pip install influxdb-client

$ cat glances.conf
[influxdb]
host=localhost
port=8086
protocol=http
org=avilpage
bucket=glances
token=secret_token

$ glances --export-influxdb -C glances.conf
``` 

We can view stats in the influxdb from Data Explorer web UI at [http://localhost:8086](http://localhost:8086).

![macOS - Log CPU & RAM history](/images/mac-log-cpu-ram-influxdb.png)

Glances provides a prebuilt Grafana dashboard[^grafana_dashboard] that we can import to visualize the stats. 

From Grafana -> Dashboard -> Import, we can import the dashboard using the above URL.

![macOS - Log CPU & RAM history](/images/mac-log-cpu-ram-grafana.png)


### Conclusion

In addition to InfluxDB, Glances can export data to ~20 services. So far, it is the best tool to log, track and view historical CPU, RAM, network and disk usage in macOS. The same method works for Linux and Windows as well.


[^Netdata]: [https://github.com/netdata/netdata](https://github.com/netdata/netdata)
[^netdata_issue]: [https://github.com/netdata/netdata/issues/16696](https://github.com/netdata/netdata/issues/16696)

[^Glances]: [https://github.com/niolargo/glances](https://github.com/nicolargo/glances)
[^grafana_dashboard]: [https://glances.readthedocs.io/en/latest/gw/influxdb.html#grafana](https://glances.readthedocs.io/en/latest/gw/influxdb.html#grafana)

[//]: # ([^InfluxDB]: [https://www.influxdata.com/]&#40;https://www.influxdata.com/&#41;)
[//]: # ([^Grafana]: [https://grafana.com/]&#40;https://grafana.com/&#41;)
