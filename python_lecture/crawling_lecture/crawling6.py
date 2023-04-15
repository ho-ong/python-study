import pandas as pd
import requests
from bs4 import BeautifulSoup

page_list = []

for i in range(1, 302, 10):
  page_list.append(str(i))

print(page_list)

title_list = [] # 뉴스 제목 리스트
content_list = [] # 뉴스 내용 리스트

for page in page_list:
  raw = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EB%94%A5%EB%9F%AC%EB%8B%9D&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=19&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start={page}")
  html = BeautifulSoup(raw.text, "html.parser")
  articles = html.select("ul.list_news > li")

  for i in range(len(articles)):
    title = articles[i].select_one("a.news_tit").text
    content = articles[i].select_one("div.dsc_wrap").text
    title_list.append(title)
    content_list.append(content)

# csv로 저장하기
sdict = {
  '제목': title_list,
  '내용': content_list
}

title_content = pd.DataFrame(sdict)
title_content.to_csv("./crawling_result2.csv", index=False)
