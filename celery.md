# Mastering Python Celery

## Introduction

Python Celery is an open source asynchronus task queue or job queue which is based on distributed message passing. It is used to run background tasks or jobs and currently supports RabbitMQ, Redis, Amazon SQS, Beanstalk, and database transports.

## Prerequisites

- Python 3.6 or above
- RabbitMQ
- Redis
- Celery

## Installation

### RabbitMQ

RabbitMQ is an open source message broker software that implements the Advanced Message Queuing Protocol (AMQP). It is used to send and receive messages between applications.

#### Installation

```bash
sudo apt-get install rabbitmq-server
```

#### Start RabbitMQ

```bash
sudo service rabbitmq-server start
```

#### Stop RabbitMQ

```bash
sudo service rabbitmq-server stop
```

#### Enable RabbitMQ Management

```bash
sudo rabbitmq-plugins enable rabbitmq_management
```

#### Access RabbitMQ Management

```bash
http://localhost:15672
```

### Redis

Redis is an open source in-memory data structure store, used as a database, cache and message broker. It supports data structures such as strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperloglogs and geospatial indexes with radius queries.

#### Installation

```bash
sudo apt-get install redis-server
```

#### Start Redis

```bash
sudo service redis-server start
```

#### Stop Redis

```bash
sudo service redis-server stop
```

### Celery

Celery is an open source asynchronous task queue or job queue based on distributed message passing. It is used to run background tasks or jobs and currently supports RabbitMQ, Redis, Amazon SQS, Beanstalk, and database transports.

#### Installation

```bash
pip install celery
```

## Getting Started

### Create a Celery Project

```bash
mkdir celery-project
cd celery-project
```

### Create a Celery App

```bash
touch app.py
```

```python

from celery import Celery

app = Celery('tasks', broker='amqp://localhost')

@app.task
def add(x, y):
    return x + y

```

### Create a Celery Worker

```bash
touch worker.py
```

```python
from app import app

app.worker_main(['worker', '-l', 'info'])

```

### Create a Celery Client

```bash
touch client.py
```

```python
from app import add

result = add.delay(4, 4)
print(result.get())

```

### Run the Celery Worker

```bash
python worker.py
```

### Run the Celery Client

```bash
python client.py
```

## Conclusion

In this tutorial, we have learned how to install and use Python Celery. We have also learned how to create a Celery project, Celery app, Celery worker, and Celery client. We have also learned how to run the Celery worker and Celery client.

## References

