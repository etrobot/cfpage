---
title: "如何复刻妙鸭相机"
date: 2023-08-06T08:12:48
tags: ['人工智能', '最新资讯', '技术']
author: Frank Lin
category: FLASH
---

妙鸭是最近大火的AI写真应用，应该是借鉴了国外的photoai等产品，利用现有技术是可以复制的，以下是步骤：

### 步骤：

1、模型选择Stable Diffussion，目前最火的开源文生图项目。

2、调试一系列提示词用于生成各类模板的AI形象照，搭配controlnet扩展调整参数让生成相对稳定。

3、使用Roop扩展将用户上传的照片进行换脸，这样比使用lora方式进行训练要更加快速。

4、创建一个 Web 应用，可以进行用户管理，允许用户上传自己的照片，查看等待进度和结果。

5、部署模型服务。

### 部署：

有多种方法可以将 Stable Diffusion 部署为服务：

可以使用[diffuzers API](https://link.zhihu.com/?target=https%3A//www.youtube.com/watch%3Fv%3DReO6vqJxg-s)，一个用于 Stable Diffusion的 Web UI 和可部署 API。

可以使用[Lightning Apps 框架](https://link.zhihu.com/?target=https%3A//github.com/Lightning-Universe/stable-diffusion-deploy)，是一个用于构建、发布和扩展 AI 应用程序的开源框架，为 Stable Diffusion提供了一个生产就绪的服务器，可以处理负载平衡、GPU 推理、性能测试、微服务编排等。还可以配置工作人员数量、批量大小。

可以使用[BentoML](https://link.zhihu.com/?target=https%3A//bentoml.com/blog/deploying-your-own-stable-diffusion-service-mz9wk)，是一个用于将机器学习模型构建和部署为服务的平台，可以将 Stable Diffusion 打包为 BentoML 服务，该服务可以部署到各种云平台，例如 AWS EC2、AWS Lambda、Google Cloud Run 等。还可以使用 BentoML 的 Web UI 或 CLI 监控和管理部署的服务工具。

### 总结：

AI应用不是技术问题，而是产品和工程问题，底层最复杂的技术已经包含在开源大模型中，而产品需要考虑的，是如何让用户觉得这个技术和ta有关，这才有付费的冲动，所以还有很多领域可以进行AI生成，比AI家装效果图、AI试穿等，广阔的新天地等待勇者的开拓，我很期待。