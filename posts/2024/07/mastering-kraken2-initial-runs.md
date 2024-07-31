<!--
.. title: Mastering Kraken2 - Part 1 - Initial Runs
.. slug: mastering-kraken2-initial-runs
.. date: 2024-07-28 10:44:25 UTC+05:30
.. tags: kraken2, metagenomics, devops
.. category: 
.. link: 
.. description: How to speed up kraken2 classification process
.. type: text
-->

### Mastering Kraken2

[Part 1 - Initial Runs](/2024/07/mastering-kraken2-initial-runs.html) (this post)

[Part 2 - Performance Optimisation](/2024/07/mastering-kraken2-performance-optimisation.html)

[Part 3 - Building custom databases](2024/07/mastering-kraken2-build-custom-db.html)

Part 4 - Regular vs Fast Builds (upcoming)

Part 5 - Benchmarking (upcoming)

### Introduction

Kraken2[^Kraken2] is widely used for metagenomics taxonomic classification, and it has pre-built indexes for many organisms. In this series, we will learn

- How to set up kraken2, download pre-built indices
- Run kraken2 (8GB RAM) at ~0.19 Mbp/m (million base pairs per minute)
- Learn various ways to speed up the classification process
- Run kraken2 (128GB RAM) at ~1200 Mbp/m
- Build custom indices

### Installation

We can install kraken2 from source using the `install_kraken2.sh` script as per the manual[^install_kraken2].

```shell
$ git clone https://github.com/DerrickWood/kraken2
$ cd kraken2
$ ./install_kraken2.sh /usr/local/bin
# ensure kraken2 is in the PATH
$ export PATH=$PATH:/usr/local/bin
```

If you already have conda installed, you can install kraken2 from conda as well.

```shell
$ conda install -c bioconda kraken2
```

If you have `brew` installed on Linux or Mac(including M1), you can install kraken2 using `brew`.

```shell
$ brew install brewsci/bio/kraken2
```

### Download pre-built indices

Building kraken2 indices take a lot of time and resources. For now, let's download and use the pre-built indices. In the final post, we will learn how to build the indices.

Genomic Index Zone[^GenomicIndexZone] provides pre-built indices for kraken2. Let's download the standard database. It contains Refeq archaea, bacteria, viral, plasmid, human1, & UniVec_Core. 

```shell
$ wget https://genome-idx.s3.amazonaws.com/kraken/k2_standard_20240605.tar.gz
$ mkdir k2_standard
$ tar -xvf k2_standard_20240605.tar.gz -C k2_standard
```

The extracted directory contains three files - `hash.k2d`, `opts.k2d`, `taxo.k2d` which are the kraken2 database files.

```shell
$ ls -l *.k2d
.rw-r--r--  83G anand 13 Jul 12:34 hash.k2d
.rw-r--r--   64 anand 13 Jul 12:34 opts.k2d
.rw-r--r-- 4.0M anand 13 Jul 12:34 taxo.k2d
```

### Classification

To run the taxonomic classification, let's use `ERR10359977` human gut meta genome from NCBI SRA.

```shell
$ wget https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR103/077/ERR10359977/ERR10359977.fastq.gz
$ kraken2 --db k2_standard --report report.txt ERR10359977.fastq.gz > output.txt
```

By default, the machine I have used has 8GB RAM and an additioinal 8GB swap. Since kraken2 needs entire db(~80GB) in memory, when the process tries to consume more than 16GB memory, the kernel will kill the process. 

```shell
$ time kraken2 --db k2_standard --paired SRR6915097_1.fastq.gz SRR6915097_2.fastq.gz > output.txt
Loading database information...Command terminated by signal 9
0.02user 275.83system 8:17.43elapsed 55%CPU 
```

To prevent this, let's increase the swap space to 128 GB.

```shell
# Create an empty swapfile of 128GB
sudo dd if=/dev/zero of=/swapfile bs=1G count=128

# Turn swap off - It might take several minutes
sudo swapoff -a

# Set the permissions for swapfile
sudo chmod 0600 /swapfile

# make it a swap area
sudo mkswap /swapfile  

# Turn the swap on
sudo swapon /swapfile
```


We can time the classification process using the `time` command.

```shell
$ time kraken2 --db k2_standard --report report.txt ERR10359977.fastq.gz > output.txt
```

If you have a machine with large RAM, the same scenario can be simulated using `systemd-run`. This will limit the memory usage of kraken2 to 6.5GB. 

```shell
$ time systemd-run --scope -p MemoryMax=6.5G --user time kraken2 --db k2_standard --report report.txt ERR10359977.fastq.gz > output.txt
```

Depending on the CPU performance, this will take around ~40 minutes to complete.

```shell
Loading database information... done.
95064 sequences (14.35 Mbp) processed in 1026.994s (5.6 Kseq/m, 0.84 Mbp/m).
  94939 sequences classified (99.87%)
  125 sequences unclassified (0.13%)
  4.24user 658.68system 38:26.78elapsed 28%CPU 
```

If we try gut WGS(Whole Genome Sequence) sample like `SRR6915097` [^srr1] [^srr2]. which contains ~3.3 Gbp, it will take weeks to complete.

```shell
$ wget -c https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR691/007/SRR6915097/SRR6915097_1.fastq.gz
$ wget -c https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR691/007/SRR6915097/SRR6915097_2.fastq.gz

$ time systemd-run --scope -p MemoryMax=6G --user time kraken2 --db k2_standard --paired SRR6915097_1.fastq.gz SRR6915097_2.fastq.gz > output.txt
```

I tried running this on 8 GB machine. Even after 10 days, it processed only 10% of the data.

If we have to process a large number of such samples, it takes months and this is not a practical solution. 

### Conclusion

In this post, we ran kraken2 on an 8GB machine and learned that it is not feasible to run kraken2 on large samples.

In the next post, we will learn how to speed up the classification process and run classification at 1200 Mbp/m.

**Next**: [Part 2 - Performance Optimisation](/2024/07/mastering-kraken2-performance-optimisation.html)


[^Kraken2]: [Kraken2](https://ccb.jhu.edu/software/kraken2/)

[^install_kraken2]: [Kraken2 - Manual - Install](https://github.com/DerrickWood/kraken2/blob/master/docs/MANUAL.markdown#installation)

[^GenomicIndexZone]: [Genomic Index Zone - k2](https://benlangmead.github.io/aws-indexes/k2)


[^srr1]: [SRR6915097_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR691/007/SRR6915097/SRR6915097_1.fastq.gz)

[^srr2]: [SRR6915097_1.fastq.gz](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR691/007/SRR6915097/SRR6915097_2.fastq.gz)
