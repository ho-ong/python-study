import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com"

result = requests.get(url) # <Response [200]> 반환
html = result.text # html 내용 반환

soup = BeautifulSoup(html, "html.parser") # html을 정확한 규격으로 나눠준다.
print(soup)
