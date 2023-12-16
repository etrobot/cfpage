---
title: "如何免费创建7x24资讯秘书"
date: 2023-12-14T00:00:00
tags: ['字节跳动', 'GPT-4']
author: Frank Lin
category: FLASH
---

相信大家都发现了，AI时代成为创作者的捷径就是汇(ban)编(yun)优秀的推文，推上也有不少人靠制作某个话题的推文组合收获很多粉丝，不需要才华，只要靠勤奋高效即可。

工欲善其事，必先利其器，今天就为爱发电，把我的Python脚本“自动抓取指定推特列表或帐号最新X分钟内并用GPT筛选发邮件”分享出来，并附上手把手教程，非技术专业人员（我也不是）都能轻松跑起来：

## 克隆分支

注册GitHub帐号，打开[github.com](https://github.com/etrobot/sumTweets/) 点击folk即可克隆我的项目到你的账号，然后新建环境叫sumTweetsCron(```注意一定要完全一致包括大小写```)

## 设置环境变量

在settings里面加入三个secret,分别是OPENAI\_API\_KEY，MAILPWD，MAILTO，以及六个Environment Vars，分别是MAIL，SMTP，NITTER，MINS，TARGET，INFO，具体含义见下图:

![创建密码](https://cdnv2.ruguoapp.com/FtnKjnzNEF2gYJ_GuhmZ9D-M5fvhv3.png?imageMogr2/auto-orient/thumbnail/1500x2000%3E)
![创建自定义参数变量](https://cdnv2.ruguoapp.com/Fnid7LnjAWSbgyuwsEQ-hevnZDNGv3.png?imageMogr2/auto-orient/thumbnail/1500x2000%3E)


## 定时任务

填完后在Action创建工作流：

![](https://cdnv2.ruguoapp.com/Fg2MGRPKsN9Be5iDzMiDS2qz-QR3v3.png?imageMogr2/auto-orient/thumbnail/1500x2000%3E)


复制以main.yml的内容:

```yaml
name: Main Workflow

on:
  schedule:
    - cron: '*/20 * * * *'

jobs:
  build:
    runs-on: ubuntu-latest
    environment:
      name: sumTweetsCron
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.x
          
      - name: Cache dependencies
        uses: actions/cache@v2
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
          restore-keys: |
            ${{ runner.os }}-pip-

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt


      - name: Run main.py
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          API_BASE_URL: ${{ vars.API_BASE_URL }}
          MAILTO: ${{ secrets.MAILTO }}
          MAIL: ${{ vars.MAIL }}
          SMTP: ${{ vars.SMTP }}
          MAILPWD: ${{ secrets.MAILPWD }}
          NITTER: ${{ vars.NITTER }}
          MINS: ${{ vars.MINS }}
          TARGET: ${{ vars.TARGET }}
          INFO: ${{ vars.INFO }}
        run: python main.py

```


![](https://cdnv2.ruguoapp.com/FtSNbK7Gxoq-tyMuhEay4MV7Sn7jv3.png?imageMogr2/auto-orient/thumbnail/1500x2000%3E)


你可以选择各式各样的主题，比如电动车、奢侈品……账号和列表靠自己筛选，在环境变量里面修改target和info即可~ 希望大家能借助这个Python脚本成为各个细分领域的大（juan）咖（wang）!