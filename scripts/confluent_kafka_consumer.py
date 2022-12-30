import logging
from contextlib import contextmanager, redirect_stderr, redirect_stdout
from os import devnull

from confluent_kafka import Consumer, KafkaError

logger = logging.getLogger(__file__)
logger.setLevel(logging.ERROR)

def error_handler(error):
    if error.code() == KafkaError.REQUEST_TIMED_OUT:
        # print('=====> Ignoring timeout error')
        return
    if error.code() == KafkaError.BROKER_NOT_AVAILABLE:
        # print('=====> BROKER_NOT_AVAILABLE error')
        return
    if error.code() == KafkaError._TRANSPORT:
        # print('=====> BROKER_NOT_AVAILABLE error')
        return

    print('======>', error, 'Consumer')


consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': '0',
    'auto.offset.reset': 'earliest',
    'logger': logger,
    # 'log.queue': True,
    'max.poll.interval.ms': 10000,
    'session.timeout.ms': 6000,
    'log.connection.close': True,
    'error_cb': error_handler,
})

topic = 'test'
consumer.subscribe([topic])
print(f'"{topic}" topic subscribed')

@contextmanager
def suppress_stdout_stderr():
    """A context manager that redirects stdout and stderr to devnull"""
    with open(devnull, 'w') as fnull:
        with redirect_stderr(fnull) as err, redirect_stdout(fnull) as out:
            yield err, out


while True:
    msg = None
    # with suppress_stdout_stderr():
    #     msg = consumer.poll(1.0)
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    print('Received message: {}'.format(msg.value().decode('utf-8')))


consumer.close()
