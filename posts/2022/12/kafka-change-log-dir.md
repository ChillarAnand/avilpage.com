<!--
.. title: Change Kafka Log Directory & Format It
.. slug: change-kafka-log-dir-format
.. date: 2022-12-24 12:19:41 UTC+05:30
.. tags: kafka, debugging, message-broker
.. category: backend
.. link: 
.. description: How to change apache kafka log directory and format it?
.. type: text
-->

### Problem Statement

On my local Mac, I was using Kafka to pass messages between various applications. Due to some reason, when I tried to start Kafka recently, it was failing to start and here are the relevant error logs.

```bash
[2022-12-23 11:57:06,217] WARN [Controller 1] writeNoOpRecord: failed with unknown server exception RuntimeException at epoch 139 in 5198 us.  Renouncing leadership and reverting to the last committed offset 927938. (org.apache.kafka.controller.QuorumController)

[2022-12-23 11:57:06,536] ERROR [Controller 1] registerBroker: unable to start processing because of NotControllerException. (org.apache.kafka.controller.QuorumController)

[2022-12-23 12:23:35,834] ERROR [RaftManager nodeId=1] Had an error during log cleaning (org.apache.kafka.raft.KafkaRaftClient)
org.apache.kafka.common.errors.OffsetOutOfRangeException: Cannot increment the log start offset to 927939 of partition __cluster_metadata-0 since it is larger than the high watermark 926507
[2022-12-23 12:23:36,035] WARN [Controller 1] writeNoOpRecord: failed with unknown server exception RuntimeException at epoch 294 in 137 us.  Renouncing leadership and reverting to the last committed offset 927938. (org.apache.kafka.controller.QuorumController)
java.lang.RuntimeException: Cant create a new in-memory snapshot at epoch 926507 because there is already a snapshot with epoch 927938

[2022-12-23 12:23:36,252] ERROR Exiting Kafka due to fatal exception during startup. (kafka.Kafka$)

```


### Debugging

I tried to figure out the exact root cause. After multiple failed attempts, I decided to change the log directory temporarily and go ahead for now.

### Solution

I create a new temporary directory and set the log directory to that.

```bash
$ mkdir /tmp/kafka-logs

# inside server.properties
log.dirs=/tmp/kafka-logs
```

When I started the Kafka server, it failed.

```bash
$ kafka-server-start server.properties

[2022-12-23 12:30:50,018] ERROR Exiting Kafka due to fatal exception (kafka.Kafka$)
org.apache.kafka.common.KafkaException: No `meta.properties` found in /tmp/ (have you run `kafka-storage.sh` to format the directory?)
```

I ran the `kafka-storage` script to format the directory. First, we need to get the cluster-id. Since we already know the old kafa-logs directory, we can get the cluster-id from there.

```bash
$ cat ~/homebrew/var/lib/kraft-combined-logs/meta.properties 
#
#Thu Oct 20 11:48:12 IST 2022
cluster.id=5MB5lq-XT-6JzQqJeIuhWQ
node.id=1
version=1      
```

Now, we can format the new directory.

```bash
$ kafka-storage format --config server.properties --cluster-id 5MB5lq-XT-6JzQqJeIuhWQ

Formatting /tmp/kafka-logs/ with metadata.version 3.3-IV3.
```

After changing log directory, Kafka has started working.

```bash
$ kafka-start-server /path/to/server.properties
```

Since I have changed log directory all older messages are lost. Since I am doing this on my local machine, it is fine. Need to revisit it to debug further.
