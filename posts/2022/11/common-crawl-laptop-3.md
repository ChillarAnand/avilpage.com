<!--
.. title: Common Crawl on Laptop - Building Web Directory
.. slug: common-crawl-laptop-3
.. date: 2022-12-04 07:41:39 UTC+05:30
.. tags: command-line, common-crawl, data-analysis, draft
.. category: programming
.. link: 
.. description: Building telugu web directory from common crawl dataset.
.. type: text
-->


Let's ignore these sites and fetch only the sites with more than 5 pages.

### Fetching the data

Now that we have the list of sites, let's fetch the data. We will use `wget` to download the data. 

```bash
# fetch data
wget -i urls.txt
```


### Extracting text

Now that we have the data, let's extract the text from the web pages. We will use `pup`[^pup] to extract the text from html.

```bash
# extract text
for f in *.warc.gz; do
    echo $f
    zcat $f | pup 'body text{}' | tr -d '\n' | tr -s ' ' | tr -d '\t' >> telugu.txt
done
```
