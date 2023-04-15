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
price_list = tbody.select("td")
slist = tbody.select("a")

# for i in range(0, len(slist)):
#   print(price_list[i].text)

count = 0

for i in range(0, len(price_list), 2):
  temp = slist[count]
  
  print("종목이름 :", temp.text, "종목코드 :", str(temp)[str(temp).find("code=") + 5:(str(temp).find("code=") + 5) + 6], \
        "현재가 :", price_list[i].text, "전일대비 :", price_list[i + 1].text)
  
  count += 1
