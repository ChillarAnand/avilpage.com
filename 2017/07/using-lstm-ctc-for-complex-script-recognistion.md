<!--
.. title: Using LSTM-CTC For Complex Script Recognition
.. slug: using-lstm-ctc-for-complex-script-recognistion
.. date: 2017-07-22 14:09:32 UTC
.. updated: 2023-07-04 14:09:32 UTC
.. tags: python, data-science, artificial-intelligence
.. category: programming
.. link: 
.. description: Use LSTM-CTC for complex script recognition
.. type: text
-->

Most Indian languages have strong consonant-vowel structures which combine to give syllables. These syllables are written as one continuous ligature and they require [complex text rendering](https://en.wikipedia.org/wiki/Complex_text_layout) (CTL) for type setting.

Writing OCR (Optical Character Recognition) software for CTL scripts is a challenging task as segmentation is hard. Because of this overall accuracy drops drastically.

A better approach is to use Connectionist Temporal Classification[^ctc](CTC) which can identify unsegmented sequence directly as it has a one-to-one correspondence between input samples and output labels.

Here is a sample input and output of an [RNN-CTC](https://github.com/rakeshvar/rnn_ctc) network which takes an unsegmented sequence and outputs labels.

<p align="center">
<img src="/images/ctc.png" >
</p>

Open-source OCR software [ocorpy](https://github.com/tmbdev/ocropy/) uses BLSTM-CTC for text recognition. [Tesseract](https://github.com/tesseract-ocr/tesseract) started using the same in its latest(4.0) version.

I have [trained a model](https://github.com/ChillarAnand/likitham) to recognize Telugu script using Ocropy and the accuracy is ~99% which is far better when compared to OCR software without CTC which are accurate to ~70%.

[^ctc]: [https://en.wikipedia.org/wiki/Connectionist_temporal_classification](https://en.wikipedia.org/wiki/Connectionist_temporal_classification)
