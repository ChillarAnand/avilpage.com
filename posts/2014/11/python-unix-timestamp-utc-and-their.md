.. title: Unix Timestamp, UTC And Their Conversions In Python
.. slug: python-unix-timestamp-utc-and-their
.. date: 2014-11-22 18:26:00
.. tags: python, linux
.. category: tech, programming, python
.. description: Conversion of various timestamps in Python programming language.


### Coordinated Universal Time(UTC):

It is the primary time standard by which the world regulates clocks and time. To get current UTC time in Python, we can use `datetime` module.

```py
In [5]: import datetime

In [6]: datetime.datetime.now(datetime.timezone.utc)
Out[6]: datetime.datetime(2014, 11, 22, 14, 42, 21, 34435, tzinfo=datetime.timezone.utc)
```


### Unix time / POSIX time / Epoch time:

It is a system for describing instants in time, defined as the number of seconds that have elapsed since 00:00:00 Coordinated Universal Time (UTC), Thursday, 1 January 1970, not counting leap seconds. To get Unix timestamp, we can use `time` module.

```py
In [8]: import time

In [9]: time.time()
Out[9]: 1416667432.5664258

In [10]: int(time.time())
Out[10]: 1416667766
```

With Pyhon 3.4, we can directly get timestamp from UTC.

```
In [13]: datetime.datetime.utcnow().timestamp()
Out[13]: 1416649608.58369
```


### Conversions:

To convert Unix timestamp to UTC we can use `utcfromtimestamp` function.

```py
In [21]: datetime.datetime.utcfromtimestamp(1416668401)
Out[21]: datetime.datetime(2014, 11, 22, 15, 0, 1)
```

To convert UTC time object to Unix time, we can use `strftime` function.

```py
In [38]: dt = datetime.datetime.now()

In [39]: dt.strftime("%s")
Out[39]: '1416668938'
```

Alternatively, we can use `calendar.timegen` function.

```py
In [46]: import calendar

In [47]: dt = datetime.datetime.utcnow()

In [48]: calendar.timegm(dt.utctimetuple())
Out[48]: 1416669150
```
