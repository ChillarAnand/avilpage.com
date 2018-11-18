<!--
.. title: Archive Million Pages With wget In Minutes
.. slug: archive-millions-pages-wget-minutes
.. date: 2018-11-18 17:21:21 UTC+05:30
.. tags: command-line, warc
.. category:
.. link:
.. description: How to archive millions of pages without using any tools in few minutes.
.. type: text
-->


### Introduction

[webrecorder](https://github.com/webrecorder/webrecorder), [heritrix](https://github.com/internetarchive/heritrix3), [nutch](https://nutch.apache.org/), [scrapy](https://scrapy.org/), [colly](https://github.com/gocolly/colly), [frontera](https://github.com/scrapinghub/frontera) are popular tools for large scale web crawling and archiving.

These tools require some learning curve and some of them don't have inbuilt support for warc([Web ARChive](https://en.wikipedia.org/wiki/Web_ARChive)) output format.

`wget` comes bundled with most *nix systems and has inbuilt support for warc output. In this article we will see how to quickly archive web pages with wget.


### Archiving with wget

In previous article we have extracted a [superset of top 1 million domains](/2018/11/comparision-alexa-majestic-domcorp-top-million-sites.html). We can use that list or urls to archive. Save this list to a file called `urls.txt`.

This can be archived with the following command.

```sh
file=urls.txt
wget -i $file --warc-file=$file -t 3 --timeout=4 -q -o /dev/null -O /dev/null
```
wget has the ability to continue partially downloaded files. But this option won't work with warc output. So, it is better to split this list into small chunks and process them. One added advantage of this approach is we can parallely download multiple chunks with wget.

```sh
mkdir -p chunks
split -l 1000 urls.txt chunks/ -d --additional-suffix=.txt -a 3
```

This will split the file into several chunks each containing 1000 urls. wget doesn't have multithreading support. We can write a for loop to schedule a seperate process for each chunk.

```
for file in `ls -r chunks/*.txt`
do
   wget -i $file --warc-file=$file -t 3 --timeout=4 -q -o /dev/null -O /dev/null &
done
```

To archive 1000 urls, it takes ~15 minutes. In less than 20 minutes, it will download entire million pages.

Also, each process takes ~8MB of memory. To run 1000 process, a system needs 8GB+ memory. Otherwise, number of parallel processes should be reduced which increases overall run time.

Each archive chunk will be ~150MB and consume lot of storage. All downloaded acrhives can be zipped to reduce storage.

```sh
gzip *.warc
```

Here is an idempotent shell script to download and archive files in batches.

```
#! /bin/sh

set -x

batch=1000
size=`expr ${#batch} - 1`
maxproc=50
file=urls.txt
dir=$HOME'/projects/chunks'$batch


mkdir -p $dir
split -l $batch $file $dir'/' -d --additional-suffix=.txt -a $size
sleep 1

useragent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'


for file in `ls -r $dir/*.txt`
do
    warcfile=$file'.warc'
    warczip=$warcfile'.gz'
    if [ -f $warczip ] || [ -f $warcfile ]; then
        continue
    fi

    if [ $(pgrep wget -c) -lt $maxproc ]; then
        echo $file
        wget -H "user-agent: $useragent" -i $file --warc-file=$file -t 3 --timeout=4 -q -o /dev/null -O /dev/null &
        sleep 2
    else
        sleep 300
        for filename in `find $dir -name '*.warc' -mmin +5`
        do
            gzip $filename -9
        done
    fi
done
```

### Conclusion

In this article, we have seen how to archive million pages with wget in few minutes.

wget2 has multithreading support and [it might have warc output soon](https://gitlab.com/gnuwget/wget2/issues/65). With that, archiving with wget becomes much easier.
