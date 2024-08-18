<!--
.. title: Kraken2 Database Builder
.. slug: kdb
.. date: 2024-08-04 01:21:21 UTC
.. tags:
.. category: projects
.. link:
.. description:
.. type: text
-->


### Kraken2 Database Builder

Build standard & custom databases for Kraken2 with a single command and way faster than default `kraken2-build`.


### Installation

```bash
$ pip install kraken-db-builder
```

### Usage

```bash
kdb --help

kraken-db-builder --help
```

```shell
# To quickly create protozoa database
kdb --db-type protozoa

# To create standard Kraken2 database
kdb --db-type standard

# To build db from a directory containing fasta files
kdb --genomes-dir /path/to/genomes --db-name k2_test --threads 36 
```

### Why kdb(kraken-db-builder)?

kdb was aimed to create to provide a simple and easy to use tool to build wide variety of databases with a single command.

While writing a series of posts on Kraken2, I realised that building Kraken2 databases is a time-consuming process. I wanted to build a tool that can build Kraken2 databases faster and with much ease. That's how `kraken-db-builder` was born.

Mastering Kraken2: [https://avilpage.com/tags/kraken2.html](/tags/kraken2.html)

Source code: [https://github.com/AvilPage/kraken-db-builder](https://github.com/AvilPage/kraken-db-builder)
