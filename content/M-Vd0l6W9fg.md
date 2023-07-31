
---
title: "Face Swapping in Stable Diffusion using Rupe"
date: 2023-07-30T09:03:29
draft: true
tags: ['Stable Diffusion', 'Rupe', 'GitHub']
author: Claude
category: efficiency
---

## Introduction

Rupe is a new extension for swapping faces in images generated with Stable Diffusion. It allows you to easily replace a face in an image with a different face from another image.

## Installation

Installing Rupe in Stable Diffusion is very easy. Just go to the Extensions tab in the UI, click on "Load from URL" under the Available section, and install the Rupe extension from the SD Web UI Extensions group. After installing, enable Rupe in the Installed tab and restart the UI.

Rupe is available on [GitHub](https://github.com/ Automatic1111/stable-diffusion-webui-rupe), where you can find extra tips and information, like needing to install Microsoft Visual Studio on Windows.

## Usage

To use Rupe, first generate an image with at least one face. Rupe will only swap existing faces in images, so it requires a starting image with a face.

Enable Rupe in the extensions sidebar and select a face image. Then click Generate to swap the selected face into the image.

Rupe has options to control face restoration quality, upscaling, and more. Restoring the face is important for quality, as seen when turning it off results in a blurry face.

You can provide a comma separated list of faces to swap multiple faces in an image.

One limitation is Rupe tends to output photorealistic faces. So cartoony faces don't swap as cleanly. But it works great for making lively portraits from old paintings!

## Conclusion

Rupe makes face swapping in Stable Diffusion a breeze. It's an easy way to customize faces for portraits, paintings, and more. Just enable, provide the new face, and generate for seamless face swaps.


### Reference:
Easy "Deepfakes" In Automatic1111 with Roop!:
{{< youtube M-Vd0l6W9fg allow_fullscreen>}}
        