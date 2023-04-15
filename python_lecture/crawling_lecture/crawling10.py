from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import time

# 크림 덩크 - 신발 분류
url = 'https://kream.co.kr/search?category_id=34&keyword=%EB%8D%A9%ED%81%AC&sort=popular&per_page=40'
driver = webdriver.Chrome('./chromedriver')
driver.get(url)

# 스크롤 기다려주는 시간
SCROLL_PAUSE_TIME = 2

# 마지막 시점의 창 높이 저장
last_height = driver.execute_script("return document.body.scrollHeight")

# while True :
for i in range(0, 2):
  # 창 높이까지 스크롤
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

  # 스크롤 후 창이 로딩될 때까지 2초를 기다리겠다는 명령어, 로딩이 완료되면 바로 넘어간다.
  time.sleep(SCROLL_PAUSE_TIME)

  # 한번에 맨 마지막까지 스크롤되면 아래 리스트가 뜨지 않아서,
  # 마지막을 찍고 조금 창을 올리는 방법으로 리스트가 로딩될 수 있게 한다.
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")

  time.sleep(SCROLL_PAUSE_TIME)

  # 스크롤이 된 후의 창 높이를 새로운 높이로 저장
  new_height = driver.execute_script("return document.body.scrollHeight")

  # 새로운 높이가 이전 높이와 변하지 않았으면 스크롤 종료
  if new_height == last_height:
    break
  last_height = new_height

# 스크롤을 다 내렸으면 페이지의 모든 정보를 긁어온다.
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# 모든 가격 요소 불러오기
'''
price = soup.find_all(class_='amount')

print(price)

for i in price:
  with open("./jor.txt", "a") as f:
    f.write(i.text + '\n')
'''

# 모든 이미지 불러오기
img2 = soup.find_all(class_='picture product_img')

n = 1

# 이미지 크롤링 시작
for i in img2:
  # 이미지 url 따오기
  imgUrl = i.find("img")["src"]

  # 이미지 저장
  # urlopen(imgUrl)은 이미지 데이터
  with urlopen(imgUrl) as f:
    # w - write b - binary
    with open('./images/img' + str(n) + '.jpg', 'wb') as h:
      img = f.read()
      h.write(img)
      
  n += 1
  print(imgUrl)
