# ipykernel (#%% 기입 후 control + enter)

import pandas as pd
import requests
from bs4 import BeautifulSoup

raw = requests.get("https://search.naver.com/search.naver?where=news&query=딥러닝")
html = BeautifulSoup(raw.text, "html.parser")

# 뉴스 기사 요소 덩어리를 가져와 줘야 한다. (li)
articles = html.select("ul.list_news > li")
source = articles[0].select_one("div.dsc_wrap").select("a")[0].text

# class 이름을 띄어쓰기로 해놓아서 Fake 거는 경우가 있다.
# 선택자에는 띄어쓰기가 자식 요소로 판별된다.

title_list = [] # 뉴스 제목 리스트
content_list = [] # 뉴스 내용 리스트

for i in range(len(articles)):
  title = articles[0].select_one("a.news_tit").text
  content = articles[i].select_one("div.dsc_wrap").text
  title_list.append(title)
  content_list.append(content)

# csv로 저장하기
sdict = {
  '제목': title_list,
  '내용': content_list
}

title_content = pd.DataFrame(sdict)
title_content.to_csv("./crawling_result.csv", index=False)
print(title_content)
