<!--
.. title: Load Testing Celery With Different Brokers
.. slug: load-testing-celery-brokers
.. date: 2018-02-09 19:19:18 UTC+06:30
.. tags: python, celery
.. category:
.. link:
.. description: how to load test celery queuing mechanism?
.. type: text
-->

Celery is mainly used to offload work from request/response cycle in web applications and to build pipelines in data processing applications. Lets run a load test on celery to see how well it queues the tasks with various brokers.

Let us take a simple add task and measure queueing time.

```
import timeit

from celery import Celery

broker = 'memory://'


app = Celery(broker=broker)


@app.task
def add(x, y):
    return x + y


tasks = 1000
start_time = timeit.default_timer()
results = [add.delay(1, 2) for i in range(tasks)]
duration = timeit.default_timer() - start_time
rate = tasks//duration
print("{} tasks/sec".format(str(rate))
```

On development machine, with AMD A4-5000 CPU, queueing time is as follows

- memory ---> 400 tasks/sec
- rabbitmq ---> 300 tasks/sec
- redis ---> 250 tasks/sec
- postgres ---> 30 tasks/sec

On production machine, with Intel(R) Xeon(R) CPU E5-2676, queueing time is as follows

- memory ---> 2000 tasks/sec
- rabbitmq ---> 1400 tasks/sec
- redis ---> 1200 tasks/sec
- postgres ---> 200 tasks/sec

For low/medium traffic webistes and applications, 1000 tasks/second should be fine. For high traffic webistes, there will be multiple servers queueing up the tasks.

Incase if we need to queue the tasks at a higher rate and if we have task arguments before hand, we can chunk the tasks.

```python
tasks = add.chunks(zip(range(1000), range(1000)), 10)
```

This will divide 1000 tasks into 10 groups of 100 tasks each. As there is no messaging overhead, it can queue any number of tasks in less than a second.
