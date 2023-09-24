<!--
.. title: Train LLMs with Custom Dataset on Laptop
.. slug: train-llm-custom-data-laptop
.. date: 2023-07-07 04:36:42 UTC+05:30
.. tags: python, artificial-intelligence
.. category: programming
.. link: 
.. description: How to train LLM (like ChatGPT, Vicuna) with custom documents on the laptop.
.. type: text
-->

### Problem Statement

I want to train a Large Language Model(LLM)[^LLM] with some private documents and query various details.

### Journey

There are open-source available LLMs like Vicuna, LLaMa, etc which can be trained on custom data. However, training these models on custom data is not a trivial task.

After trying out various methods, I ended up using privateGPT[^privateGPT] which is quite easy to train on custom documents. There is no need to format or clean up the data as privateGPT can directly consume documents in many formats like txt, html, epub, pdf, etc.

### Training

First, let's clone the repo, install requirements.txt and download the default model.

```bash
$ git clone https://github.com/imartinez/privateGPT
$ cd privateGPT
$ pip3 install -r requirements.txt
$ wget https://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin

$ cp example.env .env
$ cat .env
MODEL_TYPE=GPT4All
MODEL_PATH=ggml-gpt4all-j-v1.3-groovy.bin
```

I have sourced all documents and kept them in a folder called `docs`. Let's ingest(train) the data.

```bash
$ cp ~/docs/* source_documents

$ python ingest.py
```

This will take a while depending on the number of documents we have. Once the ingestion is done, we can start querying the model.

```bash
$ python privateGPT.py
Enter a query: Summarise about Gaaliveedu
```

The default `GPT4All-J v1.3-groovy`[^gpt4all] model doesn't provide good results. We can easily swap it with `LlamaCpp`[^llama.cpp]. Lets download the model and convert it.


```bash
$ git clone https://huggingface.co/openlm-research/open_llama_13b

$ git clone https://github.com/ggerganov/llama.cpp.git
$ cd llama.cpp
$ python convert.py ../open_llama_13b
Wrote ../open_llama_13b/ggml-model-f16.bin
```

We can now update the `.env` file to use the new model and start querying again.

```bash
$ cat .env
MODEL_TYPE=LlamaCpp
MODEL_PATH=/path/to/ggml-model-f16.bin

$ python privateGPT.py
Enter a query: Summarise about Gaaliveedu
```

### Conclusion

This makes it easy to build domain-specific LLMs and use them for various tasks. I have used this to build a chatbot for my internal docs and it is working well.


[^LLM]: [https://en.wikipedia.org/wiki/Large_language_model](https://en.wikipedia.org/wiki/Large_language_model)

[^privateGPT]: [https://github.com/imartinez/privateGPT](https://github.com/imartinez/privateGPT)

[^gpt4all]: [https://github.com/nomic-ai/gpt4all](https://github.com/nomic-ai/gpt4all)

[^llama.cpp]: [https://github.com/ggerganov/llama.cpp](https://github.com/ggerganov/llama.cpp)
