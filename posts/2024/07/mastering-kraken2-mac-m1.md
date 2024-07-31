<!--
.. title: Mastering Kraken2 - Part 3 - Running on Mac M1 (ARM)
.. slug: mastering-kraken2-run-mac-m1
.. date: 2024-07-31 10:51:30 UTC+05:30
.. tags: kraken2, metagenomics, devops, draft
.. category: 
.. link: 
.. description: How to run kraken2 on Mac M1 or Ubuntu ARM
.. type: text
-->

### Mastering Kraken2 

[Part 1 - Initial Runs](/2024/07/mastering-kraken2-initial-runs.html)

[Part 2 - Performance Optimisation](/2024/07/mastering-kraken2-performance-optimisation.html)

Part 3 - Running on Mac M1 (this post)

Part 4 - Building standard database (upcoming)

Part 5 - Building custom database (upcoming)


### Introduction

Kraken2[^k2] official docs doesn't mention anything about ARM support. In this article lets look at how we can run kraken2 on Mac M1 with or without docker.


### Brew

Kraken2 can be installed using brew on Mac M1 via homebrew-bio.

```shell
$ brew install brewsci/bio/kraken2

$ kraken2 -v
Kraken version 2.1.3
```

Once installed, we can run kraken2 as usual.

```shell
$ kraken2 --db k2_standard --report report.txt ERR10359977.fastq.gz > output.txt
```

### Docker

Kraken2 doesn't have an official docker image. We can use the image created by [avilpage](https://hub.docker.com/r/avilpage/kraken2).

```shell
$ docker run -v $(pwd):/app --rm avilpage/kraken2 kraken2 --db /app/k2_viral --report r.txt /app/ERR10359977.fastq > a.txt
```

❯ docker run -v $(pwd):/app --rm avilpage/kraken2 kraken2 --db /app/k2_viral --report r.txt /app/ERR10359977.fastq > a.txt
Loading database information... done.
95064 sequences (14.35 Mbp) processed in 2.006s (2843.9 Kseq/m, 429.35 Mbp/m).
  235 sequences classified (0.25%)
  94829 sequences unclassified (99.75%)

  ~/projects/kraken2 on   master !2 ?8 ─────────────────────────────────────────────────────── took  6s  base at ⎈ k3d-demo-cluster ﴃ DEV at  13:02:21
❯ docker run -v $(pwd):/app --rm avilpage/kraken2 kraken2 --db /app/k2_viral --report r.txt /app/ERR10359977.fastq --threads 7 > a.txt
Loading database information... done.
95064 sequences (14.35 Mbp) processed in 0.789s (7231.9 Kseq/m, 1091.82 Mbp/m).
  235 sequences classified (0.25%)
  94829 sequences unclassified (99.75%)

  ~/projects/kraken2 on   master !2 ?8 ─────────────────────────────────────────────────────── took  6s  base at ⎈ k3d-demo-cluster ﴃ DEV at  13:02:55
❯ docker run -v $(pwd):/app --rm avilpage/kraken2 kraken2 --db /app/k2_viral --report r.txt /app/SRR6915097_1.fastq --threads 7 > a.txt
Loading database information... done.
17121245 sequences (1700.06 Mbp) processed in 123.447s (8321.6 Kseq/m, 826.29 Mbp/m).
  27018 sequences classified (0.16%)
  17094227 sequences unclassified (99.84%)


### Conclusion




[^k2]: [Kraken2](https://ccb.jhu.edu/software/kraken2/)

[^ksr]: [Kraken System Requirements](https://github.com/DerrickWood/kraken2/blob/master/docs/MANUAL.markdown#system-requirements)

[^err]: [ERR10359977.fastq.gz](ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR103/077/ERR10359977/ERR10359977.fastq.gz)

[^k2p]: [Genomic Index Zone - k2](https://benlangmead.github.io/aws-indexes/k2)

[^vmt]: [https://hoytech.com/vmtouch/](https://hoytech.com/vmtouch/)
