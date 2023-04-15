import requests
from bs4 import BeautifulSoup

# openpyxl : 파이썬에서 엑셀을 다루는 것을 쉽게 해주는 도구
from openpyxl import Workbook

# 네이버 파이낸셜 사이트
url = 'https://finance.naver.com/'

# url 요청 (200 성공)
response = requests.get(url)

# 해당 url의 정보 모두 텍스트 형태로 가져온다.
html = response.text

# html의 요소별로 파싱
soup = BeautifulSoup(html, 'html.parser')

# 인기검색종목의 테이블 안의 요소를 가져온다.
tbody = soup.select_one('#container > div.aside > div > div.aside_area.aside_popular > table > tbody')
slist = tbody.select("a")

for i in slist:
  # 종목코드 위치 가져오기
  print(str(i)[str(i).find("code=") + 5:(str(i).find("code=") + 5) + 6])
  print(i.text)
