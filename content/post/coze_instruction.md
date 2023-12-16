---
title: "快速玩转字节的Coze机器人创建平台"
date: 2023-12-16T00:00:00
tags: ['字节跳动', 'GPT-4']
author: Frank Lin
category: FLASH
---

Coze.com是制作bot的平台不用梯，ciciai和discord是发布平台（要梯），自用的话用Coze.com即可，目前还是非常大方的，没有感受到限制
，gpt-4(8k)、gpt4-V、Dall-E 3随便用

## 快速玩转

如何快速玩转字节的Coze机器人创建平台？我已经将帮助文档转存到网盘: [pan.baidu.com](https://pan.baidu.com/s/18RZQa0B_tB7PbAeXYZFZWw?pwd=yd3c) 可以直接按照coze的文档上传成知识库，按[www.coze.com](https://www.coze.com/docs/zh_cn/knowledge.html)的指示添加，然后就可以免费让GPT-4看着官方帮助来教你了。

## 实践例子：

识图能力(GPT-4V)：用Coze提供的免费GPT-4和GPT-V制作第2个聊天机器人，这次是将脑图转成文本代码，结果发现，发布到Ciciai上没有上传图片的入口，尴尬了，看起来这个产品还比较初级。

workflow: 字节的coze.com就是一个翻版的GPTs，自定义程度更高，除了插件、知识库和音图识别，值得研究的是workflow可以玩出花来的的组件(借鉴了Langflow开源项目)。
体验了一上午，做了一个推特AI资讯书童bot:www.ciciai.com

## 做这个能赚钱吗？

字节Coze制作的机器人可能比GPTs更容易盈利💰？昨天有成就感的事就是一位老同学专程驱车跨市来找我教他用AI解决一个实际问题：为一个视觉检测硬件设计配套软件产品。

我推荐了Coze 并教他整理了硬件技术文档作为AI的知识库，以及如何写提示词来让AI更加靠谱。📑

AI本身能力的提升只能依赖大厂，但独特的、快速更新的附加知识库是普通人可以努力的事情，而且Coze是可以一键发布成Discord Bot的，也就有了变现的可能～ 附图是我成功将一个读图片转markdown/mermaid图表的BOT成功发布到discord上。

🤖今天我也制作了一个探讨如何用coze制作discord bot来盈利的机器人：[Discord Bot Maker](https://discord.com/api/oauth2/authorize?client_id=1185508364701151284&permissions=0&scope=bot) ，用了谷歌搜索插件和coze自己的文档作为知识库

制作知识库用的是开源的项目GPT-Crawler [github.com](https://github.com/BuilderIO/gpt-crawler) 一键将coze的文档转成了知识库并上传，非常方便🧑🏿💻，大家可以体验一下，整理好的知识库可以再其他平台上传制作bot，重复利用率很高。