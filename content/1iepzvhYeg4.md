
---
title: "Running Large Language Models at Home Using Petals"
date: 2023-07-30T09:14:13
draft: true
tags: ['Petals', 'LLM', 'GPT', 'Transformer']
author: Claude
category: efficiency
---

## Overview

Petals is an open source project that allows running large language models (LLMs) like LLMa, GPT-3 etc in a distributed, peer-to-peer fashion similar to BitTorrent. By sharing GPU resources with others, you can run models too large to fit on a single GPU.

## How It Works 

With Petals, each peer downloads a part of the model weights and relies on other peers for the remaining weights. This allows running models with billions of parameters by distributing the load across multiple GPUs.

Some benefits:

- Run huge 175B parameter models like Bloom at home
- Faster fine-tuning and inference, upto 10x faster than single GPU
- Ability to create private swarms for sensitive data

## Demo

The Petals authors have hosted a [live demo](https://chat.petals.div) showing LM capabilities and speed. Some observations:

- Fast generation, ~6 tokens/sec on 70B parameter LLMa
- Can have conversational interactions
- Integration ready for apps via API

## Running Locally

To use Petals locally, install the Python package and import the `AutoDistributedModel` class. Instantiate the model by pointing to a Petals model like LLMa. 

Then generate text by calling `model.generate()` similar to regular Transformers.

A Colab notebook is available to run the models in Google Colab.

## Applications

Possible applications include:

- Building chatbots and conversational agents
- Text generation for creative writing 
- Running LLM fine-tuning for custom datasets

The distributed nature makes it easy to leverage large SOTA models.

## References

- [Petals Project Page](https://petals.div)
- [Colab Notebook](https://colab.research.google.com/drive/1Zt-_dTja_SO72DhD8w2NJfB4RJcR9wIv)
- [Petals Paper](https://arxiv.org/abs/2302.05116)


### Reference:
Torrent for Running Huge GPT-LLMs:
{{< youtube 1iepzvhYeg4 allow_fullscreen>}}
        