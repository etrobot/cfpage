
---
title: "A Fast Guide to Using SDXL with Conf UI"
date: 2023-07-30T08:52:46
draft: true
tags: ['SDXL', 'Conf UI', 'Automatic 1111', 'Google Colab']
author: Frank
category: efficiency
---

## Overview

This post provides a quick tutorial on using the SDXL AI model with Conf UI for fast high-quality image generation.

## Steps

1. Download and install Conf UI from the provided link. Be sure to update to the latest version.

2. Open the Conf UI canvas and import the pre-made SDXL workflow provided. This sets up all nodes needed.

3. Load your SDXL base and refiner models into the appropriate nodes.

4. Enter your prompts and set rendering parameters like steps.

5. Click "Q prompt" to generate your image. With a good GPU like an RTX 4080, images render in 9 seconds!

## Google Colab Setup

You can also use Google Colab and its free GPU to run Conf UI:

1. Open the Colab notebook link and connect to a GPU runtime. 

2. Install the SDXL models and LocalTunnel dependency. 

3. Launch the LocalTunnel UI link provided.

4. Import the SDXL workflow and load models.

5. Generate images! Speed will be slower than local GPU but still usable.

## Conclusion

Using Conf UI provides a fast way to leverage SDXL for high-quality results with minimal setup. The predefined workflow makes the process easy. Google Colab integration grants GPU access for free.


### Reference:
SDXL 1.0 - SUPER FAST Render Times + Google Colab Guide:
{{< youtube TYk6taV-gVc allow_fullscreen>}}
        