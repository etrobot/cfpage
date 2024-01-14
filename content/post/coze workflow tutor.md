---
title: "字节Coze平台workflow抓取推文教程"
date: 2023-12-17T00:00:00
tags: ["字节跳动", "GPT-4"]
author: Frank Lin
category: FLASH
---

![图片](https://mmbiz.qpic.cn/mmbiz_png/8d8ZEW9VW7YPuOibAcbj6xhD9kPAhIYEauSB9SyQaibA75D0vOicUOiaAn8VYHF5HP4nKAOJYJBN14YThhcz6WbeUw/640?width=300&height=200)

字节Coze的workflow非常灵活，可以结合搜索、浏览、代码片段、GPT-3.5/4/4V等组件实现很多复杂的逻辑。本文是实现的是GPT自行筛选推特AI资讯获取，具体步骤：

### 1、配置start卡片，设变量名：TwitterUserOrListID

require我关掉了，因为下一步我会用代码自动判断是否有参数，否则使用默认参数。

![图片](https://mmbiz.qpic.cn/mmbiz_png/8d8ZEW9VW7YPuOibAcbj6xhD9kPAhIYEaag6aNly672Sz3oQB4GSE7rqNQLEibfNpib7fHxuG6AebsGGDmbeick8Cw/640)

### 2、处理用户输入目标推特账号或列表，没有则使用默认的列表ID

### 『/i/status/1733672915130847419』

通过侧边栏（默认是Basic nodes）插入一个Code卡片,代码输入：  

```javascript
async({params})=>{
const ret={
    "key0":"https://nitter.io.lol/"+ (
        params.input==""?"i/lists/1733652180576686386":params.input.replace("@","")
        )+"/rss"
 }
return ret
}
```
Output选择key0，也就是代码里面的输出字段名称，然后拖动Start卡片右侧小蓝点连线上来，这样input栏就可以选择Start卡片传过来的url参数了：

![图片](https://mmbiz.qpic.cn/mmbiz_png/8d8ZEW9VW7YPuOibAcbj6xhD9kPAhIYEaFpZdSPCzicRzm7dnVS8Sw9BLVKTHfe2XM5cibMMQK7s7PFD7JVAvjyPQ/640)

### 3、使用浏览插件进行账号或列表的推文抓取

左侧边栏点击Tools,加入一个browser卡片，选择raw(可以返回详细内容)，再将上一步的code卡片连上来，输入就可以选择code卡片的key0参数了：

![图片](https://mmbiz.qpic.cn/mmbiz_png/8d8ZEW9VW7YPuOibAcbj6xhD9kPAhIYEaELySftGfkvcFffqF69ZxhpkribyEceC2TQaZejpRND1AEE9HQYBjIcA/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1)

### 4、使用Gpt-3.5-turbo 筛选推文

左侧导航栏再切换回Basic nodes，点击LLM插入一个LLM卡片，将它与上一步的浏览器卡片和最后一步的End卡片连接，输入选择上一个卡片的参数，注意Prompt要加入花括号引用input参数名{{twitter\_rss}}，最后End卡片的输出选择Return Variable即可：

![图片](https://mmbiz.qpic.cn/mmbiz_png/8d8ZEW9VW7YPuOibAcbj6xhD9kPAhIYEak3k7vUI0Ak7U0FOlfKQLMPuOLHHCxGTyaptENc7VKL9gNB2r93VSag/640)

『{{twitter\_rss}}』以上是一些推文，你是一名专栏『AI/人工智能最新资讯』的资深作者，请在以上推文中，挑选出和『AI/RAG/人工智能』相关信息的推,汇编成一篇用markdown排版的文章，包含发推时间、作者、推特链接和推特内容以及你的解读和评论。如果推文中没有『AI/RAG/人工智能』相关信息则回复『暂未找到最新AI资讯』

### 5、测试发布

点击右上方Test run,这时开始测试运行，每个卡片右上角可以查看结果，如果没有问题就点击Publish即可，然后就可以在创建bot的时候引用啦：

![图片](https://mmbiz.qpic.cn/mmbiz_png/8d8ZEW9VW7YPuOibAcbj6xhD9kPAhIYEayaibrHKibiapVIKibiabppGklfVnt8x26LYSzPia5wPDfJ4AbCPYluD3ib9iaA/640)

附上主要步骤全景截图：

![图片](https://mmbiz.qpic.cn/mmbiz_png/8d8ZEW9VW7YPuOibAcbj6xhD9kPAhIYEaxX3CZUJZSl7bYe9hOu8BH4Yl2LIm4o2Y7BlaNMHE2d6pN4y8KfiafFA/640)

### 总结

workflow的就是将一个个的数据处理单元连接起来，所以只要仔细检查好参数的传递逻辑，就能流畅运行，这里面当然有很多技巧，是需要经验的，所以对有编程基础的人来说更容易上手，如果想玩好workflow，建议还是学习一下编程基础知识，比如Python，最好实战一点爬虫项目，才能更好的理解数据流动和处理的方方面面。


        