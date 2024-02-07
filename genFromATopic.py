import base64

from gnews import GNews
import openai
import os
import pandas as pd

client = openai.OpenAI(api_key=os.environ['OPENAI_API_KEY'],base_url=os.environ['OAI_BASE_URL'])


class gWriter:
    def __init__(self):
        pass

    def chat(self,prompt:str)->str:
        completion = client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
          ],
          temperature=0.7,
        )
        return completion.choices[0].message.content
    def gnewSerp(self,query:str)->str:
        google_news = GNews()
        search_news = google_news.get_news(query)
        serpDf=pd.DataFrame(search_news)
        serpDf['url']=base64.b64decode(serpDf['url'].str.split('/')[-1].split('?')[0]).decode("utf-8")
        print(serpDf['url'].to_csv())
        return serpDf.to_csv()

if __name__=="__main__":
    gpt = gWriter()
    # prompt="请为『AI会让文字创作良币驱逐劣币』这个题目生成5个以内的搜索引擎关键词，空格分隔"
    # keywords =gpt.chat(prompt)
    # print(keywords)
    serp_result = gpt.gnewSerp("")
    print(serp_result)