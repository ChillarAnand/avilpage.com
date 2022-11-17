<!--
.. title: Common Crawl On Laptop - Extracting Subset Of Data
.. slug: common-crawl-laptop-extract-subset
.. date: 2022-11-17 06:41:39 UTC+05:30
.. tags: common-crawl, command-line, data-analysis
.. category: programming
.. link:
.. description: How to process entire common crawl data set from your local machine.
.. type: text
-->

This series of posts discuss processing of common crawl dataset on laptop.

### Introduction

Common Crawl(CC)[^common-crawl] is an open repository of web containing peta bytes of data since 2008. As the dataset is huge, most of the tutorials use AWS EMR/Athena to process the data.

In this post, let's learn how to extract a subset of data(entire telugu language web pages) and process it on our local machine.

### Exploring Common Crawl

CC provides monthly data dumps in WARC format. Each crawl consists of about ~3 billion web pages with a compressed size of ~100 TB.

In addition to WARC files, CC provides index files as well as columnar index[^columnar-index-wiki] files so that users can easily search, filter and download the data.


### Common Crawl Index

Each crawl index is spread over 300 files consisting of ~250 GB of data. For this post, let use the latest crawl which is `CC-MAIN-2022-40`.

The index files can be accessed from AWS S3 or https. We can use aws cli to list all the files along with the sizes.

```bash
$ aws s3 ls --recursive --human-readable --summarize s3://commoncrawl/cc-index/collections/CC-MAIN-2022-40
2022-10-08 16:07:59  621.9 MiB cc-index/collections/CC-MAIN-2022-40/indexes/cdx-00000.gz
2022-10-08 16:08:26  721.6 MiB cc-index/collections/CC-MAIN-2022-40/indexes/cdx-00001.gz
...
2022-10-08 16:42:39  146.6 MiB cc-index/collections/CC-MAIN-2022-40/indexes/cluster.idx
2022-10-08 16:42:33   30 Bytes cc-index/collections/CC-MAIN-2022-40/metadata.yaml

Total Objects: 302
   Total Size: 236.1 GiB
```

Let's download an index file to our local machine and see how the data is arranged. We can use `aws` cli to download the data from s3 bucket or use wget to download it from https endpoint.

```bash
# from s3
$ aws s3 cp s3://commoncrawl/cc-index/collections/CC-MAIN-2022-40/indexes/cdx-00000.gz .

# from https
$ wget https://data.commoncrawl.org/cc-index/collections/CC-MAIN-2022-40/indexes/cdx-00000.gz
```

Let's print top five lines of the file.

```bash
$ zcat < cdx-00000.gz | head -n 5
0,1,184,137)/1klikbet 20221005193707 {"url": "http://137.184.1.0/1klikbet/", "mime": "text/html", "mime-detected": "text/html", "status": "200", "digest": "XTKGORHKLZCHDBBOMYCYYIZVRPMXNRII", "length": "7065", "offset": "83437", "filename": "crawl-data/CC-MAIN-2022-40/segments/1664030337663.75/warc/CC-MAIN-20221005172112-20221005202112-00011.warc.gz", "charset": "UTF-8", "languages": "ind"}
0,1,184,137)/7meter 20221005192131 {"url": "http://137.184.1.0/7meter/", "mime": "text/html", "mime-detected": "text/html", "status": "200", "digest": "KUJAMRT6MXYR3RTWRJTIWJ5T2ZUB3EBH", "length": "7456", "offset": "142680", "filename": "crawl-data/CC-MAIN-2022-40/segments/1664030337663.75/warc/CC-MAIN-20221005172112-20221005202112-00182.warc.gz", "charset": "UTF-8", "languages": "ind"}
...
```

The last column of each line contains the language information. We can use these index files, and we can  extract all the lines containing `tel` language code.

### Columnar Index

We can also use columnar index to filter out telugu language web pages. Let's download a single file from the index.

```bash
# from s3
$ aws s3 cp s3://commoncrawl/cc-index/table/cc-main/warc/crawl=CC-MAIN-2022-40/subset=warc/part-00001-26160df0-1827-4787-a515-95ecaa2c9688.c000.gz.parquet .

# from https
$ wget https://data.commoncrawl.org/cc-index/table/cc-main/warc/crawl=CC-MAIN-2022-40/subset=warc/part-00001-26160df0-1827-4787-a515-95ecaa2c9688.c000.gz.parquet
```

We can use Python pandas to read the parquet file and filter out telugu language web pages. Columnar index has `content_languages` column which can be use to filter out telugu pages.

```bash
$ python -c """
import pandas as pd
filename = 'part-00000-26160df0-1827-4787-a515-95ecaa2c9688.c000.gz.parquet'
df = pd.read_parquet(filename)
df = df[df['content_languages'].str.startswith('tel', na=False)]
df.to_csv('telugu.csv')
"""
```

### Improving Performance

#### Faster Downloads

I have used Macbook M1 with local ISP to download and extract the index. It took around 7 minutes to download a single file and 2 minutes to extract the data. To process 300 index files, it takes ~2 days.

Let's see how we can speed it up.

My Wi-Fi speed is ~4MBps when downloading the index file. To download faster, I have created t2.micro(free-tier) EC2 instance on AWS. In this machine, download speed is ~10MBps. We can use other instances, but I am trying to use only free resources. In this machine, single file download is taking ~3 minutes.

CC dataset is hosted in us-east-1 region. So, I have created a new t2.micro instance in us-east-1 region. This instance is taking <20 seconds to download a single file. We can download entire index in less than 2 hours.

#### Faster Performance

To extract data from index files, we have used Python pandas without specifying the engine. By default, it uses `pyarrow` which is a bit slow. To improve speed we can use `fastparquet` as engine which is ~5x faster than `pyarrow`.

```python
import pandas as pd

filename = 'part-00000-26160df0-1827-4787-a515-95ecaa2c9688.c000.gz.parquet'
df = pd.read_parquet(filename, engine='fastparquet')
```

To get better performance, we can use duckdb. Duckdb can execute SQL queries directly on parquet files with `parquet` extension. 

```bash
$ brew install duckdb

$ duckdb -c 'INSTALL parquet;'
```

We can write a simple SQL query to filter out the required rows.

```bash
$ duckdb -c """
LOAD parquet;
COPY (select * from PARQUET_SCAN('part-00000-26160df0-1827-4787-a515-95ecaa2c9688.c000.gz.parquet') where content_languages ilike '%tel%') TO 'te0001.csv' (DELIMITER ',', HEADER TRUE);
"""
```

Duckdb can execute SQL queries on remote files as well with `httpfs` extension.

```bash
$ duckdb -c 'INSTALL httpfs;'

$ duckdb -c """
    LOAD httpfs;
    LOAD parquet;

    COPY (select * from PARQUET_SCAN('s3://commoncrawl/cc-index/table/cc-main/warc/crawl=CC-MAIN-2022-40/subset=warc/part-00001-26160df0-1827-4787-a515-95ecaa2c9688.c000.gz.parquet') where content_languages ilike '%tel%') TO 'te0001.csv' (DELIMITER ',', HEADER TRUE);"""
"""
```

Duckdb can also read series of parquet files and treat them as a single table. We can use this feature to process all the index files in a single command.

```bash
$ duckdb -c """
    LOAD httpfs;
    LOAD parquet;

    SET s3_region='us-east-1';
    SET s3_access_key_id='s3_secret_access_key';
    SET s3_secret_access_key='s3_secret_access_key';

    COPY (select * from PARQUET_SCAN('s3://commoncrawl/cc-index/table/cc-main/warc/crawl=CC-MAIN-2022-40/subset=warc/*.parquet') where content_languages ilike '%tel%') TO 'te$i.csv' (DELIMITER ',', HEADER TRUE);
"""
```

Depending on the file size, duckdb takes 10-15 seconds to process a single file. With this single command, entire index can be processed in an hour. We can also parallelize the process for faster results.

### Conclusion

With this single command, we can extract any subset of index from CC in < 3 hours. In the upcoming posts, let's see how we can fetch the data from WARC files using this index and do further data processing.


[^common-crawl]: [https://commoncrawl.org](https://commoncrawl.org)
[^columnar-index-wiki]: [https://en.wikipedia.org/wiki/Column-oriented_DBMS](https://en.wikipedia.org/wiki/Column-oriented_DBMS)
