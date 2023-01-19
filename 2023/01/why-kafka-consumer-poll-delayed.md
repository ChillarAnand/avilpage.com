<!--
.. title: Why There Is A Delay In Kafka Consumer Poll?
.. slug: why-kafka-consumer-poll-delayed
.. date: 2023-01-09 09:17:45 UTC+05:30
.. tags: kafka, debugging
.. category: programming
.. link: 
.. description: After starting confluent kafka consumer with poll, sometimes there will be a delay in consuming the messages. Let's see why this happens and how to fix it. 
.. type: text
-->

### Problem Statement

- Sometimes due to error in processing the messages, kafka consumer will exit.
- During graceful restarts or upgrades, kafka consumer will restart.

In such scenarios, when consumer is started again, it will start consuming the messages from the last committed offset. This is the default behavior of kafka consumer. If we use `consumer.poll()` to consumer messages, there will be a huge delay in consuming the first message.

Let's see why this happens and how to fix this issue.

### Debugging

When a new consumer starts, Kafka will undergo the following steps to find the last committed offset for the consumer group. There is also a rebalance process that happens when a new consumer joins the group. This rebalancing takes a lot of time.

To avoid rebalancing, we can use `auto.offset.reset` property to set the offset to `earliest` or `latest`. This will avoid the rebalancing process and the consumer will start consuming the messages from the earliest or latest offset.



