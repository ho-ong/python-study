import requests
from bs4 import BeautifulSoup

url = 'https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'
response = requests.get(url)

# 200(성공) : 서버가 요청을 제대로 처리했다는 뜻
# 네이버 지식인에 파이썬을 검색한 url
# 응답 코드가 200일 때, html을 받아와 soup 객체로 변환
if response.status_code == 200: # 응답 코드가 200일 경우
  html = response.text
  soup = BeautifulSoup(html, 'html.parser')
  
  print(soup)
else: # 응답 코드가 200이 아닐 경우
  print(response.status_code)
