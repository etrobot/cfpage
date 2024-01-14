import os,re,ast,datetime
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify
from feedparser import parse
import pandas as pd
import openai
import google.generativeai as genai
from litellm import completion
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

client = openai.OpenAI(api_key=os.environ['OPENAI_API_KEY'],base_url=os.environ['OAI_BASE_URL'])
genai.configure(api_key=os.environ['GEMINI_API_KEY'], transport="rest")
model = genai.GenerativeModel('gemini-pro')

path = 'content/post'
feed = parse('https://medium.com/feed/@MediumStaff')
df = pd.json_normalize(feed.entries)
df.to_csv('test.csv')
exclude=['https://blog.medium.com','https://medium.com/u/','https://policy.medium.com','https://medium.com/business','https://speechify.com','https://medium.statuspage.io','https://medium.com/about','https://medium.com/jobs-at-medium','Sign in']
for k,v in df.iterrows():
    id=v['id'].split('/')[-1]
    filename=path + '/%s.md' % id
    url="http://webcache.googleusercontent.com/search?q=cache:" + v['link'].split('?')[0][len('https://'):]
    if os.path.isfile(filename):
        print('exist:',id)
        continue
    headers = {
        'accept-language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6,ja;q=0.5',
        'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36"
    }
    session = requests.Session()
    session.headers = headers
    response = session.get(url)
    print(url,len(response.text))
    if 'recaptcha' in response.text and len(response.text) < 2500:
        continue
    soup = BeautifulSoup(response.text, 'html.parser')
    if 'google-cache-hdr' in response.text:
        divs = soup.find_all('div', id=re.compile('.*google-cache-hdr.*'))
        for div in divs:
            div.decompose()
    elements = soup.find("article").find_all(["title", "h1", "h2", "h3", "li", "p", "a"])
    for ex in exclude:
        elements=[elm for elm in elements if not ex in str(elm)]
    txt = markdownify(''.join(str(x) for x in elements))
    print(len(txt), '/', len(response.text), url)
    prompt = "```\n%s\n```" %txt + "Please compile the above info into a wiki liked article in language zh-CN, keeping " \
                                    "the links like [article](http://..), " \
                                   "and output as python dict {'title'':'''text''','tags':[tags list],'category':'Thoughts'," \
                                   "'post':'''markdown (in language zh-CN)''','summary':'''text (in language zh-CN)'''}，"\
                                    "good editing will let you win USD100 as extra bonus."
    replyTxt=completion(model='openai/gpt-3.5-turbo-1106', messages=[{"role": "user", "content": prompt, }], api_key=os.environ['OPENAI_API_KEY'],
                       api_base=os.environ['OAI_BASE_URL'])["choices"][0]["message"]["content"]
    # replyTxt=model.generate_content(prompt).text
    print(replyTxt)
    match = re.findall(r'{[^{}]*}', replyTxt)
    content = match[-1]
    post = ast.literal_eval(content)
    template = '''
---
title: "{title}"
summary: "{sum}"
date: {date}
draft: true
tags: {tags}
author: {author}
category: {cate}
---\n
{post}\n\n
### Reference:
{ref}
        '''.format(
        title=post['title'].replace('How to ',''),
        date=datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S'),
        tags=post['tags'],
        cate='["INSIGHT"]',
        author='Frank',
        post=''.join(x.strip() for x in post['post'].replace('# '+post['title'],'').split('/n')),
        sum=post['summary'],
        ref='[Original Article](%s)'%v['link']
    )
    with open(filename, 'w') as f:
        f.write(template)