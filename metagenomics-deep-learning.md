<!--
.. title: Metagenomics Deep Learning
.. slug: metagenomics-deep-learning
.. date: 2024-11-08 03:29:59 UTC
.. updated: 2024-11-08 03:29:59 UTC
.. tags: bioinformatics, metagenomics
.. category:
.. link:
.. description: Metagenomics Deep Learning - Workshop material
.. type: text
-->

### Introduction

This is the reference material for the "Deep Learning in Metagenomics" workshop. By the end of workshop, you will be able to understand what is deep learning and how to apply to metagenomics taxanomic classification.

[Click here for "Metagenomics - Machine Learning" workshop](/metagenomics-machine-learning.html)

### Environment Setup

We will be using Python, Jupyter notebook and command line tools for this workshop.

If you are using Windows, you can install WSL2 and use Ubuntu. If you are using Mac, you can use the terminal.

- Install anaconda
- Create new environment
- Install required packages

```shell
$ wget https://repo.anaconda.com/archive/Anaconda3-2024.06-1-Linux-x86_64.sh

$ bash Anaconda3-2021.05-Linux-x86_64.sh

$ conda create -n mgdl -c fkretschmer bertax

$ conda activate mgdl

$ pip install keras-bert==0.86.0 numpy==1.23.0

$ mkdir -p workshop; cd workshop

$ git clone https://github.com/rnajena/bertax

$ pip install -e bertax

$ cd bertax

$ cd bertax/resources

$ wget https://github.com/rnajena/bertax/releases/latest/download/big_trainingset_all_fix_classes_selection.h5
```


### Machine Learning Notebooks

[https://github.com/ChillarAnand/avilpage.com/tree/master/mg_workshop](https://github.com/ChillarAnand/avilpage.com/tree/master/mg_workshop)


### Resources

- [https://keras.io/api/datasets/mnist/](https://keras.io/api/datasets/mnist/)
- [https://github.com/MicrobeLab/DeepMicrobes](https://github.com/MicrobeLab/DeepMicrobes)
- [https://github.com/rnajena/bertax](https://github.com/rnajena/bertax)


### Feedback

Please take a moment to [provide your feedback here](https://forms.gle/qoVTm2RCnCXrsjrk9)
