# -*- coding: utf-8 -*-
import os
import requests
from openai import OpenAI
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

client = OpenAI(
    api_key= os.environ["MOONSHOT_API_KEY"],
    base_url="https://api.moonshot.cn/v1",
)

class KimiWriter:
    def __init__(self):
        pass
    def bingSearch(self,query = "Microsoft")->dict:
        # Add your Bing Search V7 subscription key and endpoint to your environment variables.
        subscription_key = os.environ['BING_SEARCH_V7_SUBSCRIPTION_KEY']
        endpoint = "https://api.bing.microsoft.com/v7.0/search"
        # Construct a request
        mkt = 'global'
        params = {'q': query, 'mkt': mkt}
        headers = {'Ocp-Apim-Subscription-Key': subscription_key}
        # Call the API
        try:
            response = requests.get(endpoint, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except Exception as ex:
            raise ex

    def chat(self,prompt:str)->str:
        completion = client.chat.completions.create(
          model="moonshot-v1-8k",
          messages=[
            {"role": "system", "content": "你是Moonshot AI研发的智能助理kimi"},
            {"role": "user", "content": prompt}
          ],
          temperature=0.7,
        )
        return completion.choices[0].message.content

if __name__=="__main__":
    kimi = KimiWriter()
    prompt='请为『AI会让文字创作良币驱逐劣币』这个题目生成5个以内的搜索引擎关键词，空格分隔'
    sites='site:36kr.com OR site:huxiu.com OR site:tmtpost.com'
    keywords =kimi.chat(prompt)
    print(keywords)
    serp_result =  kimi.bingSearch(keywords)
    print(serp_result)