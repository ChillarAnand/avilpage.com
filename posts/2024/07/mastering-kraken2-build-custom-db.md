<!--
.. title: Mastering Kraken2 - Part 3 - Build Custom Database
.. slug: mastering-kraken2-build-custom-db
.. date: 2024-07-31 10:52:30 UTC+05:30
.. tags: kraken2, metagenomics, devops
.. category: 
.. link: 
.. description: How to create a custom database with kraken2
.. type: text
-->

### Mastering Kraken2 

[Part 1 - Initial Runs](/2024/07/mastering-kraken2-initial-runs.html)

[Part 2 - Performance Optimisation](/2024/07/mastering-kraken2-performance-optimisation.html)

[Part 3 - Building custom databases](/2024/07/mastering-kraken2-build-custom-db.html) (this post)

Part 4 - Regular vs Fast Builds (upcoming)

Part 5 - Benchmarking (upcoming)

### Introduction

In the previous post, we learned how to improve kraken2[^k2] performance. So far we have downloaded & used pre-built indices(databases). 

In this post, let's build a custom database for kraken2. For simplicity, let's use only refseq archaea genomes for building the index.

### Building Custom Database

First, we need to download the taxonomy files. We can use the `k2` script provided by kraken2.

```shell
$ k2 download-taxonomy --db custom_db
```

This takes ~30 minutes depending on the network speed. The taxonomy files are downloaded to the `custom_db/taxonomy` directory.

```shell
$ ls custom_db/taxonomy
citations.dmp  division.dmp  gencode.dmp  merged.dmp  nodes.dmp
nucl_wgs.accession2taxid delnodes.dmp  gc.prt 
images.dmp  names.dmp  nucl_gb.accession2taxid  readme.txt

$ du -hs custom_db/taxonomy
43G     custom_db/taxonomy
```

For simplicity, let's use the archaea refseq genomes. We can use `kraken2-build` to download the refseq genomes.

```shell
$ kraken2-build --download-library archaea --db custom_db
```

This runs on a single thread and takes longer. There are lot of issues with the downloader as well as seen on kraken2 github issues.

Let's install and use ncbi-genome-download[^ngd] to download the genomes. 

```shell
$ pip install ncbi-genome-download

$ conda install -c bioconda ncbi-genome-download

$ ncbi-genome-download -s refseq -F fasta --parallel 40 -P archaea
Checking assemblies: 100%|███| 2184/2184 [00:19<00:00, 111.60entries/s]
Downloading assemblies: 100%|███| 2184/2184  [02:04<00:00,  4.54s/files]
Downloading assemblies: 2184files [02:23, 2184files/s]
```

In just 2 minutes, it has downloaded all the files. Lets gunzip the files.

```shell
$ find . -name "*.gz" -print0 | parallel -0 gunzip

$ du -hs refseq
5.9G    refseq
```

Lets add all fasta genome files to the custom database

```shell
$ find . -name "*.fna" -exec kraken2-build --add-to-library {} --db custom_db \;
```
Let's build the database

```shell
$ time kraken2-build --build --threads 36 --db custom_db
Creating sequence ID to taxonomy ID map (step 1)...
Found 125783/125783 targets, searched through 983602079 accession IDs, search complete.
Sequence ID to taxonomy ID map complete. [4m14.765s]
Estimating required capacity (step 2)...
Estimated hash table requirement: 5340021028 bytes
Capacity estimation complete. [56.110s]
Building database files (step 3)...
Taxonomy parsed and converted.
CHT created with 11 bits reserved for taxid.
Completed processing of 125783 sequences, 6177202632 bp
Writing data to disk...  complete.
Database files completed. [20m43.414s]
Database construction complete. [Total: 25m55.868s]
kraken2-build --build --threads 36 --db custom_db  43571.40s user 109.56s system 2807% cpu 25:55.92 total
```

We are able to build index for ~6GB input files in ~30 minutes.

### Conclusion

We learnt some useful tips to speed up the custom database creation process. In the next post, we will learn about regular vs fast builds.



[^k2]: [Kraken2](https://ccb.jhu.edu/software/kraken2/)

[^ngd]: [https://github.com/kblin/ncbi-genome-download](https://github.com/kblin/ncbi-genome-download)
