<!--
.. title: Common Crawl on Laptop - Building Web Directory
.. slug: common-crawl-laptop-web-directory
.. date: 2022-12-08 07:41:39 UTC+05:30
.. tags: command-line, common-crawl, data-analysis
.. category: programming
.. link: 
.. description: Building telugu web directory from common crawl dataset.
.. type: text
-->

This series of posts discuss processing of common crawl dataset on laptop.

1. [Extracting Subset of Common Crawl](/2022/11/common-crawl-laptop-extract-subset.html)
2. [Building web directory](/2022/12/common-crawl-laptop-web-directory.html) (this post)


### Introduction

In the earlier post, we have extracted all telugu web page urls to a csv file. In this post, let's explore these urls and build a web directory from it.

### Explore Data

Let's see how many urls are present in the extracted subset of data.

```shell
$ wc -l telugu.csv
  852025 telugu.csv 
```

In the earlier post, we have installed `duckdb` and used it for processing parquet files. `duckdb` can execute SQL queries directly on csv file. Let's use it to explore the data stored in telugu.csv.

Let's see how many unique domains are present in the data.

```shell
$ duckdb -c """
    SELECT COUNT(DISTINCT url_host_name_reversed) as unique_sites
    FROM read_csv('telugu.csv', auto_detect = TRUE);
"""
┌──────────────┐
│ unique_sites │
├──────────────┤
│ 13632        │
└──────────────┘
```

There ~14k unique domains. Let's see page density across these domains.

```shell
$ duckdb -c """
SELECT count    AS page_count,
COUNT(*) AS sites
FROM (SELECT url_host_name_reversed, COUNT(*) AS count
FROM read_csv('te.csv', auto_detect = TRUE)
GROUP BY url_host_name_reversed) AS t
GROUP BY page_count
ORDER BY page_count;
"""
┌────────────┬───────┐
│ page_count │ sites │
├────────────┼───────┤
│ 1          │ 6326  │
│ 2          │ 1904  │
│ 3          │ 733   │
│ 4          │ 459   │
│ 5          │ 315   │
```

About ~75% of the sites have less than 5 pages. It is highly unlikely that these sites complete content is in Telugu language. After manually checking a few of these sites, I found that there are a lot of false positives. 

In the earlier post, we have extracted all pages where there is Telugu language content. Let's filter out pages where Telugu is **primary** language.

```shell
$ duckdb -c """
  COPY (
    SELECT * FROM read_csv('cct.csv', auto_detect=true) 
    WHERE content_languages like 'tel%'
  ) TO 'te_primary.csv' (DELIMITER ',', HEADER TRUE);
"""
```

```shell
$ wc -l te_primary.csv
  573130 te_primary.csv
```

```shell
$ duckdb -c "SELECT COUNT(DISTINCT url_host_name_reversed) as unique_sites FROM read_csv('te_primary.csv', auto_detect = TRUE)"                           
┌──────────────┐
│ unique_sites │
├──────────────┤
│ 5666         │
└──────────────┘    
```

Let's see how page density per domain has changed.

```shell
$ duckdb -c """
SELECT count    AS page_count,
COUNT(*) AS sites
FROM (SELECT url_host_name_reversed, COUNT(*) AS count
FROM read_csv('te_primary.csv', auto_detect = TRUE)
GROUP BY url_host_name_reversed) AS t
GROUP BY page_count
ORDER BY page_count
;
"""
┌────────────┬───────┐
│ page_count │ sites │
├────────────┼───────┤
│ 1          │ 2183  │
│ 2          │ 843   │
│ 3          │ 235   │
│ 4          │ 146   │
│ 5          │ 98    │
```

Page density remains almost the same. 

Let's filter out sites which have at least 5 pages in Telugu. This will eliminate a lot of false positives. Let's look at the most popular sites from the results.

```shell
   1   │ Rank,Domain,Open Page Rank
   2   │ 25,support.google.com,8.55
   3   │ 57,t.me,7.76
   4   │ 76,chrome.google.com,7.49
   5   │ 163,support.mozilla.org,6.99
   6   │ 170,groups.google.com,6.94
```

A lot of unrelated domains are present here because there might be 10+ pages in telugu in these domains as well. But we don't need these.

Let's look at only home page(or translated home page) where primary content language is telugu.

```shell
$ duckdb -c """
  SELECT COUNT(distinct url) 
  FROM read_csv('te_primary.csv', auto_detect=true) 
  WHERE (url_path = '/' or url_path = '/te/') and url_query is null;
"""
```

Now the domain count has reduced to 6k. Let's export these domains to csv file.

To categorize these domains, Common-crawl doesn't yet provide any kind of categorisation. For now, we can use Open PageRank to sort these domains based on rank. 

We can download top 10 million domains from Open PageRank[^pagerank]. Here is a simple python script to extract telugu domains from the list.

```python
import pandas as pd

domains_file = 'domains.csv'
with open(domains_file, 'r') as f:
    telugu_domains = [line.strip() for line in f.readlines()]

telugu_domains = ['.'.join(reversed(domain.split('.'))) for domain in telugu_domains]

df = pd.read_csv('t10m.csv')
df = df[df['Domain'].isin(telugu_domains)]

df.to_csv('t10m_telugu.csv', index=False)
```

Now, we have list of all telugu domains sorted by rank. In the next post, we will use this list to categorize the domains.


[^common-crawl]: [https://commoncrawl.org](https://commoncrawl.org)

[^columnar-index-wiki]: [https://en.wikipedia.org/wiki/Column-oriented_DBMS](https://en.wikipedia.org/wiki/Column-oriented_DBMS)

[^pagerank]: [https://www.domcop.com/openpagerank](https://www.domcop.com/openpagerank)

[^duckdb]: [https://duckdb.org](https://duckdb.org)

