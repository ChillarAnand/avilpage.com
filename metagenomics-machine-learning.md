<!--
.. title: Metagenomics Machine Learning
.. slug: metagenomics-machine-learning
.. date: 2024-08-08 03:29:59 UTC
.. updated: 2024-08-08 03:29:59 UTC
.. tags: bioinformatics, metagenomics
.. category:
.. link:
.. description: Metagenomics Classification - Workshop material
.. type: text
-->

### Introduction

This is the reference material for the "Machine Learning in Metagenomics" workshop. By the end of workshop, you will be able to classify metagenomic samples using Kraken2 and predict the source organism of the sample with simple ML methods.

### Environment Setup

We will be using Python, Jupyter notebook and command line tools for this workshop.

If you are using Windows, you can install WSL2 and use Ubuntu. If you are using Mac, you can use the terminal.

### Running Kraken2

In the first step, let's generate abundance report using Kraken2. Kraken2 is a taxonomic sequence classifier that assigns taxonomic labels to short DNA sequences.

Install anaconda

```shell
$ wget https://repo.anaconda.com/archive/Anaconda3-2024.06-1-Linux-x86_64.sh
$ bash Anaconda3-2021.05-Linux-x86_64.sh
```

Install kraken2

```shell
$ conda install -c bioconda kraken2
```

Download pre-built viral database

```shell
$ wget -c https://genome-idx.s3.amazonaws.com/kraken/k2_viral_20240605.tar.gz
$ mkdir -p k2_viral
$ tar -xzvf k2_viral_20240605.tar.gz -C k2_viral
```

Download sample fastq files

```shell
$ wget -c https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR103/077/ERR10359977/ERR10359977.fastq.gz
```

Kraken2 classification

```shell
$ kraken2 --db k2_viral ERR10359977.fastq.gz --report k2_report.txt --output k2_output.txt
```

### Generate Krona plot

Install Krona & update taxonomy

```shell
$ conda install -c bioconda krona
$ ktUpdateTaxonomy.sh
```
Generate Krona plot

```shell
$ ktImportTaxonomy k2_report.txt -o k2_report.html
```

### Building custom database

Download taxanomy

```shell
$ kraken2-build --download-taxonomy --db k2_fungi
```

Download required genomes

```shell
$ ncbi-genome-download --format fasta --section refseq --assembly-level complete fungi -v
```

Build kraken2 database
```shell
$ find refseq -name "*.gz" -print0 | parallel -0 gunzip

$ find refseq -name "*.fna" -exec kraken2-build --add-to-library {} --db custom_db \;

$ kraken2-build --db custom_db --build --threads 36
```

Using `kraken-db-builder` to build database

```shell
$ pip install ncbi-genome-download kraken-db-builder

$ kraken-db-builder --db-type fungi
```

### Predicting Source of Metagenomic Sample

Geometry Mean of Pairwise Ratios (GMPR)

Bray-Curtis dissimilarity

t-Stochastic Neighbor Embedding (t-SNE)

k-Nearest Neighbors (k-NN)


Download sample data

```shell
$ wget https://raw.githubusercontent.com/maxibor/sourcepredict/master/data/test/dog_test_sink_sample.csv -O dog_example.csv
$ wget https://raw.githubusercontent.com/maxibor/sourcepredict/master/data/modern_gut_microbiomes_labels.csv -O sp_labels.csv
$ wget https://raw.githubusercontent.com/maxibor/sourcepredict/master/data/modern_gut_microbiomes_sources.csv -O sp_sources.csv
```

Download sourcepredict

```shell
$ python -m pip install git+https://github.com/AvilPage/sourcepredict
```

### Machine Learning Notebooks

[https://github.com/ChillarAnand/avilpage.com/tree/master/mg_workshop](https://github.com/ChillarAnand/avilpage.com/tree/master/mg_workshop)


### Useful links:

[https://benlangmead.github.io/aws-indexes/k2](https://benlangmead.github.io/aws-indexes/k2
)

[https://jszym.com/blog/dna_protein_complexity/](https://jszym.com/blog/dna_protein_complexity)

[https://avilpage.com/2024/07/mastering-kraken2-initial-runs.html](https://avilpage.com/2024/07/mastering-kraken2-initial-runs.html)

[https://github.com/maxibor/sourcepredict](https://github.com/maxibor/sourcepredict)
