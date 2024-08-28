<!--
.. title: Mastering Kraken2 - Part 4 - Build FDA-ARGOS Index
.. slug: mastering-kraken2-fda-argos-index
.. date: 2024-08-24 15:28:00 UTC+05:30
.. tags: bioinformatics, metagenomics, kraken2
.. category: bioinformatics
.. link: 
.. description: 
.. type: text
-->

### Mastering Kraken2

[Part 1 - Initial Runs](/2024/07/mastering-kraken2-initial-runs.html)

[Part 2 - Classification Performance Optimisation](/2024/07/mastering-kraken2-performance-optimisation.html)

[Part 3 - Build custom database indices](/2024/07/mastering-kraken2-build-custom-db.html)

[Part 4 - Build FDA-ARGOS index](/2024/08/mastering-kraken2-fda-argos-index.html) (this post)

Part 5 - Regular vs Fast Builds (upcoming)

Part 6 - Benchmarking (upcoming)

### Introduction

In the previous post, we learnt how to build a custom index for Kraken2.

FDA-ARGOS[^argos] is a popular database with quality reference genomes for diagnostic usage. Let's build an index for FDA-ARGOS.

### FDA-ARGOS Kraken2 Index

FDA-ARGOS db is available at NCBI[^ncbi] from which we can download the assembly file.

<img src="/images/fda-argos-kraken2-index.png" alt="FDA-ARGOS NCBI" class="img-fluid">

We can extract accession numbers from the assembly file and then download the genomes from these accession ids.

```shell
$ grep -e "^#" -v PRJNA231221_AssemblyDetails.txt | cut -d$'\t' -f1 > accessions.txt

$ wc accessions.txt
 1428  1428 22848 accessions.txt
 
$ ncbi-genome-download --section genbank --assembly-accessions accessions.txt --progress-bar bacteria --parallel 40
```

It took ~8 minutes to download all the genomes, and the downloaded file size is ~4GB.

We can use kraken-db-builder[^kdb] tool to build index from these genbank genome files.

```shell
# kraken-db-builder needs this to convert gbff to fasta format
$ conda install -c bioconda any2fasta

$ kraken-db-builder --genomes-dir genbank --threads 36 --db-name k2_argos
```

It took ~30 minutes to build the index.

### Conclusion

We have built a Kraken2 index for the FDA-ARGOS database on 2024-Aug-24.

- [FDA-ARGOS Library](https://github.com/ChillarAnand/avilpage.com/tree/master/scripts/kraken2_argos)
- [Kraken2 Gzipped Index file](https://drive.google.com/file/d/1PbwriW3i3pkXJMFF5nq9OK_EqrwPiLWr/view) (gzip size: 2.6GB, index size: 3.8GB, md5sum: 1dd946d2e405dfec35ed3e319e9dfeac)
- [Kraken2 Inspect file](https://github.com/ChillarAnand/avilpage.com/tree/master/scripts/kraken2_argos)

In the next post, we will look at the differences between regular and fast builds.


[^argos]: [https://www.nature.com/articles/s41467-019-11306-6](https://www.nature.com/articles/s41467-019-11306-6)

[^ncbi]: [https://www.ncbi.nlm.nih.gov/bioproject/231221](https://www.ncbi.nlm.nih.gov/bioproject/231221)

[^kdb]: [https://avilpage.com/kdb.html](https://avilpage.com/kdb.html)
