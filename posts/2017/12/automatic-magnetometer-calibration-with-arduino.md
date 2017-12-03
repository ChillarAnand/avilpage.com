<!--
.. title: Automatic Magnetometer Calibration With Arduino
.. slug: automatic-magnetometer-calibration-with-arduino
.. date: 2017-12-02 21:21:21 UTC
.. tags: arduino, how-to
.. category: tech, arduino
.. link:
.. description:
.. type: text
-->

If we take readings from a 3-axis [magnetometers](https://en.wikipedia.org/wiki/Magnetometer) like HMC5883L, AK8963C (used in MPU9250) or LSM303DLHC and plot them, its response should be a sphere with ceter at origin.

In practice, due to the presence of hard and soft iron distortions, the response will be an ellipsiod with its center shifted away from origin. We need to calibrate the magnetometer to nullify the distortions.

First we need to get sample readings of magnetometer in various positions. Depending on the magnetometer, we need to connect it to arduino and take readings by rotating it in 8 shape.


### Calibration

Hard iron biases shifts center away from origin. We can eliminate this error by calculating the offsets and shifting the readings.

```c
int mx, my, mz;

int mx_min, my_min, mz_min;
int mx_max, my_max, mz_max;
int mx_offset, my_offset, mz_offset;

int mx_calibrated, my_calibrated, mz_calibrated;

// get min/max values by taking readings
// from magnetometer of your choice

mx_offset = (mx_min + mx_max)/2;
my_offset = (my_min + my_max)/2;
mz_offset = (mz_min + mz_max)/2;

mx_calibrated = mx - mx_offset;
my_calibrated = my - my_offset;
mz_calibrated = mz - mz_offset;
```

Soft iron biases makes the axial responses uneven which results in ellipsiod shape. An easier way to correct this is to rescale the axial readings to an average value.

```cpp
int mx_scale, my_scale, mz_scale;

mx_scale = (mx_max - mx_min)/2;
my_scale = (my_max - my_min)/2;
mz_scale = (mz_max - mz_min)/2;

float avg_scale = (mx_scale + my_scale + mz_scale)/3;

mx_calibrated = avg_scale/(mx - mx_offset);
my_calibrated = avg_scale/(my - my_offset);
mz_calibrated = avg_scale/(mz - mz_offset);
```

We can caclulate these biases once and store them in our code so that we don't need to calibrate it everytime. We can also write an auto update function which will recalibrate offsets & scale for every new reading.
