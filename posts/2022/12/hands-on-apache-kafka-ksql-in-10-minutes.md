<!--
.. title: Hands-on Kafka KSQL in 10 Minutes
.. slug: hands-on-kafka-ksql-10-minutes
.. date: 2022-12-12 09:12:21 UTC+05:30
.. tags: kafka, 10-minute-guide, draft
.. category: programming
.. link: 
.. description: 
.. type: text
-->

A short hands-on guide to get started with Apache Kafka for people who are in a hurry.


### KSQL

KSQL[^ksql] is a streaming SQL engine for Apache Kafka. It provides a simple SQL-like language to write streaming applications on top of Kafka. It can be used to create streaming applications that transform, join, and aggregate data in real-time.

To start KSQL CLI:

```bash
$ docker-compose exec ksqldb-cli ksql http://ksqldb-server:8088
```

To create a stream from a topic:

```sql
ksql> CREATE STREAM test_stream (name VARCHAR) WITH (KAFKA_TOPIC='test', VALUE_FORMAT='JSON');

 Message        
----------------
 Stream created 
----------------
```

To list all the streams:

```sql
ksql> SHOW STREAMS;

 Stream Name         | Kafka Topic                 | Key Format | Value Format | Windowed 
------------------------------------------------------------------------------------------
 KSQL_PROCESSING_LOG | default_ksql_processing_log | KAFKA      | JSON         | false    
 TEST_STREAM         | test                        | KAFKA      | JSON         | false    
------------------------------------------------------------------------------------------
```

To create a table from a topic:

```sql
ksql> CREATE TABLE test_table (name VARCHAR) WITH (KAFKA_TOPIC='test', VALUE_FORMAT='JSON');
```

To list all the tables:

```sql
ksql> SHOW TABLES;
```

[^wikipedia apache kafka]: [https://en.wikipedia.org/wiki/Apache_Kafka](https://en.wikipedia.org/wiki/Apache_Kafka)

[^cp-all-in-one]: [https://github.com/confluentinc/cp-all-in-one](https://github.com/confluentinc/cp-all-in-one)

[^kafka rest proxy]: [https://github.com/confluentinc/kafka-rest](https://github.com/confluentinc/kafka-rest)

[^ksql]: [https://github.com/confluentinc/ksql](https://github.com/confluentinc/ksql)
