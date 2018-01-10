<!--
.. title: How To Plot Renko Charts With Python?
.. slug: how-to-plot-renko-charts-with-python
.. date: 2018-01-10 14:57:23 UTC+05:30
.. tags: python, trading, programming
.. category: programming, python
.. link:
.. description: How to plot renko charts for stocks using OHLC data with python?
.. type: text
-->

Renko charts are time independent of time and are efficient to trade as they eliminate noise. In this article we plot renko charts of an instrument with OHLC data using Python.

First we need to calculate bricks from OHLC data. For brick size, we can choose a fix value or calculate it form ATR(Average True Range). Once brick size is selected, we can do diff on shifted close values to get the difference and divide it by brick size to get the bricks.

Once bricks are obtained, we need to assign the brick colors based on the direction of price movement and then plot rectangles for each available brick.


```python
brick_size = 2


def plot_renko(data, brick_size):
    fig = plt.figure(1)
    fig.clf()
    axes = fig.gca()
    y_max = max(data)

    prev_num = 0

    bricks = []

    for delta in data:
        if delta > 0:
            bricks.extend([1]*delta)
        else:
            bricks.extend([-1]*abs(delta))

    for index, number in enumerate(bricks):
        print((index, number), (1, brick_size), number)

        if number == 1:
            facecolor='green'
        else:
            facecolor='red'

        prev_num += number

        renko = Rectangle(
            (index, prev_num * brick_size), 1, brick_size,
            facecolor=facecolor, alpha=0.5
        )
        axes.add_patch(renko)

    plt.show()


df = pd.read_csv(file)

df['cdiff'] = df[close] - df[close].shift(1)
df.dropna(inplace=True)
df['bricks'] = df.loc[:, ('cdiff', )] / brick_size

bricks = df[df['bricks'] != 0]['bricks'].values
plot_renko(bricks, brick_size)
```


Here is a sample renko chart plotted using the above code.

<p align="center">
<img src="/images/python-renko3.png" />
</p>
