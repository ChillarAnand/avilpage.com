<!--
.. title: Using LSTM-CTC For Complex Script Recognistion
.. slug: using-lstm-ctc-for-complex-script-recognistion
.. date: 2017-07-22 14:09:32 UTC
.. tags: machine-learning
.. category: python
.. link:
.. description:
.. type: text
-->

Most Indian languages have strong consonant-vowel structure which combine to give syllables. These syllables are written as one continuous ligature and they require [complex text rendering](https://en.wikipedia.org/wiki/Complex_text_layout) (CTL) for type setting.

Writing OCR (Optical Character Recognistion) software for CTL scripts is a challenging task as segmentation is hard. Because of this overall accuracy drops drastically.

A better approach is to use [Connectionist Temporal Classification](ftp://ftp.idsia.ch/pub/juergen/icml2006.pdf) (CTC) which can identify unsegmented sequence directly as it has one-to-one correspondence between input samples and output labels.

Here is a sample input and output of a [RNN-CTC](https://github.com/rakeshvar/rnn_ctc) network which takes an unsegmented sequence and outputs labels.

<p align="center">
<img src="/images/ctc.png" >
</p>

Open source OCR software [ocorpy](https://github.com/tmbdev/ocropy/) uses BLSTM-CTC for text recognistion. [Tesseract](https://github.com/tesseract-ocr/tesseract) started using the same in its latest(4.0) version.

I have [trained a model](https://github.com/ChillarAnand/likitham) to recognize Telugu script using ocropy and the accuracy is ~99% which is far better when compared to OCR softwares without CTC which are accurate to ~70%.
