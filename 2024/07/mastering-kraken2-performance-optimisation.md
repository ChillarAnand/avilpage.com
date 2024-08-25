<!--
.. title: Mastering Kraken2 - Part 2 - Performance Optimisation
.. slug: mastering-kraken2-performance-optimisation
.. date: 2024-07-28 10:51:30 UTC+05:30
.. tags: bioinformatics, metagenomics, kraken2, devops
.. category: 
.. link: 
.. description: How to speed up kraken2 classification process
.. type: text
-->

### Mastering Kraken2 

[Part 1 - Initial Runs](/2024/07/mastering-kraken2-initial-runs.html)

[Part 2 - Classification Performance Optimisation](/2024/07/mastering-kraken2-performance-optimisation.html) (this post)

[Part 3 - Building custom databases](/2024/07/mastering-kraken2-build-custom-db.html)

Part 4 - Regular vs Fast Builds (upcoming)

Part 5 - Benchmarking (upcoming)

### Introduction

In the previous post, we learned how to set up kraken2[^k2], download pre-built indices, and run kraken2. In this post, we will learn various ways to speed up the classification process.


### Increasing RAM

Kraken2 standard database is ~80GB in size. It is recommended to have at least db size RAM to run kraken2 efficiently[^ksr]. Let's use 128GB RAM machine and run kraken2 with ERR10359977[^err] sample.

```shell
$ time kraken2 --db k2_standard --report report.txt ERR10359977.fastq.gz > output.txt
Loading database information... done.
95064 sequences (14.35 Mbp) processed in 2.142s (2662.9 Kseq/m, 402.02 Mbp/m).
  94816 sequences classified (99.74%)
  248 sequences unclassified (0.26%)
kraken2 --db k2_standard --report report.txt ERR10359977.fastq.gz >   1.68s user 152.19s system 35% cpu 7:17.55 total
```

Now the time taken has come down from 40 minutes to 7 minutes. The classification speed has also increased from 0.19 Mbp/m to 402.02 Mbp/m.

The previous sample had only a few reads, and the speed is not a good indicator. Let's run kraken2 with a larger sample.

```shell
$ time kraken2 --db k2_standard --report report.txt --paired SRR6915097_1.fastq.gz SRR6915097_2.fastq.gz > output.txt
Loading database information... done.
Processed 14980000 sequences (2972330207 bp) ...
17121245 sequences (3397.15 Mbp) processed in 797.424s (1288.2 Kseq/m, 255.61 Mbp/m).
  9826671 sequences classified (57.39%)
  7294574 sequences unclassified (42.61%)
kraken2 --db k2_standard --report report.txt --paired > output.txt  526.39s user 308.24s system 68% cpu 20:23.86 total
```

This took almost 20 minutes to classify ~3 Gbp of data. Out of 20 minutes, 13 minutes was spent in classification. The remaining time in loading the db into memory.

Let's use k2_plusPF[^k2p] db, which is twice the size of k2_standard and run kraken2.

```shell
$ time kraken2 --db k2_plusfp --report report.txt --paired SRR6915097_1.fastq.gz SRR6915097_2.fastq.gz > output.txt
Loading database information...done.
17121245 sequences (3397.15 Mbp) processed in 755.290s (1360.1 Kseq/m, 269.87 Mbp/m).
  9903824 sequences classified (57.85%)
  7217421 sequences unclassified (42.15%)
kraken2 --db k2_plusfp/ --report report.txt --paired SRR6915097_1.fastq.gz  >   509.71s user 509.51s system 55% cpu 30:35.49 total
```

This took ~30 minutes to complete, but the classification took only 13 minutes similar to k2_standard. The remaining time was spent in loading the db into memory.

### Preloading db into RAM

We can use vmtouch[^vmt] to preload db into RAM. kraken2 provides `--memory-mapping` option to use preloaded db. 

```shell
$ vmtouch -vt k2_standard/hash.k2d k2_standard/opts.k2d k2_standard/taxo.k2d
           Files: 3
     Directories: 0
   Touched Pages: 20382075 (77G)
         Elapsed: 434.77 seconds
```

When Linux requires RAM, it will incrementally evict the db from memory. To prevent this, we can copy the db to shared memory (/dev/shm) and then use vmtouch to preload the db.

```shell
$ cp -r k2_standard /dev/shm

$ vmtouch -t /dev/shm/*.k2d
```

Now, let's run kraken2 with `--memory-mapping` option.

```shell
$ time kraken2 --db k2_standard --report report.txt --memory-mapping --paired SRR6915097_1.fastq.gz SRR6915097_2.fastq.gz > output.txt
Loading database information... done.
17121245 sequences (3397.15 Mbp) processed in 532.486s (1929.2 Kseq/m, 382.79 Mbp/m).
  9826671 sequences classified (57.39%)
  7294574 sequences unclassified (42.61%)
  kraken2 --db k2_standard --report report.txt --paired SRR6915097_1.fastq.gz   >  424.20s user 11.76s system 81% cpu 8:54.98 total
```

Now the classification took only ~10 minutes.

### Multi threading

kraken2 supports multiple threads. I am using a machine with 40 threads.

```shell
$ time kraken2 --db k2_standard --report report.txt --paired SRR6915097_1.fastq.gz SRR6915097_2.fastq.gz --memory-mapping --threads 32 > output.txt
Loading database information... done.
17121245 sequences (3397.15 Mbp) processed in 71.675s (14332.5 Kseq/m, 2843.81 Mbp/m).
  9826671 sequences classified (57.39%)
  7294574 sequences unclassified (42.61%)
kraken2 --db k2_standard --report report.txt --paired SRR6915097_1.fastq.gz      556.58s user 22.85s system 762% cpu 1:16.02 total
```

With 32 threads, the classification took only 1 minute. Beyond 32 threads, the classification time did not decrease significantly.


### Optimising input files

So far we have used gzipped input files. Let's use unzipped input files and run kraken2.

```shell
$ gunzip SRR6915097_1.fastq.gz
$ gunzip SRR6915097_2.fastq.gz

$ time kraken2 --db k2_standard --report report.txt --paired SRR6915097_1.fastq SRR6915097_2.fastq --memory-mapping --threads 30 > output.txt
Loading database information... done.
17121245 sequences (3397.15 Mbp) processed in 34.809s (29512.0 Kseq/m, 5855.68 Mbp/m).
  9826671 sequences classified (57.39%)
  7294574 sequences unclassified (42.61%)
kraken2 --db k2_standard --report report.txt --paired SRR6915097_1.fastq    30   565.03s user 17.12s system 1530% cpu 38.047 total
```

Now the classification time has come down to 40 seconds.

Since the input fastq files are paired, interleaving the files also takes time. Lets interleave the files and run kraken2.

To interleave the files, lets use `seqfu` tool.

```shell
$ conda install -y -c conda-forge -c bioconda "seqfu>1.10"

$ seqfu interleave -1 SRR6915097_1.fastq.gz -2 SRR6915097_2.fastq.gz > SRR6915097.fastq

$ time kraken2 --db k2_standard --report report.txt --memory-mapping SRR6915097.fq --threads 32 > output.txt
Loading database information... done.
34242490 sequences (3397.15 Mbp) processed in 20.199s (101714.1 Kseq/m, 10090.91 Mbp/m).
  17983321 sequences classified (52.52%)
  16259169 sequences unclassified (47.48%)
kraken2 --db k2_standard --report report.txt --memory-mapping SRR6915097.fq  32  618.96s user 18.24s system 2653% cpu 24.013 total
```

Now the classification time has come down to 24 seconds. 

### Conclusion

In terms of classification speed, we have come a long way from 0.1 Mbp/m to 1200 Mbp/m. In the next post, we will learn how to optimise the creation of custom indices.


[^k2]: [Kraken2](https://ccb.jhu.edu/software/kraken2/)

[^ksr]: [Kraken System Requirements](https://github.com/DerrickWood/kraken2/blob/master/docs/MANUAL.markdown#system-requirements)

[^err]: [ERR10359977.fastq.gz](ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR103/077/ERR10359977/ERR10359977.fastq.gz)

[^k2p]: [Genomic Index Zone - k2](https://benlangmead.github.io/aws-indexes/k2)

[^vmt]: [https://hoytech.com/vmtouch/](https://hoytech.com/vmtouch/)
