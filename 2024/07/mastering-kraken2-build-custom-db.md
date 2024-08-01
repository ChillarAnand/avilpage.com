<!--
.. title: Mastering Kraken2 - Part 3 - Build Custom Database
.. slug: mastering-kraken2-build-custom-db
.. date: 2024-08-01 10:52:30 UTC+05:30
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

In the previous post, we learned how to improve kraken2[^k2] classification performance. So far we have downloaded & used pre-built genome indices(databases). 

In this post, let's build a custom database for kraken2. For simplicity, let's use only refseq archaea genomes[^rag] for building the index.

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
$ k2 download-library --library archaea --db custom_db
```

This runs on a single thread. Instead of using `kraken2-build`, we can use `ncbi-genome-download`[^ngd] tool to download the genomes. This provides much granular control over the download process. For example, we can download only `--assembly-levels complete` genomes. We can also download multiple genomes in parallel.

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
$ find refseq -name "*.gz" -print0 | parallel -0 gunzip

$ du -hs refseq
5.9G    refseq
```

Lets add all fasta genome files to the custom database

```shell
$ time find refseq -name "*.fna" -exec kraken2-build --add-to-library {} --db custom_db \;
667.46s user 90.78s system 106% cpu 12:54.80 total
```

`kraken2-build` doesn't use multiple threads for adding genomes to the database. In addition to that, it also doesn't check if the genome is already present in the database. 

Let's use `k2` for adding genomes to the database.

```shell
export KRAKEN_NUM_THREADS=40

$ find . -name "*.fna" -exec k2 add-to-library --files {} --db custom_db \;
668.37s user 88.44s system 159% cpu 7:54.40 total
```

This took only half the time compared to `kraken2-build`.

Let's build the index from the library.

```shell
$ time kraken2-build --db custom_db --build --threads 36
Creating sequence ID to taxonomy ID map (step 1)...
Found 0/125783 targets, searched through 60000000 accession IDs...
Found 59923/125783 targets, searched through 822105735 accession IDs, search complete.
lookup_accession_numbers: 65860/125783 accession numbers remain unmapped, see unmapped.txt in DB directory
Sequence ID to taxonomy ID map complete. [2m1.950s]
Estimating required capacity (step 2)...
Estimated hash table requirement: 5340021028 bytes
Capacity estimation complete. [23.875s]
Building database files (step 3)...
Taxonomy parsed and converted.
CHT created with 11 bits reserved for taxid.
Completed processing of 59911 sequences, 3572145823 bp
Writing data to disk...  complete.
Database files completed. [12m3.368s]
Database construction complete. [Total: 14m29.666s]
kraken2-build --db custom_db --build --threads 36  24534.98s user 90.50s system 2831% cpu 14:29.75 total

$ ls -ll
.rw-rw-r-- 5.3G anand  1 Aug 16:35 hash.k2d
drwxrwxr-x    - anand  1 Aug 12:32 library
.rw-rw-r--   64 anand  1 Aug 16:35 opts.k2d
.rw-rw-r-- 1.5M anand  1 Aug 16:22 seqid2taxid.map
.rw-rw-r-- 115k anand  1 Aug 16:23 taxo.k2d
lrwxrwxrwx   20 anand  1 Aug 12:31 taxonomy
.rw-rw-r-- 1.2M anand  1 Aug 16:22 unmapped.txt
```

We are able to build index for ~6GB input files in ~15 minutes.

### Conclusion

We learnt some useful tips to speed up the custom database creation process. In the next post, we will learn about regular vs. fast builds.


[^k2]: [Kraken2](https://ccb.jhu.edu/software/kraken2/)

[^rag]: [RefSeq Archaea genomes](https://ftp.ncbi.nlm.nih.gov/genomes/refseq/archaea/)

[^ngd]: [https://github.com/kblin/ncbi-genome-download](https://github.com/kblin/ncbi-genome-download)
