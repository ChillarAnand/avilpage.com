<!--
.. title: Guide to setting up GeoDjango on Mac M1
.. slug: guide-to-setting-up-geodjango-on-mac-m1
.. date: 2023-10-30 08:59:23 UTC+05:30
.. tags: macbook, django
.. category: programming
.. link: 
.. description: How setup GeoDjango using conda on Mac M1
.. type: text
-->

There are a lot of guides on setting up GeoDjango and PostGIS. But most of them are outdated and doesn't work on Mac M1. In this article, let us look at how to set up GeoDjango on Mac M1/M2.

Ensure you have already installed Postgres on your Mac. 

### Install GeoDjango

The default GDAL version available on brew fails to install on Mac M1.

```commandline
$ brew install gdal
==> cmake --build build
Last 15 lines from /Users/chillaranand/Library/Logs/Homebrew/gdal/02.cmake:
    [javac] Compiling 82 source files to /tmp/gdal-20231029-31808-1wl9085/gdal-3.7.2/build/swig/java/build/classes
    [javac] warning: [options] bootstrap class path not set in conjunction with -source 7
    [javac] error: Source option 7 is no longer supported. Use 8 or later.
    [javac] error: Target option 7 is no longer supported. Use 8 or later.

BUILD FAILED
/tmp/gdal-20231029-31808-1wl9085/gdal-3.7.2/swig/java/build.xml:25: Compile failed; see the compiler error output for details.

Total time: 0 seconds
gmake[2]: *** [swig/java/CMakeFiles/java_binding.dir/build.make:108: swig/java/gdal.jar] Error 1
gmake[2]: Leaving directory '/private/tmp/gdal-20231029-31808-1wl9085/gdal-3.7.2/build'
gmake[1]: *** [CMakeFiles/Makefile2:9108: swig/java/CMakeFiles/java_binding.dir/all] Error 2
gmake[1]: Leaving directory '/private/tmp/gdal-20231029-31808-1wl9085/gdal-3.7.2/build'
gmake: *** [Makefile:139: all] Error 2
```

We can use conda to install gdal. Create a new environment and install gdal in it.

```bash
$ conda create -n geodjango python=3.9
$ conda install -c conda-forge gdal
$ pip install django
$ pip install psycopg2-binary
```

Once installed, you can check the version using `gdalinfo --version`.

Remaining dependencies can be installed via brew.

```bash
$ brew install postgresql
$ brew install postgis
$ brew install libgeoip
```

Let's create a new django project and add spatial backends.

```bash
$ django-admin startproject geodjango
```

Add `django.contrib.gis` to `INSTALLED_APPS` in `settings.py`.

```python
INSTALLED_APPS = [
    ...,
    'django.contrib.gis',
]
```

Add the following to `DATABASES` in `settings.py`.

```python
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'
```

Since we used conda to install gdal, we need to set the path to gdal in our django settings. Run `locate libgdal.dylib` to find the path to gdal.

```python
GDAL_LIBRARY_PATH = '/opt/homebrew/anaconda3/envs/geodjango/lib/libgdal.dylib'
```

Similarly, we need to set `GEOS_LIBRARY_PATH` as well.

```python
GEOS_LIBRARY_PATH = '/opt/homebrew/anaconda3/envs/geodjango/lib/libgeos_c.dylib'
```

Now, we can create a new app and add PointField or any other spatial fields to our models.

```bash
$ python manage.py startapp places
```

```python
from django.contrib.gis.db import models

class Place(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
```

### Conclusion

In this article, we looked at how to set up GeoDjango on Mac M1. We used conda to install gdal and brew to install other dependencies. 
